# task 4


import sys

class Player:

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score
    
    def __bool__(self):
        return bool(self.score)

    def __str__(self):
        return f'{self.name=}, {self.score=}'


# считывание списка из входного потока (эту строчку и список lst_in не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
"Балакирев; 34; 2048",
"Mediel; 27; 0",
"Влад; 18; 9012",
"Nina P; 33; 0",
]

players = []
for line in lst_in:
    name, old, score = line.split('; ')
    players.append(Player(name, int(old), int(score)))

players.filter(bool)

print(*players)

