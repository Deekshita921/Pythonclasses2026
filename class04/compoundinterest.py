p = int(input("Enter initial principal balance: "))
r = int(input("Enter annual interest rate: "))
t = int(input("Enter time(in years): "))

a = p * (1 + r/100) ** t
compound_interest = a - p
print("Compound Interest =", compound_interest)