N = int(input())
A = list(map(int,input().split()))
T = {}
for i in A:
    if i not in T:
        T[i] = 0
    T[i] = T[i] + 1
for i in range(1, N+1):
    print(T.get(i, 0))