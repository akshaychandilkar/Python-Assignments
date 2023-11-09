
def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
def main():
    num1 = int(input("Enter a number: "))
    result1 = check_number(num1)
    print(result1)

    num2 = int(input("Enter a Number: "))
    result2 = check_number(num2)
    print(result2)

    num3 = int(input("Enter a number: "))
    result3 = check_number(num3)
    print(result3)

if __name__ == "__main__":
    main()
    





    