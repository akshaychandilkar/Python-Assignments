import MarvellousNum

def ListPrime(numbers):
    prime_sum = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num
    return prime_sum

def main():
    N = int(input("Numbers of Elements: "))
    input_elements = []
    for i in range(N):
        num = int(input("Input Elements: "))
        input_elements.append(num)

    result = ListPrime(input_elements)
    print("Output:",result,"(", "+".join(str(num)for num in input_elements if MarvellousNum.ChkPrime(num)),")")

if __name__ == "__main__":
    main()