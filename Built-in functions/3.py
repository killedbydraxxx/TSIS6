def check(s):
    clean = ''.join(s.split()).lower()
    return clean == clean[::-1]

string = input()
if check(input_string):
    print("palindrome")
else:
    print("not palindrome")
