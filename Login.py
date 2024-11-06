#login.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

DATABASE_FILE = "user_data.db"

def load_user_data():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users")
    users = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return users

def login():
    username = username_entry.get()
    password = password_entry.get()
    users = load_user_data()

    if username in users and users[username] == password:
        root.destroy()  # Close the login window
        subprocess.run(["python", "dashboard.py"])  # Open the employee screen
    else:
        message_label.config(text="Invalid credentials. Try again.", fg="red")

def open_signup_screen():
    root.destroy()
    subprocess.run(["python", "signup.py"])

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    message_label.config(text="")

# Create the Login screen
root = tk.Tk()
root.title("Payroll Management System - Login")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Payroll Management System", font=("Serif", 20, "bold"), fg="#0066CC")
title_label.pack(pady=10)

username_label = tk.Label(root, text="Username:")
username_label.pack(anchor="w", padx=50, pady=(10, 0))
username_entry = tk.Entry(root, width=30)
username_entry.pack(padx=50)

password_label = tk.Label(root, text="Password:")
password_label.pack(anchor="w", padx=50, pady=(10, 0))
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(padx=50)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

login_button = tk.Button(button_frame, text="Login", command=login)
login_button.grid(row=0, column=0, padx=10)

signup_button = tk.Button(button_frame, text="Sign Up", command=open_signup_screen)
signup_button.grid(row=0, column=1, padx=10)

message_label = tk.Label(root, text="", fg="red")
message_label.pack(pady=10)

root.mainloop()
