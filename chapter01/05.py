def getNGram(n,s):
    wordX = s.split(" ")
    charX = ''.join(wordX)
    wordGram = ['-'.join(wordX[i:i+n]) for i in range(len(wordX)-n+1)]
    charGram = ['-'.join(charX[i:i+n]) for i in range(len(charX)-n+1)]

    print('word gram:',wordGram)
    print('character gram:',charGram)

getNGram(2,"I am an NLPer")