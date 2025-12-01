# agent-sofia
| Creating agents for better health care understanding.

By: 
- [Susan Kraemer, PhD](https://www.linkedin.com/in/susankraemer/)
- [Cameron Guthrie](https://www.linkedin.com/in/cameron-guthrie-8340032a/)
- [Patrick Cavins, PhD](https://www.linkedin.com/in/patrickcavins/)

## Background 

An agentic application can have multiple users and each user may have multiple sessions with the application. To manage these sessions and events, ADK offers a Session Manager and Runner. Created as part of the [5-Day AI Agents Intensive Course with Google](https://www.kaggle.com/learn-guide/5-day-agents)


**SessionService: The storage layer**

Manages creation, storage, and retrieval of session data
Different implementations for different needs (memory, database, cloud)

**Runner: The orchestration layer**

Manages the flow of information between user and agent
Automatically maintains conversation history
Handles the Context Engineering behind the scenes

## Project structure 
1. `capstone-project-with-mcp-server.ipynb`
- This is an end-to-end jupyter notebook that uses an MCP service with a single agent to answer medical queries
 - Example log, `demo_logs_from_query-script.txt` 

2. `multi-agent-and-custom-tool-script.py`
- This is python script which creates multiple agents. One agents uses the Pubmed MCP, and the other agent uses a custom tool called `get_dict_from_query` which return a structure python dictionary using the format {'PMID': list[int]}. Both agents are sub-agents inside of root_agent which coordinates their invocation.
 - Example log, `demo_logs_with_mcp_server.txt

3. `README.md`
- The explainer, hopefully. 

4. `b4-soup-edit` 
- **workin progress** python file for parsing a full text html publication 


## References 

**PUBMED MCP**
- [GITHUB](https://github.com/grll/pubmedmcp)
- [REDDIT](https://www.reddit.com/r/modelcontextprotocol/comments/1kuc03k/cyanheadspubmedmcpserver_an_mcp_server_enabling/)

**PUMBED CLIENT**
- [GITHUB](https://github.com/grll/pubmedclient)


### PUBMED API CLIENT IN PYTHON
- [University of Alabama, Library](https://ua-libraries-research-data-services.github.io/UALIB_ScholarlyAPI_Cookbook/src/python/pubmed.html)

#### Searching Based on Publication Types

We can sort by publication type by adding `AND` into the search:

```
term=<searchQuery>+AND+filter[filterType]
```

`[pt]` specifies that the filter type is publication type. More filters can be found at <a href="https://pubmed.ncbi.nlm.nih.gov/help/" target="_blank">PubMed Help</a>.