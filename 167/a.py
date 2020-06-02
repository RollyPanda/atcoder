S = input()
T = input()
print("Yes" if T[:-1]==S and len(T)-1==len(S) else "No")