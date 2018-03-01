import sys
import math

from elasticsearch import Elasticsearch
import pandas as pd

index = sys.argv[1]

job_postings = pd.read_csv('./data/job_postings.csv')

es = Elasticsearch()

for _, job_posting in job_postings.iterrows():
    doc = job_posting.dropna().to_dict()
    es.index(index=index, doc_type='_doc', body=doc)
