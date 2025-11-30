## https://ua-libraries-research-data-services.github.io/UALIB_ScholarlyAPI_Cookbook/src/python/pubmed.html 
## https://www.ncbi.nlm.nih.gov/home/develop/api/
# 
# Here we are creating an Observation input that the Large Language Model (LLM) will use to generate the final output. 

import requests as re
from time import sleep
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3 as sql
import pandas as pd




def pubmed_query(term, retmax=20):
    ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    
    base_params = {
        'db': 'pubmed',
        'term': term + ' free full text[sb] NOT review[pt]',
        'retmode': 'json',
        'retmax': retmax,
        'sort': 'pub date'
    }
    response = re.get(ESEARCH_URL, params=base_params)
    response.raise_for_status()  # Raise an error for bad responses
    base_data = response.json()
    pprint(base_data, depth=3)


    review_params = {
        'db': 'pubmed',
        'term': term + 'AND  free full text[sb] AND review[pt]',
        'retmode': 'json',
        'retmax': 5,
        'sort': 'pub date'
    }

    response = re.get(ESEARCH_URL, params=review_params)
    response.raise_for_status()  # Raise an error for
    review_data = response.json()
    pprint(review_data, depth=3)



    return 



query_string = "wnt signaling AND cancer"
pubmed_data = pubmed_query(query_string, retmax=20)

df = pd.DataFrame(pubmed_data['esearchresult']['idlist'], columns=['PubMed_ID'])
print(df.head())


