s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.split(" ")
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
d = {}
for i in range(20):
    if (i+1) in num:
        d[s[i][:1]] = i + 1
    else:
        d[s[i][:2]] = i + 1
print(d)