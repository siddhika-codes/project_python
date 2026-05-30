expenses = []
total = 0
while True:
    expense_name = input("your expense name :")
    expense_amt = int(input("amout incurred in expense :"))
    expenses.append({"name" : expense_name , "amount" : expense_amt})

    expenses_add = input("Add Another Expense ? Yes/No")
    if expenses_add == "No":
        break

for el in expenses:
    print(el["name"], "→ ₹", el["amount"])
    total = total + el["amount"]

print("Total: ₹", total)











