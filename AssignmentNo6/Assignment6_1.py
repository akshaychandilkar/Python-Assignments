class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
            print(f"{self.Name} by {self.Author}.No Of Books: {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("Linux System Programming","Robert love")    
    obj1.Display() 

    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.Display()  

if __name__ == "__main__":
    main()