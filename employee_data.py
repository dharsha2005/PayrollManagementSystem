import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('employee_data.db')
cursor = conn.cursor()

# Create table with the new columns
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    emp_id INTEGER PRIMARY KEY,
                    name TEXT,
                    position TEXT,
                    address TEXT,
                    phone TEXT,
                    salary REAL,
                    pf REAL DEFAULT 0,
                    conveyance REAL DEFAULT 0,
                    medical REAL DEFAULT 0
                 )''')
conn.commit()

def add_employee(employee):
    cursor.execute('''INSERT INTO employees (emp_id, name, position, address, phone, salary, pf, conveyance, medical)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (employee['emp_id'], employee['name'], employee['position'], employee['address'], 
                    employee['phone'], employee['salary'], employee.get('pf', 0), 
                    employee.get('conveyance', 0), employee.get('medical', 0)))
    conn.commit()

def delete_employee(emp_id):
    cursor.execute('''DELETE FROM employees WHERE emp_id = ?''', (emp_id,))
    conn.commit()
    return cursor.rowcount > 0

def modify_employee(emp_id, new_data):
    # We use a dynamic query update
    set_clause = ', '.join([f"{key} = ?" for key in new_data])
    query = f"UPDATE employees SET {set_clause} WHERE emp_id = ?"
    cursor.execute(query, (*new_data.values(), emp_id))
    conn.commit()
    return cursor.rowcount > 0

def get_employees(): 
    cursor.execute("SELECT * FROM employees") 
    rows = cursor.fetchall() 
    employees = [] 
    for row in rows: 
        employee = { "emp_id": row[0], "name": row[1], "position": row[2], "address": row[3], "phone": row[4], "salary": row[5], "pf": row[6], "conveyance": row[7], "medical": row[8] } # Calculate net salary 
        employee["net_salary"] = calculate_net_salary(employee) 
        employees.append(employee) 
        return employees

def calculate_net_salary(employee):
    salary = float(employee["salary"])
    pf = float(employee.get("pf", 0))
    conveyance = float(employee.get("conveyance", 0))
    medical = float(employee.get("medical", 0))
    net_salary = salary - (pf + conveyance + medical)
    return net_salary

# Close the connection when done
def close_connection():
    conn.close()
