num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the second number : '))
Opt = input('Enter the operation what you need : ')

try:
 if Opt == "+":
     Answer = num1 + num2
     print(Answer)
 elif Opt == "-":
     Answer = num1 - num2
     print(Answer)
 elif Opt == "*":
     Answer = num1 * num2
     print(Answer)
 elif Opt == "/":
     Answer =num1 / num2
     print(Answer)
 else:
     print("Error invalid operator")    
except Exception as e:
        print(f"error: {str(e)}")
