A, B, C, K = map(int, input().split())
T = 0
if A >= K:
    T += K
if A < K:
    if B >= K - A:
        T += A
    if B < K - A:
        T += 2*A + B - K
print(T)