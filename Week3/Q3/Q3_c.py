Cost = float(input('Enter the cost of the meal : '))
print(' Satisfaction level 1 is totally satisfied 2 is satisfied 3 is dissatisfied\n')
State = int(input('Enter satisfaction level\n '))
if State == 1:
    Tip = Cost * 0.2
    print('Tip is ',Tip)
elif State == 2:
    Tip = Cost * 0.15
    print('Tip is ',Tip)
elif State == 3:
    Tip = Cost * 0.1
    print('Tip is ',Tip)
else:
    print(' Invalid ')