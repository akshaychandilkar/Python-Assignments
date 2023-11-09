class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter account holder's name: ")
        self.Amount = float(input("Enter initial amount: "))

    def Display(self):
        print(f"Account Holder's Name: {self.Name}")
        print(f"Account Balance: {self.Amount}")

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.Amount += deposit_amount
        print(f"Deposit {deposit_amount} successfully...")
        self.Display()

    def Withdraw(self):
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        if withdrawal_amount <= self.Amount:
            self.Amount -= withdrawal_amount
            print(f"Withdraw {withdrawal_amount} successfully...")
        else:
            print("Insufficient balance to withdraw.")
        self.Display()

    def calculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated at {BankAccount.ROI}%: {interest}")
        self.Display()

def main():
    account1 = BankAccount()
    account2 = BankAccount()

    account1.Display()
    account1.Deposit()
    account1.Withdraw()
    account1.calculateInterest()

    account2.Display()
    account2.Deposit()
    account2.Withdraw()
    account2.calculateInterest()

if __name__ == "__main__":
    main()