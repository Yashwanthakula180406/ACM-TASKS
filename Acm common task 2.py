def sum_even_fibonacci(n):

    a, b = 0, 1
    sum = 0
    
    # Generate Fibonacci numbers and sum the even ones
    for i in range(n):
        if b > n:
            break
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    
    return sum


n = 4000000

# Calculate the sum of even Fibonacci numbers
result = sum_even_fibonacci(n)
print(result)
