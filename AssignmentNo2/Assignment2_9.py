
def count_digits(number):
    return len(str(number))

user_input = int(input("Enter a number: "))
digits_count = count_digits(user_input)
print("NUmber of digits:", digits_count)
