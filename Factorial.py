def fact(n):
    if n == 0:
        return 1  
    else:
        return n * fact(n - 1)  # Recursive call to compute factorial

num = int(input('Enter the number: '))  
print('Factorial is:', fact(num))  
