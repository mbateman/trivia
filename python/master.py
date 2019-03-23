from trivia import Game

from random import randrange, seed


def play(players, seedValue):
    seed(seedValue)

    not_a_winner = False

    game = Game()

    for player in players:
        game.add(player)

    while True:
        
        not_a_winner = game.play()
        
        if not not_a_winner: break


# try to play with one player only
play(["Chet"], 0)

# 1000 iterations
for counter in range(1, 1000):
    play(['Chet', 'Pat', 'Sue'], counter)
