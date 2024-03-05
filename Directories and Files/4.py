file_path=input("Get your directories way: ")
with open(file_path, 'r') as file:
        lines=file.readlines()
        print(len(lines))

