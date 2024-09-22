# Read the currency conversion rates from the file
with open('currany.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.strip().split("\t")  
    currencyDict[parsed[0]] = float(parsed[1])  

print(currencyDict)  

amount = float(input("Enter the amount you want to convert (in PKR): \n")) 

print("Enter the name of the currency you want to convert the amount to. Available options: ")
[print(item) for item in currencyDict.keys()] 

currency = input('Please enter one of these values: ')

if currency in currencyDict:
    converted_amount = amount * currencyDict[currency]
    print(f"{amount} PKR is equal to {converted_amount} {currency}.")
else:
    print("The currency you entered is not available.")
