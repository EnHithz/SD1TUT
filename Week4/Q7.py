import random
#asighning variables
doubles_count = 0
#process
for _ in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        doubles_count += 1

print(f'Out of 100 rolls, you rolled {doubles_count} doubles.')