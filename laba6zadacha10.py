states = {}
 
for _ in range(int(input())):
    state, *cities = input().split()
    for city in cities:
        states[city] = state
 
print(*(states[input()] for _ in range(int(input()))), sep="\n")
