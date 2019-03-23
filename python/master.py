from trivia import Game

from random import randrange, seed


def play(players, seedValue):
    seed(seedValue)

    not_a_winner = False

    game = Game()

    for player in players:
        game.add(player)

    while True:
        
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        if not not_a_winner: break


# try to play with one player only
play(["Chet"], 0)

# 1000 iterations
for counter in range(1, 1000):
    play(['Chet', 'Pat', 'Sue'], counter)
