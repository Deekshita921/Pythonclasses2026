#Grocery store
cost_of_rice = 10 #per kg
cost_of_wheat = 34 #per kg

quan_of_rice = int(input("Enter the quantity of rice in kgs: "))
quan_of_wheat = int(input("Enter the quantity of wheat in kgs: "))

payable_amount_for_rice = quan_of_rice * cost_of_rice
payable_amount_for_wheat = quan_of_wheat * cost_of_wheat
print("Total cost of rice purchase:", payable_amount_for_rice)
print("Total cost of wheat purchase:", payable_amount_for_wheat)

billable_amount = payable_amount_for_rice + payable_amount_for_wheat
print("Aount to be paid:", billable_amount)