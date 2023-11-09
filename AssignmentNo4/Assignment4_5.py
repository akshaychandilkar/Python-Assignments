from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def multiply_by_2(num):
    return num * 2

def find_maximum(x, y):
    return max(x, y)

def main():
    input_list = [2, 70, 11, 10, 17, 23, 31, 77]

    filtered_list = list(filter(is_prime, input_list))

    multiplied_list  = list(map(multiply_by_2, filtered_list))

    result = reduce(find_maximum, multiplied_list)

    print("Input List =",input_list)
    print("List after filter =",filtered_list)
    print("List after map =",multiplied_list)
    print("Output of reduce =",result)

if __name__ == "__main__":
    main()
