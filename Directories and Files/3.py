import os

path = input()

if os.path.exists(path):
    print("Path exists.")
    if os.path.isfile(path):
        print("File")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    elif os.path.isdir(path):
        print("Directory.")
        print("Directory path:", path)
else:
    print("Path does not exist.")
