print('Enter 1 to convert Celsius to Fahrenheit or enter 2 to convert Fahrenheit to Celsius\n')
temp = int(input('Enter your choice 1 or 2 : '))
if temp == 1:
    c = float(input('Enter temperature in Celsius: '))
    f = (c * 1.8) + 32
    print(f'The temperature is Fahrenheit {f} ')
elif temp == 2:
    f = float(input('Enter temperature in Fahrenheit: '))
    c = (f -32)/1.8
    print(f'The temperature is Celcius {c}')
else:
    print('Invalid option enterd')