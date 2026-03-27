# 23/08/2025 Daily Challenge

# Given an integer, determine if that number is a prime number or a negative prime number.

# A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.

# A negative prime number is the negative version of a positive prime number.

# 1 and 0 are not considered prime numbers.

def is_unnatural_prime(number:int) -> bool:

    # When number is 0 or 1 return false:

    if number == 0 or abs(number) == 1:
        return False

    # When the number is negative:

    elif number < 0:
        for i in range(2,abs(number)):
            if abs(number) % i == 0:
                result = False
                break
            else:
                result = True
        return(result)

    # When the number is positive:

    else:
        for i in range(2,number):
            if number % i == 0:
                result = False
                break
            else:
                result = True
        return(result)
        
is_unnatural_prime(99)