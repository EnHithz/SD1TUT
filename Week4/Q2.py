total = 0 # sum of scores
count = 0 # number of scores entered

#get the inputs from the user
score = int(input('Enter your scores, (Enter -9 to end) : '))

#process
if score == -9 and count == 0:
    print('enter at least one score')
else:
    while(score != -9):
        total += score
        count += 1
        score = int(input('Enter your next score : '))


    average = float(total)/count
    print('Class average is', average)


    