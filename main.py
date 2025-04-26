employees = {}
def add_employee(emp_id, name, age, position, salary):
    employees[emp_id] = {
        'name': name,
        'age': age,
        'position': position,
        'salary': salary
    }
    print(f"Employee {name} added successfully!")
def view_employee(emp_id):
    if emp_id in employees:
        emp = employees[emp_id]
        print(
            f"ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Position: {emp['position']}, Salary: {emp['salary']}")
    else:
        print(f"Employee with ID {emp_id} not found.")
def update_employee(emp_id, name=None, age=None, position=None, salary=None):
    if emp_id in employees:
        if name:
            employees[emp_id]['name'] = name
        if age:
            employees[emp_id]['age'] = age
        if position:
            employees[emp_id]['position'] = position
        if salary:
            employees[emp_id]['salary'] = salary
        print(f"Employee {emp_id} updated successfully!")
    else:
        print(f"Employee with ID {emp_id} not found.")
def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee {emp_id} deleted successfully!")
    else:
        print(f"Employee with ID {emp_id} not found.")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            add_employee(emp_id, name, age, position, salary)

        elif choice == '2':
            emp_id = input("Enter employee ID to view: ")
            view_employee(emp_id)

        elif choice == '3':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            position = input("Enter new position (leave blank to skip): ")
            salary = input("Enter new salary (leave blank to skip): ")
            update_employee(emp_id, name, age if age else None, position, salary if salary else None)

        elif choice == '4':
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)

        elif choice == '5':
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
