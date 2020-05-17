N,M = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
print(max(-1,N-s))