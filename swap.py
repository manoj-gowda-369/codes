def fibonacci(n):
    series = [0, 1]
    for _ in range(n - 2):
        series.append(series[-1] + series[-2])
    return series[:n]

num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(num)
    print("Fibonacci Series:")
    for i in result:
        print(i, end=' ')
    print("\nProgram by Manoj 🚀")

