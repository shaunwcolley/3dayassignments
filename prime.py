num = int(input("Provide a number to see if it is prime: "))

def is_prime(n):
    if n == 0:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    half = n - int(n / 2) + 1
    divisor = 2
    while divisor <= half:
        if n % divisor == 0:
            return False
        divisor += 1
    else:
        return True
if is_prime(num) == True:
    print("You have a prime!")
elif is_prime(num) == False:
    print("Sorry not a prime")
