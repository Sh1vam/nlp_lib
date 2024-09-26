# nlp_lib
## For Custome Text Pre-processing during NLP Task

Use :

* from nlp_lib import *
* df = pd.read_csv("mycsv.csv") # let columns be col1,col2,col3 ... coln
* df['rm_punct'] = df['col1'].apply(remove_punctuations) 
