# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
# print("Ledger Food:", food.ledger)
# print("Food Budget:", food.available_budget)
# print("\nLedger Clothing:", clothing.ledger)
# print("Clothing Budget:", clothing.available_budget)
# print("\nLedger Auto:", auto.ledger)
# print("Auto Budget:", auto.available_budget)
# print(f"\n{food}")

print(food)
print(clothing)
print(auto)

a = create_spend_chart([food, clothing, auto])
print(a)

text_file = open('test2.txt', 'w')
text_file.write(r'{}'.format(a))
text_file.close()

# Run unit tests automatically
main(module='test_module', exit=False)