#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string 
import re


# In[2]:


def remove_punctuations(text):
  text = text.translate(str.maketrans('', '', string.punctuation))
  return text.strip()


# In[3]:


def removes_specials(text):
  tmp=text
  pattern = re.compile(r'[A-Za-z0-9\s]')
  specials = re.sub(pattern, "", tmp)
  return text.translate(str.maketrans('', '', specials)).strip()


# In[4]:


def removes_non_printables(text):
  tmp=text
  specials = tmp.translate(str.maketrans('', '', string.printable)).strip()
  return text.translate(str.maketrans('', '', specials)).strip()


# In[5]:


def remove_whitespace(text):
  text = text.translate(str.maketrans('', '', string.whitespace))
  return text.strip()


# In[6]:


def remove_hexdigits(text):
  text = text.translate(str.maketrans('', '', string.hexdigits))
  return text.strip()


# In[7]:


def remove_octdigits(text):
  text = text.translate(str.maketrans('', '', string.octdigits))
  return text.strip()


# In[8]:


def remove_html_tags(text):
    reg=re.compile(r"<[^>]*>")
    return re.sub(reg,"",text)


# In[9]:


def remove_url(text):
  url_pattern = re.compile(r"(http?|ftp|https?|file)://\S+ ")
  return re.sub(url_pattern, "", text)


# In[10]:


'''use on df by df[].apply(function_name)
remove_punctuations
remove_url
remove_html_tags
removes_specials'''

