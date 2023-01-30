import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

average = total / 5

print('Thrown', dice1, dice2, dice3, dice4, dice5)
print('Total', total)
print(f'Total {total}')

print('Average', average)

if total < 10:
    print('loser')
elif total >= 10 and total < 20:
    print('Not bad')
else:
    print('Great')











# dice = []
# for _ in range(5):
#     dice.append( random.randint(1, 6) )
#
# print('Thrown', dice)
# print('Total', sum(dice))


# dice = [random.randint(1, 6) for _ in range(20)]
#
# print('Thrown', dice)
# print('Total', sum(dice))
