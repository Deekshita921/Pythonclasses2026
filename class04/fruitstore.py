DOZEN = 12
DISCOUNT = 2
GST = 12.5

cost_of_apples = 12
cost_of_mangos = 34

quant_of_apples = 5 * DOZEN
quant_of_mangos = 3 * DOZEN

total_sp = cost_of_apples * quant_of_apples + cost_of_mangos * quant_of_mangos
print("Total Selling Price =", total_sp)

discount_amount = (total_sp * DISCOUNT)/100
print("Discount Amount =", discount_amount)

payable_amount = total_sp - discount_amount
print("Payable Amount =", payable_amount)

gst_on_fruits = (payable_amount * GST)/100
print("GST on fruits =", gst_on_fruits)

billable_amount = payable_amount + gst_on_fruits
print("Total Bill =", round(billable_amount))