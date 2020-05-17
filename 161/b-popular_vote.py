n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
total = sum(a)

print("No" if a[m - 1] < 1/(4*m) * total else "Yes")