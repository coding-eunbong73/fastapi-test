def menu():
    print("MAIN MENU")
    print("-----------------")
    print("1. Print pay check")
    print("2. Change benefits")
    print("3. Exit")

    choice = input("Choose menu option (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice.  Choose menu option (1-3): ")
    return int(choice)


menu_chosen = True
choice = menu()
print("You chose menu option", choice)