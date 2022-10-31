n = int(input())
A = set()
for i in range(n):
    S = input().split()
    for elem in S:
        A.add(elem)
print(len(A))
