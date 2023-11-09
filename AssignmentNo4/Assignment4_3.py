from functools import reduce

def main():
    input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    filtered_list = list(filter(lambda x: 70 <= x <= 90, input_list))

    mapped_list = list(map(lambda x: x + 10,filtered_list))

    product = reduce(lambda x, y: x * y, mapped_list)

    print("List after filter: ",filtered_list)
    print("List after map: ",mapped_list)
    print("Output of reduce =",product)

if __name__ == "__main__":
    main()