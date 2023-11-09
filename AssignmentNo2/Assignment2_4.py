
def sum_of_factors(n):
    factors = [1]
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append(i)
    return sum(factors)

num = int(input("Enter a number: "))
result = sum_of_factors(num)
print("Sum of factors:", result)

