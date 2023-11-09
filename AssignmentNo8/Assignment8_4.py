def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def main():
    num = int(input("Enter a number: "))

    result = sum_of_digits(num)
    print("Sum of digits: ",result)

if __name__ == "__main__":
    main()