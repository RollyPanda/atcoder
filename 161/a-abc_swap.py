a, b, c = map(int, input().split())

# a, b swap
a, b = b, a
# new_a, c swap
a, c = c, a

print(a, b, c)