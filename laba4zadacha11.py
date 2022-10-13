def guests_seating( n, dis ):
    lis = list( range(1, n + 1) )
    bad_pairs = set()
    for e in dis:
        L, de, R = e.partition('-')
        not_frends = set( int(x) for x in R.split(',') )
        for nf in not_frends:
            bad_pairs.add( frozenset( [int(L), nf] ) )
    res = [ [x] for x in lis ]
    flag = True
    while flag:
        flag = False
        for x in res:
            for y in lis:
                if frozenset([x[-1],y]) not in bad_pairs and y not in x:
                    x.append(y)
                    flag = True
                    if len(x) == n:
                        #return x
                        return True
    return False
n = 10
dis = '1-2,4,6,8 3-5,7,9 4-1,2,3 5-2,4 6-3'.split()
print( guests_seating( n, dis ) )
