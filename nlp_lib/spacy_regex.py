#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import spacy
from spacy import displacy


# In[4]:


nlp=spacy.load("en_core_web_sm")
options={'distance':110,"compact":True,"color":"black","bg":"white","font":"time"}


# In[5]:


def pos_tag(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags


# In[ ]:


def lower_case(body_text):
    # Call the pos_tag function to get the pos_tags for the current body_text
    pos_tags = pos_tag(body_text)
    return [(word.lower(), tag) for word, tag in pos_tags]


# In[6]:


def displacy_render(text):
    doc = nlp(text)
    try:
        displacy.render(doc, style="dep", jupyter=True, options=options)
    except :
        pass
    finally :
        print("use jupyter for this")
    return None

