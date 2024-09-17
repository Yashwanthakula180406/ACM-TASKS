def large_prime_factor(n):
    
    largest_factor = None
    

    while n % 2 == 0:
        large_factor = 2
        n //= 2
    
    
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            large_factor = factor
            n //= factor
        factor += 2
    
    # If n becomes a prime number greater than 2
    if n > 2:
        large_factor = n
    
    return large_factor

# The number to factor
number =600851475143

# Find and print the largest prime factor
answer = large_prime_factor(number)
print(answer)
