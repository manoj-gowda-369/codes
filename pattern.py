def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

# Call the function with the number of rows
n = 5  # You can change this value to adjust the height of the pyramid
print_pyramid(n)

