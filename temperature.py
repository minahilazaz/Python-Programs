# (32°F − 32) × 5/9 = 0°C  Fahrenheit to Celsius
# (0°C × 9/5) + 32 = 32°F  Celsius to Fahrenheit

celsius = float(input('Enter number for celsius'))

fahrenheit = float(input('Enter number for fahrenheit'))

f  = (fahrenheit -32)*5/9
c = (celsius *9/5) + 32
print(f"Fahrenheit to Celsius {f} ")

print(f"Celsius to Fahrenheit {c}")