a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print( sum(v for i,v in enumerate(a) if not i%2) - sum(v for i,v in enumerate(a) if i%2))
