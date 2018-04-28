import random

def Typoglycemia(s):
    result = ""
    s = s.split(" ")
    for i in range(0,len(s)):
        if len(s[i]) > 4:
            s[i] = s[i][0] + "".join(random.sample(s[i][1:-1], len(s[i][1:-1]))) + s[i][-1]
        
    for i in range(0,len(s)):
        if i != len(s):
            result += (s[i] + " ")
        else:
            result += s[i]

    return result

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(s)
print(Typoglycemia(s))