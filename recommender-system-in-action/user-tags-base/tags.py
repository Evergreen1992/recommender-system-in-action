#coding=utf-8
#records[i] = [user, item, tag]
def InitStat(records):
    user_tags = dict()
    tag_items = dict()
    user_items = dict()
    for user, item, tag in records.items():
        addValueToMat(user_tags, user, tag, 1)
        addValueToMat(tag_items, tag, item, 1)
        addValueToMat(user_items, user, item, 1)
#物品标签数据余弦相似度
def CosineSim(item_tags, i, j):
    ret = 0
    for b , wib in item_tags[i].items():
        if b in item_tags[j]:
            ret += wib * item_tags[j][b]
    ni = 0
    nj = 0
    for b, w in item_tags[i].items():
        ni += w * w
    for b, w in item_tags[j].items():
        nj += w * w
    if ret == 0 :
        return 0
    return ret / math.sqrt(ni * nj)
#基于用户标签的推荐算法
def Recommend(user):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag, wut in user_tags[user].items():#遍历用户打过的标签
        for item, wti in tag_items[tag].items:#遍历被tag标记过的物品
            if item in tagged_items:
                continue
            if item not in recommend_items:
                recommend_items[item] = wut * wti#用户打过标签tag的次数   乘以   物品被标签tag标记过的次数
            else:
                recommend_items[item] += wut * wti
    return recommend_items