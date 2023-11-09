from functools import reduce

def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2

def add (x, y):
    return x + y

def main():
    input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    filtered_list = list(filter(is_even, input_list))

    squared_list = list(map(square,filtered_list))

    result = reduce(add, squared_list)

    print("Input List =",input_list)
    print("List after filter =",filtered_list)
    print("List after map =",squared_list)
    print("Output of reduce =",result)

if __name__ == "__main__":
    main()

