import game

g = game.Game()

while True:
    user = input('Enter your guess: ')
    if user == '?':
        print('You give up! The answer was {}'.format(g.answer))
        break
    result = g.guess([int(x) for x in user])
    if result['won']:
        print('Correct')
        break
    else:
        print('{} bulls, {} cows'.format(result['bulls'], result['cows']))
