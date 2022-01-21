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
docs = [json.loads(line) for line in open('sampledata.json', encoding='utf-8')]

# 笑死人的部分
docs = docs[0]

mydata = []
# 取出全部的內文
for doc in docs:
    # 笑死人的部分part 2
    doc = doc[0]
    text = doc['content']
    #print(text)
    mydata.append([text])

# 移除停用詞
# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
# 停用詞增加示範
stop_words.extend(['from', 'also', 'could', 'would'])
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
                                            #分幾群，要比較要改這裡
                                           num_topics=5, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)


# 取得文章為第幾群的方法get_document_topics
my_dict = []
for i in range(30):
    #print(lda_model.get_document_topics(corpus[i]))
    t = lda_model.get_document_topics(corpus[i])
    # 取機率大的
    group, score= max(t, key=lambda item: item[1])
    print('Score = ', score, "Group = ", group)
    # 看屬於哪群，要比較要改這裡
    if group == 1:
        my_dict.append(docs[i])

# 存檔(可跳過)
with open('num_topics5_group1.json', 'w',  encoding='utf-8') as fp:
    json.dump(my_dict, fp, ensure_ascii=False)

