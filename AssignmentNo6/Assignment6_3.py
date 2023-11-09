class Numbers:
    def __init__(self, Value):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
            return True

    def ChkPerfect(self):
        return self.SumFactors() == 2 * self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)

def main():
    num1 = Numbers(6)
    num2 = Numbers(5)

    print("Is num1 prime?", num1.ChkPrime())
    print("Is num2 prime?", num1.ChkPrime())
    print("Is num1 perfect?", num1.ChkPerfect())
    print("Is num2 perfect?", num1.ChkPerfect())
    print("Factors of num1:", num1.Factors())
    print("Factors of num2:", num1.Factors())
    print("Sum of factors of num1:", num1.SumFactors())
    print("Sum of factors of num2:", num1.SumFactors())

if __name__ == "__main__":
    main()