import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
clothing = budget.Category("Clothing")
auto = budget.Category("Auto")
auto.deposit(100, "initial deposit")

food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(50, clothing)
food.transfer(20, auto)

clothing.withdraw(25.55)
clothing.withdraw(100)

auto.withdraw(120)


print(food)
print()
print(clothing)
print()
print(auto)
print()
print(create_spend_chart([food, clothing, auto]))
