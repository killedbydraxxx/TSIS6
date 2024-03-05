def count(s):
    upper = 0
    lower = 0
    
    for some in s:
        if some.isupper():
            upper += 1
        elif some.islower():
            lower += 1

    return upper, lower

string = input()
uppercase, lowercase = count(string)
print(uppercase)
print(lowercase)
