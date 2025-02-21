"""You can Sign Up and create an account
You can Log In with your username & password"""

import account

while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        account.signup(username, password)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if account.login(username, password):
            print("Login Successful!")

    elif choice == "3":
        break

    else:
        print("Invalid choice! Try again.")
