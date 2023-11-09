
def display_pattern(n):
    for i in range(n, 0, -1):
        print("  " * (n - 1), "*   " * i)

user_input = int(input("Enter a number: "))
display_pattern(user_input)
