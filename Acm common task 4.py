def prime(num):
    #it removes numbers less than or equal to 1 basically takes only 2 or 3
    # checking divisibility by numbers of the form 6k+or-1
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    #it counts one by one and finds till the n number is reached
    count = 0
    num = 1
    while count < n:
        num += 1
        if prime(num):
            count += 1
    return num

# Find the 10,001st prime number
result = nth_prime(10001)
print(result)
