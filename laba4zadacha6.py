def main(l):
    print(*(i for i in l if i[-1] == '0'))
lst = input().split()
main(lst)
