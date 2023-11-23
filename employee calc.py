# Import necessary libraries
import streamlit as st

# Define the Employee class
class Employee:
    def __init__(self, name, assigned_task, attendance, leaves, completed_tasks):
        self.name = name
        self.assigned_task = assigned_task
        self.attendance = attendance
        self.leaves = leaves
        self.completed_tasks = completed_tasks

    def calculate_performance(self):
        # Calculate performance based on attendance and completed tasks
        performance = (self.attendance / 100) * (self.completed_tasks / self.assigned_task) * 100
        return performance

# Function to display employee information and performance in a table
def display_employee_info(employee):
    st.write("Employee Information:")
    data = {
        "Name": [employee.name],
        "Assigned Tasks": [employee.assigned_task],
        "Attendance": [f"{employee.attendance}%"],
        "Leaves": [employee.leaves],
        "Completed Tasks": [employee.completed_tasks],
        "Performance": [f"{employee.calculate_performance():.2f}%"],
    }
    table = st.table(data)

# Streamlit application
def main():
    # Title of the application
    st.title("Employee Performance Calculator")

    # Get employee information from the user
    name = st.text_input("Enter employee name:")
    assigned_task = st.number_input("Enter the number of assigned tasks:", min_value=1)
    attendance = st.number_input("Enter attendance percentage:", min_value=0, max_value=100)
    leaves = st.number_input("Enter the number of leaves taken:")
    completed_tasks = st.number_input("Enter the number of completed tasks:", min_value=0, max_value=assigned_task)

    # Create an Employee object
    employee = Employee(name, assigned_task, attendance, leaves, completed_tasks)

    # Display employee information and performance in a table
    if st.button("Calculate Performance"):
        display_employee_info(employee)

# Run the application
if __name__ == "__main__":
    main()
