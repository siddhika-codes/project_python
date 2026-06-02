contact_list = []

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
       name = input("tell your name :")
       mob_num = int(input("your mobile number :"))
       contact_list.append({"name": name, "number": mob_num})

    elif choice == "2":
        search_name = input("Enter name to search:")
        for el in contact_list:
            if el["name"] == search_name:
                print(el["name"], "→", el["number"])
            
    elif choice == "3":
                print(contact_list)

    else:
        print("Exit")

    



