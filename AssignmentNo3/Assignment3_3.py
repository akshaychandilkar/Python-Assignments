def find_minimum_number():
    n = int(input("Number of elements : "))
    num_list = []

    print("Input Elements: ")
    for i in range(n):
        num = int(input())
        num_list.append(num)

    min_num = min(num_list)
    return min_num

result = find_minimum_number()
print("Output: ",result)