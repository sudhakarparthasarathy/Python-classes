#Tip Calculator for a Group of friends / Splitting of expenses
print("Welcome to the tip calculator.")
Bill = float(input("Whats ur total bill:"))
T = float(input("Percantage of tip ? 10,12, or 15"))
Tip = float(T/100)
peoples = float(input("split for persons? "))
cal = ((Bill*Tip)+Bill)/peoples

amt = f"Each should pay a amout of: {cal}"
print (amt)
