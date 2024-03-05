import os

path = input()

print("\nDirectories:")
for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isdir(full_path):
        print(item)

print("\nFiles:")
for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        print(item)

print("\nAll directories and files:")
for item in os.listdir(path): 
    print(item)
