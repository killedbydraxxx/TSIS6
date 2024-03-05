import os

path = input()

if os.path.exists(path):
    print("exists")
else:
    print("not exists")
    exit()

if os.access(path, os.R_OK):
    print("readable")
else:
    print("not readable")

if os.access(path, os.W_OK):
    print("writable")
else:
    print("not writable")

if os.access(path, os.X_OK):
    print("executable")
else:
    print("not executable")
