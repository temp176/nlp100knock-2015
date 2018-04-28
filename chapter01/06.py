def getCharNGram(n,s):
    wordX = s.split(" ")
    charX = ''.join(wordX)
    charGram = [''.join(charX[i:i+n]) for i in range(len(charX)-n+1)]

    return charGram


X = set(getCharNGram(2,"paraparaparadise"))
Y = set(getCharNGram(2,"paragraph"))
print('X =',X)
print('Y =',Y)
print("和集合：",X.union(Y))
print("積集合：",X.intersection(Y))
print("差集合(X - Y)：",X.difference(Y))
print("差集合(Y - X)：",Y.difference(X))
print("Xにseは含まれるか：","se" in X)
print("Yにseは含まれるか：","se" in Y)