def cipher(s):
    cip = ''
    for i in range(0,len(s)):
        if s[i].islower():
            cip += chr(219 - ord(s[i]))
        else:
            cip += s[i]
    return cip

input = input('暗号化する文字列： ')
print('暗号化:' + cipher(input))
print('復号化:' + cipher(cipher(input)))