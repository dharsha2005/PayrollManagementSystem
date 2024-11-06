# delete_employee.py

import tkinter as tk
from tkinter import messagebox
from employee_data import delete_employee

def open_delete_employee():
    def delete():
        emp_id = emp_id_entry.get().strip()
        if delete_employee(emp_id):
            messagebox.showinfo("Success", f"Employee {emp_id} deleted.")
            root.destroy()
        else:
            messagebox.showerror("Error", f"No employee found with ID {emp_id}")

    root = tk.Toplevel()
    root.title("Delete Employee")
    root.geometry("300x150")

    tk.Label(root, text="Employee ID to Delete").pack()
    emp_id_entry = tk.Entry(root)
    emp_id_entry.pack()

    tk.Button(root, text="Delete", command=delete).pack(pady=10)
    tk.Button(root, text="Back", command=root.destroy).pack()