num = input("Enter a number: ")

sum_prime = 0

for digit in num:
    d = int(digit)
    if d in [2, 3, 5, 7]:
        sum_prime += d

print("Sum of prime digits:", sum_prime)
