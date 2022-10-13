for b in range (1, 100//10+1):
    for k in range(1, 100//5+1):
        t = 100-b-k
        if b*10+k*5+t*0.5 == 100:
            print("быки:", b, "коровы:", k, "телята:", t);
