import threading

def sum_even(input_list):
    even_sum = sum(num for num in input_list if num % 2 == 0)
    print("Sum of even elements: ",even_sum)

def sum_odd(input_list):
    odd_sum = sum(num for num in input_list if num % 2 != 0)
    print("Sum of odd elements: ",odd_sum)

def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_thread = threading.Thread(target=sum_even, args=(input_list,))
    odd_thread = threading.Thread(target=sum_odd, args=(input_list,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both thread have finished.")

if __name__ == "__main__":
    main()