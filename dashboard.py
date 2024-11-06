# dashboard.py
import tkinter as tk
from add_employee import open_add_employee
from delete_employee import open_delete_employee
from modify_employee import open_modify_employee
from view_employee import open_view_employee
from report import open_report 

def open_dashboard():
    root = tk.Tk()
    root.title("Employee Dashboard")
    root.geometry("400x400")

    tk.Button(root, text="Add Employee", command=open_add_employee).pack(pady=10)
    tk.Button(root, text="Delete Employee", command=open_delete_employee).pack(pady=10)
    tk.Button(root, text="Modify Employee", command=open_modify_employee).pack(pady=10)
    tk.Button(root, text="View Employee Details", command=open_view_employee).pack(pady=10)
    tk.Button(root, text="View Report", command=open_report).pack(pady=10)  # New Report button

    root.mainloop()

open_dashboard()