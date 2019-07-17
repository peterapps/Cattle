import game
import random

class Solver:
    def __init__(self, g):
        self.game = g
        self.known = [None] * 4
    def random_with_known(self):
        selection = list(range(0, 10))
        for i in range(4):
            if self.known[i] is not None:
                selection.remove(self.known[i])
        last_guess = random.sample(selection, 4)
        for i in range(4):
            if self.known[i] is not None:
                last_guess[i] = self.known[i]
        return last_guess
    def print_known(self):
        print(' '.join(['_' if x == None else str(x) for x in self.known]))
    def solve(self):
        total_guesses = 0
        thought = False
        #self.print_known()
        last_guess = self.random_with_known()
        while True:
            if (not thought) and (not None in self.known):
                #print('I think the answer is ' + ''.join([str(x) for x in g.answer]))
                thought = True
                print(self.game.guess(self.known))
            total_guesses += 1
            last_guess = self.random_with_known()
            last_result = self.game.guess(last_guess)
            if not last_result['won']:
                if last_result['bulls'] > 0: # Something in the right position
                    # Figure out what is in the correct position
                    for i in range(4):
                        if self.known[i] is not None: continue
                        test = [-1] * 4
                        test[i] = last_guess[i]
                        total_guesses += 1
                        if self.game.guess(test)['bulls'] > 0:
                            self.known[i] = last_guess[i]
                            #self.print_known()
                            break
                if last_result['cows'] > 0: # Something but in the wrong position
                    # Test every position
                    for i in range(4):
                        if self.known[i] is not None: continue
                        for j in range(4):
                            test = [-1] * 4
                            test[j] = last_guess[i]
                            total_guesses += 1
                            if self.game.guess(test)['bulls'] > 0:
                                self.known[j] = last_guess[i]
                                #self.print_known()
                                break
            else:
                break
        return (last_guess, total_guesses)

if __name__ == '__main__':
    iterations = []
    for i in range(10000):
        s = Solver(game.Game())
        answers, guesses = s.solve()
        iterations.append(guesses)
    print('Average # of guesses: {}'.format(round(sum(iterations) / len(iterations))))
