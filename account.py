#Allows new users to sign up
#Users can log in by checking credentials

import database

def user_menu():
    print("\n 💰 Welcome to the Bank Management System 💰")
    print("1️⃣ Deposit Money")
    print("2️⃣ Withdraw Money")
    print("3️⃣ Transfer Money")
    print("4️⃣ Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter your username: ")
        amount = float(input("Enter amount to deposit: "))
        database.deposit(username, amount)

    elif choice == "2":
        username = input("Enter your username: ")
        amount = float(input("Enter amount to withdraw: "))
        database.withdraw(username, amount)

    elif choice == "3":
        from_user = input("Enter your username: ")
        to_user = input("Enter recipient's username: ")
        amount = float(input("Enter amount to transfer: "))
        database.transfer(from_user, to_user, amount)

    elif choice == "4":
        print("✅ Exiting... Goodbye!")
        return

    else:
        print("❌ Invalid choice!")

    user_menu()  # Loop back to menu


# Run the menu
user_menu()
