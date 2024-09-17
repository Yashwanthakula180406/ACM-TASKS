# Number of natural numbers
n = 100

# Calculate the sum of the squares
sum_squares = sum(i**2 for i in range(1, n+1))

# Calculate the square of the sum
sum_numbers = sum(range(1, n+1))
square_sum = sum_numbers**2

# Calculate the difference
difference = square_sum - sum_squares

print("The difference is", difference)
