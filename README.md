# Job word embeddings
This project builds word embeddings from job postings using [Gensim's word2vec API](https://radimrehurek.com/gensim/models/word2vec.html). check [this notebook](./Job%20word%20embeddings.ipynb) for more details.

## Setup
### Install miniconda
When you preapre isolated python environment for each project (especially machine learning project),
[Conda](https://conda.io/docs/) is commonly used as a paackage management system.  
In this project we will use [Minicoda](https://conda.io/miniconda.html), a minimum version of conda.  

You can install Miniconda with `brew cask`.

```
brew cask install miniconda
```

You may need to setup PATH.

```
echo 'export PATH=/usr/local/miniconda3/bin:"$PATH"' >> ~/.zshrc
```

and theh, check if it's installed properly

```
conda --version
```

### Create a python environment
Clone this repostiroy to your computer and move to the project directory

```
conda create --name job-posting-embeddings python=3.6
source activate job-posting-embeddings
pip install -r requirements.txt
```

### Install other dependencies
Install Japanese tokenizer and dictionary

```
brew install mecab mecab-ipadic

git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -a
```

check if it tokenize proper nouns

```
echo "SMAPの中居正広" | mecab -U %m -F "%f[6]\s" -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
=> SMAP の 中居正広 EOS
```

## Open notebook
```
jupyter notebook Job\ word\ embeddings.ipynb

```