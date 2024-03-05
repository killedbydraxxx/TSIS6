filename = input()
count = 0
with open(filename, 'r') as file:
    for line in file:
        count += 1
print(count)
