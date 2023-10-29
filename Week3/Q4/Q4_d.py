Marks = int(input('Enter your marks : '))
if  Marks < 0 or Marks > 100:
    print('Your exam marks are invalid')
else:
    if Marks >= 70:
        print('Exceptional result!')
    elif Marks >= 40:
        print('Satisfactory result!')
    else:
        print('You have failed')