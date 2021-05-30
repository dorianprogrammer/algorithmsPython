X = [
    [12, 7, 2],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [5, 8, 1, 2],
    [6, 7, 0, 3],
    [4, 5, 9, 1]
]

result = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
print("Matrix 1: [3x3]")
for r in X:
    print(r)
print("Matrix 2: [3x4]")
for r in Y:
    print(r)
print("Matrix Multiplication: [3x4]")
for r in result:
    print(r)
