
def display_pattern(n):
    for i in range(n):
        for j in range(1, n+1):
            print(j, end="\t")
        print()

user_input = int(input("Enter a number: "))
display_pattern(user_input)