def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5+1)):
            if n%i == 0:
                return False
                break
        return True
    
print(is_prime(3))
print(is_prime('a'))
print(is_prime.__annotations__)
