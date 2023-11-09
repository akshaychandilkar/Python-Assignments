def display_pattern(n):
    if n > 0:
        display_pattern(n - 1)
        print("*", end="\t")
   
def main():
    n = int(input("Enter a number: "))
    display_pattern(n)

if __name__ == "__main__":
    main()