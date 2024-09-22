"""Write a python program which will keep  adding a stream of numbers inputed by the users.The adding stop as soon as user press q on the keyboard"""

sum = 0
orders = [] 

while(True):
    userInput = input('Enter a number (or "q/Q" to quit): \n')
    
    if (userInput != 'q' and userInput != 'Q'):
        order = int(userInput)  
        orders.append(order)  
        sum += order  
        print(f"Order total so far: {sum}")
    else:
        print(f"Your total bill is {sum}. Thank you for shopping with us!")
        print(f"All orders: {', '.join(map(str, orders))}")
        break

