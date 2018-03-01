import re
import unicodedata

import MeCab
import pandas as pd
from gensim.models import word2vec

job_postings = pd.read_csv('./data/job_postings.csv')

def normalize_job_title(title):
    title = unicodedata.normalize('NFKC', title)
    title = re.sub(r'【.*】', '', title)
    title = re.sub(r'\[.*\]', '', title)
    title = re.sub(r'「.*」', '', title)
    title = re.sub(r'\(.*\)', '', title)
    title = re.sub(r'\<.*\>', '', title)
    title = re.sub(r'[※@◎].*$', '', title)
    return title.lower()

tagger = MeCab.Tagger("-U %m,未知語\\t -F %f[0],%f[6]\\t  -d  /usr/local/opt/mecab-ipadic-neologd")

def extract_nouns(text): 
    words = []
    for row in tagger.parse(text).split('\t'):
        if row.strip() == 'EOS':
            continue
        t = row.split(',')[0]
        w = row.split(',')[1]
        if t == '名詞':
            words.append(w.strip().lower())
    return words

def convert_job_posting(job):
    converted = []

    title_and_requirements  = [normalize_job_title(job['job_title'])] + extract_nouns(job['requirements'])
    converted.append(title_and_requirements)

    summary = extract_nouns(job['summary'])
    converted.append(summary)

    return converted

inputs = []
for _, p in job_postings.iterrows():
    inputs += convert_job_posting(p)

word2vec_model = word2vec.Word2Vec(inputs, size=100, min_count=5, window=10, sg=1) # train with CBOW algorithm 
word2vec_model.save('job_word_embeddings.model')
