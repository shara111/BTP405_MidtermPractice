from datetime import datetime
from project import Project
from employee import Employee
from managementsystem import ManagementSystem
from task import Task
import unittest

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self): # 1 marks
        employee = Employee("John Doe", 101, "Developer", 50000)
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.emp_id, 101)
        self.assertEqual(employee.role, "Developer")
        self.assertEqual(employee.salary, 50000)

class TestProject(unittest.TestCase):
    def test_project_creation(self):  # 2 marks
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        self.assertEqual(project.project_id, 1)
        self.assertEqual(project.name, "Project X")
        self.assertEqual(project.description, "Description of Project X")

    def test_assign_employee(self): # 2 marks
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        employee = Employee("John Doe", 101, "Developer", 50000)
        project.assign_employee(employee)
        self.assertEqual(len(project.employees), 1)

class TestTask(unittest.TestCase):
    def test_task_creation(self): # 2 marks
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        task = Task(1, "Task 1", datetime(2024, 2, 1), "Incomplete", project)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.description, "Task 1")
        self.assertEqual(task.status, "Incomplete")

class TestManagementSystem(unittest.TestCase):
    def test_add_employee(self): # 1 marks
        management_system = ManagementSystem()
        employee = Employee("John Doe", 101, "Developer", 50000)
        management_system.add_employee(employee)
        self.assertEqual(len(management_system.employees), 1)

    def test_remove_employee(self): # 1 marks
        management_system = ManagementSystem()
        employee = Employee("John Doe", 101, "Developer", 50000)
        management_system.add_employee(employee)
        management_system.remove_employee(101)
        self.assertEqual(len(management_system.employees), 0)

    def test_add_project(self):  # 1 marks
        management_system = ManagementSystem()
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        management_system.add_project(project)
        self.assertEqual(len(management_system.projects), 1)

    def test_add_task(self): # 1 marks
        management_system = ManagementSystem()
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        task = Task(1, "Task 1", datetime(2024, 2, 1), "Incomplete", project)
        management_system.add_task(task)
        self.assertEqual(len(management_system.tasks), 1)

    def test_assign_employee_to_project(self): # 3 marks
        management_system = ManagementSystem()
        employee = Employee("John Doe", 101, "Developer", 50000)
        management_system.add_employee(employee)
        project = Project(1, "Project X", "Description of Project X", datetime(2024, 1, 1), datetime(2024, 12, 31))
        management_system.add_project(project)
        management_system.assign_employee_to_project(101, 1)
        self.assertEqual(len(project.employees), 1)

if __name__ == "__main__":
    unittest.main()