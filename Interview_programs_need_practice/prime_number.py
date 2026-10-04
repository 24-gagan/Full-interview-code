lst = [2, 3, 4, 5, 6, 7]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # it will go till square root of n
        if n % i == 0:
            return False
    return True


# List ke primes print karna
primes = [num for num in lst if is_prime(num)]
print("Prime numbers in the list:", primes)
