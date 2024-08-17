#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import (
    PorterStemmer,
    LancasterStemmer,
    SnowballStemmer,
    RegexpStemmer
)
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.cistem import Cistem


# In[2]:


def basic_downloads():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')


# In[3]:


stop_words = set(stopwords.words('english'))
lemmatizer = wnl = WordNetLemmatizer()
# Initialize the stemmers
ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer("english")
rs = RegexpStemmer('ing$|s$|e$', min=4) # Fixed the syntax error in RegexpStemmer
wordnet_map={"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ  # adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # verb
    elif tag.startswith('N'):
        return wordnet.NOUN  # noun
    elif tag.startswith('R'):
        return wordnet.ADV  # adverb
    else:
        return wordnet.NOUN  # default to noun


# In[4]:


def remove_stopwords(text):
    tokens = text.split()
    filtered_words = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_words)


# In[5]:


def clean_text(text):
    text = "".join([word for word in text if word not in punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords.words('english')]  # Use stopwords.words('english') directly
    return text


# In[6]:


def stem_words(text):
    if pd.isnull(text):  # check if tweet is NaN
        return np.nan
    return ' '.join([ps.stem(word) for word in text.split()])
# Define stemming functions for each stemmer
def tokenized_text(text):
    return nltk.word_tokenize(text)
def porter_stemming(tokenized_text):
    return [ps.stem(word) for word in tokenized_text]

def lancaster_stemming(tokenized_text):
    return [ls.stem(word) for word in tokenized_text]

def snowball_stemming(tokenized_text):
    return [ss.stem(word) for word in tokenized_text]

def regexp_stemming(tokenized_text):
    return [rs.stem(word) for word in tokenized_text]

# Define lemmatization function using WordNetLemmatizer
def wordnet_lemmatizing(tokenized_text):
    return [lemmatizer.lemmatize(word) for word in tokenized_text]


# In[7]:


def perform_lemmatization_with_pos(text):
    tokens = nltk.word_tokenize(text)  # Tokenize the tweet
    pos_tags = nltk.pos_tag(tokens)  # Get POS tags for each token
    lemmatized_words = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]
    return ' '.join(lemmatized_words)


# In[8]:


def word_pos_tag(text):
    # Tokenize the text
    tokens = re.split('\W+', text)
    # Remove stopwords
    text = [word for word in tokens if word not in stopwords.words('english')]
    # Lemmatize the text
    text_lemmatized = [wnl.lemmatize(word) for word in text]
    # Perform POS tagging
    pos_tags = nltk.pos_tag(text_lemmatized)
    return pos_tags 
    # return text  # This line is unreachable and can be removed

