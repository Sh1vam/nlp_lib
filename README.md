# nlp_lib
## For Custome Text Pre-processing during NLP Task
> python -m spacy download en_core_web_sm
- got to nlp_lib-master directory run command prompt
> type : pip install . 
Use :

* from nlp_lib import *
* df = pd.read_csv("mycsv.csv") # let columns be col1,col2,col3 ... coln
* df['rm_punct'] = df['col1'].apply(remove_punctuations) 
