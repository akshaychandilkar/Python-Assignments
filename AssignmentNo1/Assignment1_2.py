
def chkNum(number):
    if number % 2 == 0:
        print("{} is even number".format(number))
    
    else:
        print("{} is odd number".format(number))
        
def main():
    chkNum(11)
    chkNum(8)

if __name__ == "__main__":
    main()