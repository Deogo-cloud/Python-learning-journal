print("--Tips calculator--")
meals_price=float(input("Meals price:"))
tips_percentage=int(input("Tips percentage:"))

tips_amount=meals_price*(tips_percentage/100)
total_bills=tips_amount+meals_price
print("Total bills:",total_bills)
