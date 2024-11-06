# modify_employee.py

import tkinter as tk
from tkinter import messagebox
from employee_data import modify_employee, calculate_net_salary

def open_modify_employee():
    def save_changes():
        emp_id = emp_id_entry.get().strip()
        new_data = {
            "name": name_entry.get().strip(),
            "position": position_entry.get().strip(),
            "address": address_entry.get().strip(),
            "phone": phone_entry.get().strip(),
            "salary": salary_entry.get().strip(),
            "pf": pf_entry.get().strip(),
            "conveyance": conveyance_entry.get().strip(),
            "medical": medical_entry.get().strip(),
        }
        new_data["net_salary"] = calculate_net_salary(new_data)
        if modify_employee(emp_id, new_data):
            messagebox.showinfo("Success", f"Employee {emp_id} modified.")
            root.destroy()
        else:
            messagebox.showerror("Error", f"No employee found with ID {emp_id}")

    root = tk.Toplevel()
    root.title("Modify Employee")
    root.geometry("300x400")

    tk.Label(root, text="Employee ID").pack()
    emp_id_entry = tk.Entry(root)
    emp_id_entry.pack()

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Position").pack()
    position_entry = tk.Entry(root)
    position_entry.pack()

    tk.Label(root, text="Address").pack()
    address_entry = tk.Entry(root)
    address_entry.pack()

    tk.Label(root, text="Phone").pack()
    phone_entry = tk.Entry(root)
    phone_entry.pack()

    tk.Label(root, text="Salary").pack()
    salary_entry = tk.Entry(root)
    salary_entry.pack()

    tk.Label(root, text="PF").pack()
    pf_entry = tk.Entry(root)
    pf_entry.pack()

    tk.Label(root, text="Conveyance").pack()
    conveyance_entry = tk.Entry(root)
    conveyance_entry.pack()

    tk.Label(root, text="Medical").pack()
    medical_entry = tk.Entry(root)
    medical_entry.pack()

    tk.Button(root, text="Save", command=save_changes).pack(pady=10)
    tk.Button(root, text="Back", command=root.destroy).pack()