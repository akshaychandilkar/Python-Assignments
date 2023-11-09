def find_frequency():
    n = int(input("Number of elements : "))
    num_list = []

    print("Input Elements: ")
    for i in range(n):
        num = int(input())
        num_list.append(num)

    search_num = int(input("Element to search: "))
    frequency = num_list.count(search_num)
    return frequency

result = find_frequency()
print("Output: ",result)