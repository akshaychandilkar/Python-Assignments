
def main():
    power_of_two = lambda x: x ** 2

    inputs = [4, 6]

    for input_value in inputs: 
        result = power_of_two(input_value)
        print("Input: ",input_value, "Output: ",result)

if __name__ == "__main__":
    main()