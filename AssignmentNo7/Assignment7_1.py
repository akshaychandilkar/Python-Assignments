import threading 

def even_numbers():
    for i in range(2, 21, 2):
        print(f"Even Thread: {i}")

def odd_numbers():
    for i in range(1, 20, 2):
        print(f"Odd Thread: {i}")

def main():
    even_thread = threading.Thread(target=even_numbers)
    odd_thread = threading.Thread(target=odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()