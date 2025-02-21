#GUI code to integrate with the database functions
import tkinter as tk
from tkinter import messagebox
import database

# Create main window
root = tk.Tk()
root.title("Bank Management System")
root.geometry("400x500")


# Function to create a new user
def create_user():
    username = entry_user.get()
    password = entry_password.get()

    if username and password:
        database.create_user(username, password)
        messagebox.showinfo("Success", f"User '{username}' created successfully!")
    else:
        messagebox.showerror("Error", "Please enter both username and password.")


# Function to deposit money
def deposit_money():
    username = entry_user.get()
    amount = entry_amount.get()

    if username and amount.isdigit():
        database.deposit(username, float(amount))
        messagebox.showinfo("Success", f"Deposited {amount} successfully!")
    else:
        messagebox.showerror("Error", "Invalid username or amount.")


# Function to withdraw money
def withdraw_money():
    username = entry_user.get()
    amount = entry_amount.get()

    if username and amount.isdigit():
        success = database.withdraw(username, float(amount))
        if success:
            messagebox.showinfo("Success", f"Withdrawn {amount} successfully!")
        else:
            messagebox.showerror("Error", "Insufficient balance or user not found.")
    else:
        messagebox.showerror("Error", "Invalid username or amount.")


# Function to transfer money
def transfer_money():
    from_user = entry_user.get()
    to_user = entry_recipient.get()
    amount = entry_amount.get()

    if from_user and to_user and amount.isdigit():
        success = database.transfer(from_user, to_user, float(amount))
        if success:
            messagebox.showinfo("Success", f"Transferred {amount} to {to_user} successfully!")
        else:
            messagebox.showerror("Error", "Transfer failed: Insufficient balance or invalid users.")
    else:
        messagebox.showerror("Error", "Invalid details.")


# Function to check balance
def check_balance():
    username = entry_user.get()

    if username:
        balance = database.check_balance(username)
        if balance is not None:
            messagebox.showinfo("Balance", f"{username}'s Balance: {balance}")
        else:
            messagebox.showerror("Error", "User not found!")
    else:
        messagebox.showerror("Error", "Please enter a username.")


# GUI Layout
tk.Label(root, text="Bank Management System", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

tk.Label(root, text="Recipient (For Transfer):").pack()
entry_recipient = tk.Entry(root)
entry_recipient.pack()

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

btn_create_user = tk.Button(root, text="Create User", command=create_user)
btn_create_user.pack(pady=5)

btn_deposit = tk.Button(root, text="Deposit", command=deposit_money)
btn_deposit.pack(pady=5)

btn_withdraw = tk.Button(root, text="Withdraw", command=withdraw_money)
btn_withdraw.pack(pady=5)

btn_transfer = tk.Button(root, text="Transfer", command=transfer_money)
btn_transfer.pack(pady=5)

btn_check_balance = tk.Button(root, text="Check Balance", command=check_balance)
btn_check_balance.pack(pady=5)

# Run the GUI
root.mainloop()
