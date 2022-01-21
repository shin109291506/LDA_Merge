# load資料
import json

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
#from gensim.test.utils import common_corpus
from gensim import corpora, models

# 斷詞
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
#import pyLDAvis.gensim_models  #取代上面的 舊寫法
import matplotlib.pyplot as plt

# load資料
docs = [json.loads(line) for line in open('data.json', encoding='utf-8')]
# 笑死人的部分
docs = docs[0]

mydata = []
for doc in docs:
    #doc = docs[i]
    text = doc['content']
    #print(text)
    mydata.append([text])

#移除停用詞
# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'said', 'also', 'could', 'would'])
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

data_nostops = remove_stopwords(mydata)
#print(data_nostops)

# LDA
# Create Dictionary
id2word = corpora.Dictionary(data_nostops)
# Create Corpus
texts = data_nostops
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# Build LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                            #分幾群
                                           num_topics=5, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
# Visualize the topics
#pyLDAvis.enable_notebook()
#pyLDAvis.save_html() 用下面的程式代替
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word, mds='mmds')
pyLDAvis.save_html(vis, 'LDAvis.html')
