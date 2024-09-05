from Battlefield import Battlefield
from Unit import Unit

import Agent.Algoritmi


class Game:

    def start(self):
        init_state = ['C', 'H', 'M', 'H', 'M', 'C', 'H', 'M', 'M', 'M']
        game = Battlefield(init_state)
        game.regroup()
        game.print()
        final = game.endgame()
        while final == 0:
            unit1 = input("Your unit : ")
            if int(unit1) == -1:
                game.endturn()
            elif int(unit1) == -2:
                final = 2
            else:
                unit2 = input("Other unit : ")
                game.action(int(unit1), int(unit2))
                game.print()
                final = game.endgame()
        if final == 1:
            print("WIN!")
        elif final == 2:
            print("LOSE!")
        print("Turns: ", game.turn + 1)
        print("Actions: ", game.nrAction)


def main():
    Game().start()

    return 0


if __name__ == "__main__":
    main()
