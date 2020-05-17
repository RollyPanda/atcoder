k = int(input())
a = (1 + k) * k // 2
three = (3+3*(k//3)) * (k // 3) // 2
five = (5+5*(k//5)) * (k // 5) // 2
fifteen = (15+15*(k//15)) * (k // 15) // 2
print(a-three-five+fifteen)