with open('file.name') as t:
    print( * (sum(map(int, line.split())) for line in t.readlines()), sep = '\n')
