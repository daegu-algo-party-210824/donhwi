import sys

input = sys.stdin.readline

m = int(input())

S = [False] * 21

for _ in range(m):
    cal = input().rstrip()

    if cal == "all":
        for i in range(1, 21):
            S[i] = True
    elif cal == "empty":
        for i in range(1, 21):
            S[i] = False
    else:
        cal, x = cal.split()
        x = int(x)
        if cal == "add":
            S[x] = True
        elif cal == "remove":
            S[x] = False
        elif cal == "check":
            if S[x]:
                print(1)
            else:
                print(0)
        elif cal == "toggle":
            if S[x]:
                S[x] = False
            else:
                S[x] = True
