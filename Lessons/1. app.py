import os

f = r"C:\Users\dpierce\PycharmProjects\Burmese\Network_Automation\source_lists\SW_List.txt"

# File exists, you can open it here.
if not os.path.isfile(f):
    print(f"The file '{f}' does not exist.")
else:
    print(f)