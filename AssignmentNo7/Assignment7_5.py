import threading

def thread1_function():
    for i in range(1, 51):
        print(f"Thread1: {i}")

def thread2_function():
    for i in range(50, 0,-1):
        print(f"Thread2: {i}")

def main():
    thread1 = threading.Thread(target=thread1_function)
    thread2 = threading.Thread(target=thread2_function)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()