# LDA_Merge
LDA method get the topic of each content \
回推文章屬於第幾群，因為群數選擇困難，覺得某兩群都很好，那就merge data吧！ \
因為研究時，覺得LDA分群分成22、23群都很好，想著重看22群的2, 3, 5群以及23群的2, 4, 5群才想出能不能看同時屬於這些兩個`num_of_topics`的文章。 

# 前言
LDA的教學很多，這裡就不重複贅述了 \
`sampledata`是來自台灣國立清華大學陳素燕教授實驗室爬文美國華盛頓時報(或什麼東西我忘記了)，原資料為`washington.june`，為做示範將原資料切分取前30筆(原先高達40000多) \
重點是merge的想法&過程 

# 說明
`num_topics`指的是LDA分群的群數，最終決定應該要以`Perplexity`和`Coherence Score`或是視覺化呈現來決定 \
`group`指的是在`num_topics`裡面的第幾群 \
`lda_model.get_document_topics(corpus)`是取得文章屬於哪個`group`的機率值 \
最後將欲比較的`data`存成json再去比較是否相同而已，即可取得交集文章

# Notice
1. 注意資料格式，`sampledata`的格式是已經轉過的`[[sampledata.json]]`，要放進LDA要確定格式
2. 注意`num_topics`和`group`的意思 
3. 記得`Python`語言起始是0，`LDA`起始則是1
