
def display_pattern(n):
    if n > 0:
        print(n, end="\t")
        display_pattern(n - 1)
        
def main():
    n = int(input("Enter a number: "))
    display_pattern(n)

if __name__ == "__main__":
    main()