# Setup environment
## Install miniconda
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

## Create environment
```
conda create --name job-posting-embeddings python=3.6
source activate job-posting-embeddings
pip install -r requirements.txt
```

## Install other dependencies
Install Japanese tokenizer and dictionary

```
brew install mecab mecab-ipadic

git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -a

# check if it's installed properly
echo "10日放送の「中居正広のミになる図書館」（テレビ朝日系）で、SMAPの中居正広が、篠原信一の過去の勘違いを明かす一幕があった。" | mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
```
