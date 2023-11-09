
def prime(number):
    if number <= 1:
        return False

    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False

    i = 5 
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False

        i += 6 
    return True

user_input = int(input("Enter a number: "))
if prime (user_input):
    print("It is a prime number")

else:
    print("It is not a prime number")
    
    