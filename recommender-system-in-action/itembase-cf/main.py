#encoding=utf-8
#item based cf algorithm
def ItemSimilarity(train):
    C = dict()
    N = dict()
    for u , items in train.items():
        for i in users:
            N[i] += 1
            for j in users:
                if i == j:
                    continue
                c[i][j] += 1#同时喜欢物品i和物品j的人
    #calculate final similarity matrix
    W = dict()
    for i , related_items in C.items():
        for j , cij in related_items.items():
            W[u][v] = cij / math.sqrt(N[i] * N[j])
    return W

def Recommendation(train, user_id, W, K):
    rank = dict()
    ru = train[user_id]
    for i, pi in ru.items():
        for j, wj in sorted(W[i].items(),key=itemgetter(1),reverse=True)[0:k]:
            if j in ru:
                continue
            rank[j] += pi * wj
    return rank