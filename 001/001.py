# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

days = [1, 2, 3, 4, 5]
weekends = [6, 7]
number = int(input('Enter the day of the week: '))
if number in weekends:
    print(f'{number} -> weekend')
elif number in days:
    print(f'{number} -> working day')
else:
    print('null')
