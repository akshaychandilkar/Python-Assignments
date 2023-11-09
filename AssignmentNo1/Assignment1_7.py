
def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False
    
Value_1 = int(input("Enter the first number: "))
Value_2 = int(input("Enter the second number: "))

result_1 = is_divisible_by_5(Value_1)
result_2 = is_divisible_by_5(Value_2)

print(f"{Value_1} is {'True' if result_1 else 'False'} and {Value_2} is {'True' if result_2 else 'False'}")







