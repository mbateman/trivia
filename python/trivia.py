#!/usr/bin/env python

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.coinTally = [0] * 6
        self.in_penalty_box = [0] * 6
        
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False
        
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))
    
    def create_rock_question(self, index):
        return "Rock Question %s" % index
    
    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.coinTally[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        
        print player_name + " was added"
        print "They are player number %s" % len(self.players)
        
        return True
    
    @property
    def how_many_players(self):
        return len(self.players)

    def is_odd(self, roll):
        return roll % 2 != 0

    def roll(self, roll):
        print "%s is the current player" % self.players[self.current_player]
        print "They have rolled a %s" % roll
        
        if self.in_penalty_box[self.current_player]:
            if self.is_odd(roll):
                self.is_getting_out_of_penalty_box = True
                print "%s is getting out of the penalty box" % self.players[self.current_player]
            else:
                print "%s is not getting out of the penalty box" % self.players[self.current_player]
                self.is_getting_out_of_penalty_box = False

        if self.can_play():
            self.places[self.current_player] = self.places[self.current_player] + roll
            self.board_size = 12
            if self.places[self.current_player] >= self.board_size:
                self.wrap_board()
            
            print self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player])
            print "The category is %s" % self._current_category
            self._ask_question()

    def wrap_board(self):
        self.places[self.current_player] = self.places[self.current_player] - self.board_size

    def can_play(self):
        return not self.in_penalty_box[self.current_player] or self.is_getting_out_of_penalty_box

    def _ask_question(self):
        if self._current_category == 'Pop': print self.pop_questions.pop(0)
        if self._current_category == 'Science': print self.science_questions.pop(0)
        if self._current_category == 'Sports': print self.sports_questions.pop(0)
        if self._current_category == 'Rock': print self.rock_questions.pop(0)
    
    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if not self.is_getting_out_of_penalty_box:
                self.next_player()
                return True

            else:

                print 'Answer was correct!!!!'
                self.update_coin_tally()

                winner = self._did_player_win()
                self.next_player()

                return winner


        else:

            print "Answer was corrent!!!!"
            self.update_coin_tally()

            winner = self._did_player_win()
            self.next_player()

            return winner

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

    def update_coin_tally(self):
        self.coinTally[self.current_player] += 1
        print self.players[self.current_player] + \
              ' now has ' + \
              str(self.coinTally[self.current_player]) + \
              ' Gold Coins.'

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print self.players[self.current_player] + " was sent to the penalty box"
        self.in_penalty_box[self.current_player] = True

        self.next_player()
        return True
    
    def _did_player_win(self):
        return not (self.coinTally[self.current_player] == 6)

    def play(self):
        not_a_winner = False
        self.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = self.wrong_answer()
        else:
            not_a_winner = self.was_correctly_answered()

        return not_a_winner


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        not_a_winner = game.play()
        
        if not not_a_winner: break
