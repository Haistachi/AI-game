import numpy
from Halb import Halb
from Cav import Cav
from Musket import Musket
from Unit import Unit
import random
import string


class Battlefield:

    def __init__(self, init_state=None):
        self.battlefield = []
        self.init_state = []
        if init_state is not None:
            self.fill_battlefield(init_state)
        else:
            self.fill_battlefield_random()
        self.turn = 0
        self.nrAction = 0
        self.team1_unit_lost = False
        self.team2_unit_lost = False
        self.prev_ac = (0, 0)

    def fill_battlefield(self, init_state):
        for i in range(10):
            if init_state[i] == 'M':
                self.battlefield.append(Musket())
            elif init_state[i] == 'H':
                self.battlefield.append(Halb())
            elif init_state[i] == 'C':
                self.battlefield.append(Cav())
            elif init_state[i] == '_':
                self.battlefield.append(None)

    def fill_battlefield_random(self):
        chars = ['M', 'H', 'C', '_']
        init_state = random.choices(chars, weights=[1, 1, 1, 1], k=10)
        self.fill_battlefield(init_state)

    """def print(self):
        for i in range(5):
            if self.battlefield[i] is None:
                print(str(i) + " : _")
            else:
                self.battlefield[i].id_print(i)
        print("|-------------------------|")
        for i in range(5, 10):
            if self.battlefield[i] is None:
                print(str(i) + " : _")
            else:
                self.battlefield[i].id_print(i)"""

    def print(self):
        string = []
        for i in range(0, 10, 1):
            if i == 5:
                string.append("<|>")
            if self.battlefield[i] is None:
                string.append("_")
            else:
                string.append(self.battlefield[i].simple_print())
        print(string)

    def action(self, pos1, pos2):
        self.prev_ac = (pos1, pos2)
        self.team1_unit_lost = False
        self.team2_unit_lost = False
        if pos1 == -1:
            self.endturn()
        elif pos1 > 9 or pos2 > 9:
            print("You must select valid targets!")
        elif (self.battlefield[pos1] is None) or (self.battlefield[pos2] is None):
            print("You must select valid targets!")
        elif self.battlefield[pos1].action_points == 0:
            print("You selected a extenuated unit!")
        elif pos1 > 4:
            print("You can't command an enemy unit!")
        else:
            if (pos1 < 5 and pos2 < 5) or (pos1 > 4 and pos2 > 4):
                self.swap_unit(pos1, pos2)
            elif pos1 < 5 and pos2 > 4:
                self.battlefield[pos1].attack(self.battlefield[pos2])
                self.battlefield[pos2].attack(self.battlefield[pos1]) #Adversarial contra-atac
                self.battlefield[pos2].inc_ap()
                kill = self.battlefield[pos1].dead()
                if kill:
                    self.battlefield[pos1] = None
                    self.team1_unit_lost = True
                kill = self.battlefield[pos2].dead()
                if kill:
                    self.battlefield[pos2] = None
                    self.team2_unit_lost = True
                self.regroup()
            self.nrAction += 1

    def regroup(self):
        for i in range(4, 0, -1):
            if self.battlefield[i] is None:
                for j in range(i - 1, -1, -1):
                    if self.battlefield[j] is not None:
                        self.battlefield[j], self.battlefield[i] = self.battlefield[i], self.battlefield[j]
                        i -= 1

        for i in range(5, 9, 1):
            if self.battlefield[i] is None:
                for j in range(i + 1, 10, 1):
                    if self.battlefield[j] is not None:
                        self.battlefield[i], self.battlefield[j] = self.battlefield[j], self.battlefield[i]
                        i += 1

    def endturn(self):
        for i in range(10):
            if self.battlefield[i] is not None:
                self.battlefield[i].resett()
        self.regroup()
        self.turn += 1

    def endgame(self):
        win = 1
        lose = 1
        for i in range(5, 10, 1):
            if self.battlefield[i] is not None:
                win = 0
        for i in range(0, 5, 1):
            if self.battlefield[i] is not None:
                lose = 0
        if win == 0 and lose == 0:
            return 0  # jocu continua
        elif win == 1 and lose == 1:
            return 3  # impas
        elif win == 1:
            return 1  # castigi
        elif lose == 1:
            return 2  # pierzi

    def swap_unit(self, poz1, poz2):  # mutare intre doua unitati
        if (poz1 < 5 and poz2 < 5) or (poz1 > 4 and poz2 > 4):
            if abs(poz1 - poz2) == 1:
                if self.battlefield[poz1].can_move() and self.battlefield[poz2].can_move():
                    self.battlefield[poz1].dec_ap()
                    self.battlefield[poz2].dec_ap()
                    self.battlefield[poz1], self.battlefield[poz2] = self.battlefield[poz2], self.battlefield[poz1]
                else:
                    print("Not enough AP!")
            else:
                print("You can swap only neighbors!")
        else:
            print("You can't swap outside your team!")

    def __eq__(self, other):
        if self.nrAction != other.nrAction:
            return False
        elif self.turn != other.turn:
            return False
        else:
            for i in range(0, 10, 1):
                if self.battlefield[i] != other.battlefield[i]:
                    return False
        return True

    def result(self, action):
        x, y = action
        self.action(x, y)
        return self