"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

while True:
    try:
        monthly_savings = int(input("How much do you want to save each month? £"))
        break
    except:
        print("Invalid input: Please enter a valid number. ")


annual_savings = monthly_savings * 12

print(f"You will save £{annual_savings} in one year")

interest = annual_savings * 0.008
total_savings = annual_savings + interest


print(f"Your total savings including interest will be £{total_savings:.2f}")




      

