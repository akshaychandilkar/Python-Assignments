def main():
    multiply = lambda x, y: x * y

    inputs = [(4, 3), (6, 3)]

    for x, y in inputs:
        result = multiply(x,y)
        print(f"Input: {x}     {y}     Output: {result}")

if __name__ == "__main__":
    main()