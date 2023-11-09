import threading

def evenfactor(number):
    sum_even = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            sum_even += i

    print(f"Sum of even factors of {number}: {sum_even}")

def oddfactor(number):
    sum_odd = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 != 0:
            sum_odd += i

    print(f"Sum of odd factors of {number}: {sum_odd}")

def main():
    number = int(input("Enter an interger: ")) 

    even_thread = threading.Thread(target=evenfactor, args=(number,))
    odd_thread = threading.Thread(target=oddfactor, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()