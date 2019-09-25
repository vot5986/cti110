#Write a pogram that calculates the total amount of a meal purchased at a restaurant.
#The pogram should ask the user to enter the charge for the food,
#then calcuate the amounts of a 18 percent tip and 7 percent sales tax.
#Display each of these amounts and the total.
#24SEP19
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#That Vo
#


foodCharge = float( input("Please enter the charge of the food: " ))

tip = 0.18 * foodCharge

salesTax = 0.07 * foodCharge

total = foodCharge + tip + salesTax

print("Food Charge: $" + format(foodCharge, ",.2f"), "Tip: $" + \
       format( tip, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "Total: $" + format( total, ",.2f"), sep = "\n")
