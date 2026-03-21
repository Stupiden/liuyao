from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        runner = cls()
        c = 0

        while True:
            print("Round {}\n".format(runner.round))

            # 每轮重新 roll
            for die in runner.dice:
                die.roll()
                print(die.show())

            guess = int(input("What is your guess?: "))

            if guess == runner.answer():
                print("Correct")
                runner.wins += 1
                c += 1
            else:
                print("Wrong")
                print("Answer:", runner.answer())
                runner.loses += 1
                c = 0

            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won!")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                i_just_throw_an_exception()
