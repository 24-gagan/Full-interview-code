lst = [2, 3, 4, 5, 6, 7, 11]

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
primes=[num for num in lst if is_prime(num)]
primes.sort(reverse=True)
print("Prime number in descending order", primes)