

f = int(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate: "))
n = int(input("Enter the number of years the money will grow: "))

p = f/(1+r)**n
z = p * (1+r)

print(f"You will need to deposit this amount: {p:.2f}")
print(f"Previous one: {z:.2f}")