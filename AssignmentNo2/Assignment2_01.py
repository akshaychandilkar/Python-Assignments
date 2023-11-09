import arithmetic

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Addition:", arithmetic.Add(a, b))
    print("Subtraction:", arithmetic.Sub(a, b))
    print("Multiplication:", arithmetic.Mult(a, b))
    print("Division:", arithmetic.Div(a, b))

if __name__ == "__main__":
    main()                