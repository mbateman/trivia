from trivia import Game

from random import randrange, seed




for counter in range(1, 1000):
    seed(counter)

    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        if not not_a_winner: break
