import os

f = "Z:\\damori.pierce\PythonProjects\Burmese\\Network Automation\Lesson 4\SW_List.txt"

# File exists, you can open it here.
if not os.path.isfile(f):
    print(f"The file '{f}' does not exist.")
else:
    print(f)