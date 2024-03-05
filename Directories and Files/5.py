filename= input()
idk = input()
my_list = idk.split()
with open(filename, 'w') as file:
    for item in my_list:
        file.write(item + '\n')

