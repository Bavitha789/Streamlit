import streamlit as st

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.performance_rating = 0
        self.tasks_completed = 0
        self.leaves_taken = 0

    def calculate_performance(self):
        # Assume some logic for calculating performance rating
        base_performance = (self.salary / 1000) * 1.5
        task_bonus = self.tasks_completed * 0.2
        leaves_penalty = self.leaves_taken * 0.1
        self.performance_rating = base_performance + task_bonus - leaves_penalty

    def display_info(self):
        st.write(f"Name: {self.name}")
        st.write(f"Age: {self.age}")
        st.write(f"Position: {self.position}")
        st.write(f"Salary: ${self.salary}")
        st.write(f"Performance Rating: {self.performance_rating}")
        st.write(f"Tasks Completed: {self.tasks_completed}")
        st.write(f"Leaves Taken: {self.leaves_taken}")


def main():
    st.title("Employee Performance Calculator")

    # Input employee details
    name = st.text_input("Enter Name:")
    age = st.number_input("Enter Age:", min_value=18, max_value=100)
    position = st.text_input("Enter Position:")
    salary = st.number_input("Enter Salary:", min_value=0)

    # Create an Employee object
    employee = Employee(name, age, position, salary)

    # Input task and leave details
    employee.tasks_completed = st.number_input("Enter Tasks Completed:", min_value=0)
    employee.leaves_taken = st.number_input("Enter Leaves Taken:", min_value=0)

    # Display employee information
    if st.button("Display Employee Info"):
        employee.display_info()

    # Calculate and display performance
    if st.button("Calculate Performance"):
        employee.calculate_performance()
        st.success("Performance calculated successfully!")
        st.write(f"Performance Rating: {employee.performance_rating}")


if __name__ == "__main__":
    main()
