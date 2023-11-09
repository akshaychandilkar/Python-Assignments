
def display_pattern(n):
    for i in range(n):
        print(" ".join(["*"] * n))

number = int(input("Input: "))
display_pattern(number)