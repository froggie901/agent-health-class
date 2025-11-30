import requests as re 
from bs4 import BeautifulSoup as bs
import pandas as pd
import os


## get some article data from PubMed Central (PMC)
paper_article="https://pmc.ncbi.nlm.nih.gov/articles/PMC8248927/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

page = re.get(paper_article, headers=headers)
print(page.status_code)


## save the text of the article as soup, article_text is the text of the article
soup = bs(page.text, 'html.parser')
article_text = soup.get_text()
print(article_text[0:500])  # print first 500 characters of the article text


# with open("PMC8248927-article.txt", "w") as f:
#     f.write(article_text.)




# import os
# from google.adk.tools import ToolContext # Optional, but good practice

# def summarize_local_document(article_text: str, context: ToolContext) -> str:
#     """
#     Takes in text of an article and summarizes it using Gemini LLM.
#     """
#     from google.adk.models.google_llm import Gemini
#     from google.genai import types
#     from dotenv import load_dotenv
#     import os

#     # Load environment variables from the .env file (if present)
#     load_dotenv()

#     # The client gets the API key from the environment variable `GEMINI_API_KEY`.
#     try:
#         GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#         print("✅ API key setup complete.")
    
#     except KeyError:
#         raise KeyError("GOOGLE_API_KEY not found in environment variables.")

#     # Initialize the Gemini model
#     model = Gemini(model="gemini-2.5-flash-lite")

#     # Create the prompt for summarization
#     prompt = f"Please summarize the following article text:\n\n{article_text}\n\nSummary:"

#     # Generate the summary using the model
#     response = model.generate(
#         inputs=[types.Content(role="user", parts=[types.Part(text=prompt)])]
#     )

#     # Extract and return the summary text
#     summary = response[0].parts[0].text
#     return summary    



