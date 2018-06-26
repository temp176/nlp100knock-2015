with open("hightemp.txt") as f:
    for i in f:
        print(i.replace('\t',' '),end = '')
