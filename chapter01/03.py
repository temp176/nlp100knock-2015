str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.split(" ")
for i in range(len(str)):
    if str[i].find(",") != -1 or str[i].find(".") != -1:
        str[i] = str[i][:-1]
    print(len(str[i]))