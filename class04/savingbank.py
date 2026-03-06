balance = 0
initial_deposit = 1500
salary_credited = int(input("Salary credited = "))
online_purchase = float(input("Online purchase = "))
house_rent = int(input("House rent paid = "))
balance = (initial_deposit + salary_credited) - (online_purchase + house_rent)
print("Remaining Balance:", balance)