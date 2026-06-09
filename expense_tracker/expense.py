# Third mini project - Expense Tracker
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

# Expesne tracker mini project with functions in it.
Expenses = []
def add_Expenses():
    Expense_name = input("your expense name :")
    Expense_amt = int(input("enter your expense amt :"))
    Expenses.append({"name" : Expense_name, "amount" : Expense_amt})

def view_Expenses():
    for el in Expenses:
        print(el["name"], ":", el["amount"])
        
def get_total():
    sum = 0
    for el in Expenses:
        sum += el["amount"]
    print(sum)

def main_program():
    while True:
          print("add / view / total / exit")
          userAsk = input("your prefernce :")
          if userAsk == "add":
            add_Expenses()
          elif userAsk == "view":
            view_Expenses()
          elif userAsk == "total":
            get_total()
          else:
            print("EXIT")
            break
          
main_program()
        
        




















