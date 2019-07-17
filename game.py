import random

class Game:
    def __init__(self):
        self.answer = random.sample(range(0, 10), 4)
    def guess(self, arr):
        bulls = 0 # Right position
        cows = 0 # Wrong position
        for i in range(len(self.answer)):
            if self.answer[i] == arr[i]:
                bulls += 1
            if arr[i] in self.answer:
                cows += 1
        cows -= bulls
        return {'bulls': bulls, 'cows': cows, 'won': (str(self.answer) == str(arr))}
