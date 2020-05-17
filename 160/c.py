K, N = map(int, input().split())
A = list(map(int, input().split()))

distance = []
for i in range(1, N):
	distance.append(A[i] - A[i - 1])

distance.append(A[0] + K - A[-1])
most = max(distance)
output = K - most
print(output)