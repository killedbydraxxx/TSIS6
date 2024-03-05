file1 = input()
file2 = input()
with open(file1, 'r') as f1:
    copy = f1.read()
with open(file2, 'w') as f2:
    f2.write(copy)
