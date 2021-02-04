first_number = int(input('Enter first number: '))
operator = input('Enter operator: ')
second_number = int(input('Enter second number: '))

if operator == '+':
    sum = first_number + second_number
    print(sum)
elif operator == '-':
    sub = first_number - second_number
    print(sub)
elif operator == '*':
    mul = first_number * second_number
    print(mul)
elif operator == '/':
    div = first_number / second_number
    print(div)
else:
    print('Please select a valid operator.')