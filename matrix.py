A = [[int(input("Enter A[0][0]: ")), int(input("Enter A[0][1]: "))],
     [int(input("Enter A[1][0]: ")), int(input("Enter A[1][1]: "))]]

B = [[int(input("Enter B[0][0]: ")), int(input("Enter B[0][1]: "))],
     [int(input("Enter B[1][0]: ")), int(input("Enter B[1][1]: "))]]

addition = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
subtraction = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]

print("Addition:")
for row in addition:
    print(row)

print("Subtraction:")
for row in subtraction:
    print(row)
