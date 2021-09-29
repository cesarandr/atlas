import sys # for adding paths at runtime
sys.path.insert(1, "/home/cesar/Projekte/Python/atlas/base")

from user import User
from sheet import Sheet
from task import Task

user_one = User("Cesar", "Test")

task_one = Task("Do Homework", user_one, "29.09.2021")
task_two = Task("Do Sports", user_one, "30.09.2021")

sheet_one = Sheet("My first Sheet")
sheet_one.add_task(task_one)
sheet_one.add_task(task_two)

sheet_one.display()

print(sheet_one.get_tasks())

