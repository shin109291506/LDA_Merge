import json

# load資料，因為當時是22、23群再比較，這邊就懶得改變數名稱了
docs22 = [json.loads(line) for line in open('num_topics3_group1.json', encoding='utf-8')]
docs23 = [json.loads(line) for line in open('num_topics5_group1.json', encoding='utf-8')]

#print("Data22",len(docs22[0]))
#print("Data23",len(docs23[0]))

a = []

# 比較文章
for i in range(len(docs22[0])):
    for j in range(len(docs23[0])):
        if docs22[0][i] == docs23[0][j]:
            #print(docs22[0][i])
            a.append(docs22[0][i])

print(a)


