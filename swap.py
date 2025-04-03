def fibonacci(n):
    series = [0, 1]
    for _ in range(n - 2):
        series.append(series[-1] + series[-2])
    return series[:n]

num = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci(num))
