# Import necessary libraries
import streamlit as st

# Define the Employee class
class Employee:
    def __init__(self, name, assigned_task, attendance, leaves, completed_tasks, communication_skills, team_collaboration, technical_skills):
        self.name = name
        self.assigned_task = assigned_task
        self.attendance = attendance
        self.leaves = leaves
        self.completed_tasks = completed_tasks
        self.communication_skills = communication_skills
        self.team_collaboration = team_collaboration
        self.technical_skills = technical_skills

    def calculate_performance(self):
        # Calculate performance based on attendance, completed tasks, and additional skills
        performance = (
            (self.attendance / 100) * 
            (self.completed_tasks / self.assigned_task) * 
            (self.communication_skills + self.team_collaboration + self.technical_skills) / 3
        ) * 100
        return performance

# Function to display employee information and performance
def display_employee_info(employee):
    st.write(f"Name: {employee.name}")
    st.write(f"Assigned Tasks: {employee.assigned_task}")
    st.write(f"Attendance: {employee.attendance}%")
    st.write(f"Leaves: {employee.leaves}")
    st.write(f"Completed Tasks: {employee.completed_tasks}")
    st.write(f"Communication Skills: {employee.communication_skills}")
    st.write(f"Team Collaboration: {employee.team_collaboration}")
    st.write(f"Technical Skills: {employee.technical_skills}")
    st.write(f"Performance: {employee.calculate_performance():.2f}%")

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
    communication_skills = st.number_input("Enter communication skills rating (1-10):", min_value=1, max_value=10)
    team_collaboration = st.number_input("Enter team collaboration rating (1-10):", min_value=1, max_value=10)
    technical_skills = st.number_input("Enter technical skills rating (1-10):", min_value=1, max_value=10)

    # Create an Employee object
    employee = Employee(name, assigned_task, attendance, leaves, completed_tasks, communication_skills, team_collaboration, technical_skills)

    # Display employee information and performance
    if st.button("Calculate Performance"):
        display_employee_info(employee)

# Run the application
if __name__ == "__main__":
    main()
