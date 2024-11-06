# view_employee.py

import tkinter as tk
from employee_data import get_employees

def open_view_employee():
    root = tk.Toplevel()
    root.title("View Employees")
    root.geometry("600x400")

    employees = get_employees()
    if employees:
        for idx, employee in enumerate(employees):
            tk.Label(root, text=f"ID: {employee['emp_id']}").grid(row=idx, column=0, padx=10, sticky="w")
            tk.Label(root, text=f"Name: {employee['name']}").grid(row=idx, column=1, padx=10, sticky="w")
            tk.Label(root, text=f"Position: {employee['position']}").grid(row=idx, column=2, padx=10, sticky="w")
            tk.Label(root, text=f"Net Salary: {employee['net_salary']}").grid(row=idx, column=3, padx=10, sticky="w")
    else:
        tk.Label(root, text="No employees found").pack()

    tk.Button(root, text="Back", command=root.destroy).pack(pady=10)