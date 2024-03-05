def multiply(numbers):
    answer = 1
    for number in numbers:
        answer *= number
    return result

input_num = list(map(int, input().split()))

some = multiply(input_num)

print(some)
