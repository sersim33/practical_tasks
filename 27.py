f = float(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
n = int(input("Enter the number of years the money will grow: "))

p = f / ((1 + r) ** n)
z = p * ((1 + r) ** n)

print(f"You will need to deposit this amount: {p:.2f}")
print(f"Recalculated future value: {z:.2f}")
