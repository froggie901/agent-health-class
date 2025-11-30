import logging
import os
import asyncio
from dotenv import load_dotenv
from typing import Any, Dict

from google.adk.agents import Agent, LlmAgent, SequentialAgent
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.models.google_llm import Gemini
from google.adk.sessions import DatabaseSessionService

from google.adk.runners import Runner
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from google.adk.plugins.logging_plugin import (
    LoggingPlugin,
)
from google.adk.plugins.reflect_retry_tool_plugin import (
    ReflectAndRetryToolPlugin,
)

from google.genai import types


# Load environment variables from the .env file (if present)
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
try:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    print("✅ API key setup complete.")
except KeyError:
    raise KeyError("GOOGLE_API_KEY not found in environment variables.")

# Clean up any previous logs
for log_file in ["logger.log", "web.log", "tunnel.log"]:
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"🧹 Cleaned up {log_file}")

# Configure logging with DEBUG log level.
logging.basicConfig(
    filename="logger.log",
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

print("✅ Logging configured")


## AGENT SETUP ##

APP_NAME = "default"  # Application
USER_ID = "default"  # User
SESSION = "default"  # Session
MODEL_NAME = "gemini-2.5-flash-lite"

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

# MCP integration
mcp_pubmed_server = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",  # Run MCP server via npx
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@cyanheads/pubmed-mcp-server",
            ],
            env={
                "NBCBI_API_KEY": os.getenv("NBCBI_API_KEY", "")
            }
        ),
        timeout=30,

    )
)

# Pubmed Search Agent
pubmed_search_agent = LlmAgent(
    name="pubmed_search_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    description="Searches for information using Pubmed",
    instruction="""Return a list of relevant research paper PMIDs based on the user's query. Focus on finding papers that directly address the user's topic. Focus on papers that are recent and highly cited. Return only the PMIDs in a comma-separated format.""",
    tools=[mcp_pubmed_server],
    # output_key="pmids"
)

# Summarize Agent
summarize_agent = LlmAgent(
    name="summarize_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    description="Summarizes research papers",
    instruction="""Use the provided PMIDs to fetch the full text of each research paper from Pubmed. Summarize the key findings of each paper in a concise manner. Ensure that each summary includes a proper citation with a link to the original article.""",
    tools=[mcp_pubmed_server],
    # output_key="summaries"
)


root_agent = LlmAgent(
    name="research_paper_finder_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction=""" You are an expert research assistant. Your task is to find research papers and summarize them. Your audience is a professional working in science communications seeking evidence-based information.
    You MUST ALWAYS follow these steps:
    1) Find research papers on the user provided topic using the 'pubmed_search_agent'. 
    2) Then, pass the papers to 'summarize_agent' tool to summarize the papers.
    3) Check that summaries include a citation with a link to the article. If not, go back to step 2 and ask the summarize_agent to include citations with links.
    4) Finally, provide a comprehensive response to the user that includes the summaries and citations
    Make sure to ALWAYS use the tools provided to you. NEVER make up information or citations.
    """,
    tools=[AgentTool(agent=pubmed_search_agent), AgentTool(agent=summarize_agent)]
)



# SQLite database will be created automatically
db_url = "sqlite:///my_agent_data.db"  # Local SQLite file
session_service = DatabaseSessionService(db_url=db_url)

# Create a new runner with persistent storage
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME, 
    session_service=session_service,
    plugins=[
        LoggingPlugin(), # Add the plugin. Handles standard Observability logging across ALL agents
        ReflectAndRetryToolPlugin(),
    ],
)

QUERY = "How is metformin related to diabetes control?"
# QUERY = "How does hormone replacement therapy, including both testosterone and estrogen, effect your A1C?"
# QUERY = "What are the main causes of acute respiratory distress syndrome?"
# QUERY = "I want to learn about stage 4 prostate cancer. What can cause it?"
# QUERY = "Yes. What's the best treatment for stage 4 prostate cancer?"
# QUERY = "Can you tell me more about genomically targeted therapies"


async def main():
    response = await runner.run_debug(QUERY, verbose=True)

asyncio.run(main())