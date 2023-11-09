def find_maximum_number():
    n = int(input("Number of elements : "))
    num_list = []

    print("Input Elements: ")
    for i in range(n):
        num = int(input())
        num_list.append(num)

    max_num = max(num_list)
    return max_num

result = find_maximum_number()
print("Output: ",result)