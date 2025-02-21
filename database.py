#Creates a bank.db database if it doesn’t exist
# Stores users with username, password, and balance
#Allows deposits, withdrawals, and transfers
#Checks balance of any user

import sqlite3

# Connect to database (creates if not exists)
def connect_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Function to create a new user
def create_user(username, password):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        print(f"User '{username}' created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists!")

    conn.close()

# Function to check balance
def check_balance(username):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None  # User not found

# Function to deposit money
def deposit(username, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET balance = balance + ? WHERE username = ?", (amount, username))
    conn.commit()
    conn.close()

# Function to withdraw money
def withdraw(username, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and result[0] >= amount:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, username))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False  # Insufficient balance

# Function to transfer money between users
def transfer(from_user, to_user, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE username = ?", (from_user,))
    sender_balance = cursor.fetchone()

    cursor.execute("SELECT balance FROM users WHERE username = ?", (to_user,))
    receiver_balance = cursor.fetchone()

    if sender_balance and receiver_balance and sender_balance[0] >= amount:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, from_user))
        cursor.execute("UPDATE users SET balance = balance + ? WHERE username = ?", (amount, to_user))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False  # Transfer failed (insufficient balance or user not found)

# Initialize the database
connect_db()
