X = int(input())
A = 100
i = 1
while True:
    A = int(A*1.01)
    if A >= X:
        print(i)
        break
    else:
        i += 1