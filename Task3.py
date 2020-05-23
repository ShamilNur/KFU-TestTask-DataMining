def ReadFile(filename='users.txt'):
    f = open(filename)
    info = dict()
    for line in f:
        l = line.split(';')
        user = l[0]
        post = l[1]
        rate = int(l[2])
        print(str(user) + ' ' + str(post) + ' ' + str(rate))
        if not user in info:
            info[user] = dict()
        info[user][post] = rate
    f.close()
    return info


def distCosine(vecA, vecB):
    dotProduct = 0.0  # скалярное произведение vecA и vecB
    dotSquareA = 0.0  # скалярный квадрат (квадрат длины) вектора A
    dotSquareB = 0.0  # скалярный квадрат вектора B
    for dim in vecA:
        dotSquareA += vecA[dim] * vecA[dim]
        if dim in vecB:
            dotProduct += vecA[dim] * vecB[dim]
    for dim in vecB:
        dotSquareB += vecB[dim] * vecB[dim]
    return dotProduct / math.sqrt(dotSquareA * dotSquareB)


import math


def get_recommendations(userID, nBestUsers, nBestPosts):
    userRates = ReadFile()
    matches = [(u, distCosine(userRates[userID], userRates[u])) for u in userRates if u != userID]
    topMatches = sorted(matches, key=lambda x: x[1], reverse=True)[:nBestUsers]
    print("Самые подходящие пользователи по вкусам для %s:" % userID)
    for line in topMatches:
        print("%6s distCosine: %.3f" % (line[0], line[1]))
    similarity = dict()
    similarity_all = sum([x[1] for x in topMatches])
    topMatches = dict([x for x in topMatches if x[1] > 0.0])
    for relatedUser in topMatches:
        for post in userRates[relatedUser]:
            if not post in userRates[userID]:
                if not post in similarity:
                    similarity[post] = 0.0
                similarity[post] += userRates[relatedUser][post] * topMatches[relatedUser]
                similarity[post] /= similarity_all
    bestPosts = sorted(similarity.items(), key=lambda x: x[1], reverse=True)[:nBestPosts]
    print("\nРекомендации:")
    for postInfo in bestPosts:
        print("%7s  Коэф. корел.: %6.4f" % (postInfo[0], postInfo[1]))
    return [(x[0], x[1]) for x in bestPosts]


get_recommendations('PRD0900725', 2, 5)