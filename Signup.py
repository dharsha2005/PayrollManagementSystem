#signup
import tkinter as tk
import sqlite3
import subprocess

# Database file to store user data
DATABASE_FILE = "user_data.db"

def create_table():
    """Create the users table if it does not exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def signup():
    username = username_entry.get()
    password = password_entry.get()  # Retrieve the password from the password entry field

    if username and password:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            message_label.config(text="Signup successful! You can now log in.", fg="green")
            clear_fields()  # Clear input fields after successful signup
        except sqlite3.IntegrityError:
            message_label.config(text="Username already exists. Try another.", fg="red")
        finally:
            conn.close()
    else:
        message_label.config(text="Please fill out both fields.", fg="red")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def go_to_login_screen():
    root.destroy()
    subprocess.run(["python", "login.py"])  # Adjust this based on your login script name

# Create the Signup screen
root = tk.Tk()
root.title("Payroll Management System - Sign Up")
root.geometry("400x300")
root.resizable(False, False)

# Create the users table when the application starts
create_table()

username_label = tk.Label(root, text="Username:")
username_label.pack(anchor="w", padx=50, pady=(10, 0))
username_entry = tk.Entry(root, width=30)
username_entry.pack(padx=50)

password_label = tk.Label(root, text="Password:")
password_label.pack(anchor="w", padx=50, pady=(10, 0))
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(padx=50)

signup_button = tk.Button(root, text="Sign Up", command=signup)
signup_button.pack(pady=20)

message_label = tk.Label(root, text="", fg="red")
message_label.pack(pady=10)

login_button = tk.Button(root, text="Back to Login", command=go_to_login_screen)
login_button.pack(pady=(0, 20))

root.mainloop()
