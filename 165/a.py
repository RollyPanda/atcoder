K = int(input())
A, B = map(int, (input().split()))
lst = []
for i in range(A, B+1):
    if i % K == 0:
        result = "OK"
        lst.append(result)
        break
    else:
        result = "NG"
        lst.append(result)
print(lst[-1])