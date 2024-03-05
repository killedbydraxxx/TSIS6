logic = input('write "1" if its true, "" if false: ') 
my_tuple = tuple(map(bool, logic.split()))
print(all(my_tuple))
