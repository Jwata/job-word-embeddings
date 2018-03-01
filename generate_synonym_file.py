from gensim.models.word2vec import Word2Vec
import pandas as pd

import MeCab
tagger = MeCab.Tagger("-F %f[6]\\s")

def tokenize(text):
    return tagger.parse(text).strip(" EOS\n")

model = Word2Vec.load('job_word_embeddings.model')

with open('data/synonym.txt', 'w') as f:
    for word in model.wv.index2word:
        similar_words = [tokenize(word)]
        for w, _ in model.most_similar(word, topn=5):
            tokenized = tokenize(w)
            if tokenized:
                similar_words.append(tokenized)
        line = '{}=>{}\n'.format(word, ','.join(similar_words))
        f.write(line)
