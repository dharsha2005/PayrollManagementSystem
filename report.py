# report.py
import tkinter as tk
from tkinter import messagebox
from employee_data import get_employees


def open_report():
    root = tk.Toplevel()
    root.title("Employee Salary Report")
    root.geometry("600x400")

    # Fetch employee data
    employees = get_employees()

    # Create a function to display the employee data in the table
    def display_data(employee_list):
        # Clear previous data
        for widget in root.grid_slaves():
            widget.grid_forget()

        # Set header labels
        headers = ["Employee ID", "Name", "Position", "Salary", "Annual Salary", "Half Year Salary", "Quarterly Salary"]
        for col, header in enumerate(headers):
            tk.Label(root, text=header, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=10, pady=5)

        # Display employee details
        for idx, employee in enumerate(employee_list):
            annual_salary = float(employee["salary"]) * 12
            half_year_salary = annual_salary / 2
            quarterly_salary = annual_salary / 4
            row = idx + 1

            tk.Label(root, text=employee["emp_id"]).grid(row=row, column=0, padx=10, pady=5)
            tk.Label(root, text=employee["name"]).grid(row=row, column=1, padx=10, pady=5)
            tk.Label(root, text=employee["position"]).grid(row=row, column=2, padx=10, pady=5)
            tk.Label(root, text=employee["salary"]).grid(row=row, column=3, padx=10, pady=5)
            tk.Label(root, text=annual_salary).grid(row=row, column=4, padx=10, pady=5)
            tk.Label(root, text=half_year_salary).grid(row=row, column=5, padx=10, pady=5)
            tk.Label(root, text=quarterly_salary).grid(row=row, column=6, padx=10, pady=5)

    # Display the initial employee data
    display_data(employees)

    # Function to search employees by position
    def search_by_position():
        position = position_entry.get().strip().lower()
        filtered_employees = [emp for emp in employees if position in emp["position"].lower()]

        if filtered_employees:
            display_data(filtered_employees)
        else:
            messagebox.showinfo("No Results", "No employees found with the given position.")

    # Create position search bar and button
    tk.Label(root, text="Search by Position").grid(row=len(employees) + 1, column=0, padx=10, pady=10)
    position_entry = tk.Entry(root)
    position_entry.grid(row=len(employees) + 1, column=1, padx=10, pady=10)

    search_button = tk.Button(root, text="Search", command=search_by_position)
    search_button.grid(row=len(employees) + 1, column=2, padx=10, pady=10)

    # Back button
    tk.Button(root, text="Back", command=root.destroy).grid(row=len(employees) + 2, column=0, pady=10)

    root.mainloop()