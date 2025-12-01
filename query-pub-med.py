## https://ua-libraries-research-data-services.github.io/UALIB_ScholarlyAPI_Cookbook/src/python/pubmed.html 
## https://www.ncbi.nlm.nih.gov/home/develop/api/
 


import requests as re
from time import sleep
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3 as sql
import pandas as pd

retmax = 10
term = "what are the main risk factors for acute respiratory distress syndrome"

def pubmed_query(term, retmax=retmax):
    ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    base_params = {
            'db': 'pubmed',
            'term': term + ' free full text[sb] AND review[pt]',
            'retmode': 'json',
            'retmax': retmax,
            'sort': 'pub date'
        }
    
    response = re.get(ESEARCH_URL, params=base_params)
    response.raise_for_status()  # Raise an error for bad responses
    base_data = response.json()
    base_data_pmids = base_data['esearchresult']['idlist']
    base_data_pmids_dict = {'PMID': base_data_pmids}

    return base_data_pmids_dict






# pubmed_data = pubmed_query(term, retmax=20)
# pprint(pubmed_data)
# pprint((len(pubmed_data)))
# pprint(type(pubmed_data))
# pprint(pubmed_data.keys())
# base_data_pmids = pubmed_data['esearchresult']['idlist']
# base_data_pmids_dict = {'PMID': base_data_pmids}



# df = pd.DataFrame(pubmed_data['esearchresult']['idlist'], columns=['PMID'])
# df.head()

# def pubmed_query(term, retmax=retmax):
#     ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

#     def base_query (term, retmax=retmax):

    
#         base_params = {
#             'db': 'pubmed',
#             'term': term + ' free full text[sb] NOT review[pt]',
#             'retmode': 'json',
#             'retmax': retmax,
#             'sort': 'pub date'
#         }
#         response = re.get(ESEARCH_URL, params=base_params)
#         response.raise_for_status()  # Raise an error for bad responses
#         base_data = response.json()

#         base_data_df = pd.DataFrame(base_data['esearchresult']['idlist'], columns=['PMID'])
#         print(f"Base Articles DataFrame:")
#         print(base_data_df)


#     review_params = {
#         'db': 'pubmed',
#         'term': term + 'AND  free full text[sb] AND review[pt]',
#         'retmode': 'json',
#         'retmax': 5,
#         'sort': 'pub date'
#     }

#     response = re.get(ESEARCH_URL, params=review_params)
#     response.raise_for_status()  # Raise an error for bad responses
#     review_data = response.json()
    



#     return base_data, review_data



# query_string = "what are the main causes of acute respiratory distress syndrome?"
# pubmed_data = pubmed_query(query_string, retmax=20)

# for base, review in pubmed_data:
#     print("\nBase Articles PMIDs:")
#     pprint(base, depth=3)
#     print("\n Results:")
#     pprint(base.keys())
#     # base_pmids = base['esearchresult']['idlist']
#     # print(base_pmids)

#     print("\nReview Articles PMIDs:")
#     pprint(review, depth=3)
#     # review_pmids = review['esearchresult']['idlist']
#     # print(review_pmids)   



# pmids = pubmed_data['esearchresult']['idlist']
# print(f"Found PMIDs: {pmids}")

