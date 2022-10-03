b=10
k=20
t=200
for b in range(0,11):
    for k in range(0,21):
        for t in range(0,201):
            if(10*b+5*k+0.5*t==100) and (b+k+t==100):
                print(b,k,t)
