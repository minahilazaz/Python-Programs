# Find Largest Number: Write a program to find the largest number among three numbers.
number1 = int(input('Enter number 1 '))
number2 = int(input('Enter nunber 2 '))
number3 = int(input('Enter number 3 '))

if number1>=number2 and number1>=number3:
    print('Number 1 is greater ')
elif number2>=number1 and number2>=number3:
    print('Number 2 is greater ')
else:
    print('Number 3 is greater ')