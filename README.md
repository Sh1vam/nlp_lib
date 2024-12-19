# nlp_lib
## For Custome Text Pre-processing during NLP Task

- download repo and extract it 
- got to nlp_lib-master directory run command prompt
> type : pip install .

 >> python -m spacy download en_core_web_sm # for language corpus of english language
 >> python -m spacy download en_core_web_md
 >> nlp=spacy.load("en_core_web_md") # for using a.similarity(b) function

Use :

* from nlp_lib import *
* df = pd.read_csv("mycsv.csv") # let columns be col1,col2,col3 ... coln
* df['rm_punct'] = df['col1'].apply(remove_punctuations) 

___**Note :- when you imoport this library as shown it will import pandas as pd and numpy as np aditionaly re,string,nltk and spacy can also be use without importing statements.**___
