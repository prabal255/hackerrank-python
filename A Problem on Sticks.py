###  A Problem on Sticks

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l = set(l)
    if 0 in l:
        print(len(l)-1)
    else:print(len(l))
