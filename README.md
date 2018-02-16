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
