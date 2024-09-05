class Unit:

    def __init__(self, name, max_action_points, max_hp):
        self.name = name
        self.max_action_points = max_action_points
        self.action_points = max_action_points
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.dmg = 3

    def reset(self):
        self.action_points = self.max_action_points
        self.current_hp = self.max_hp

    def resett(self):
        self.action_points = self.max_action_points

    def show_stats(self):
        stats = []
        stats.append(self.name)
        stats.append(self.max_action_points)
        stats.append(self.action_points)
        stats.append(self.max_hp)
        stats.append(self.current_hp)
        return stats

    def attack(self, target):
        if self.action_points > 0:  # daca poate sa faca mutare
            self.action_points = self.action_points - 1
            if target.name() == "Musket":
                target.current_hp = target.current_hp - self.dmg
                return self.dmg
            elif target.name() == "Cav":
                target.current_hp = target.current_hp - self.dmg
                return self.dmg
            elif target.name() == "Halb":
                target.current_hp = target.current_hp - self.dmg
                return self.dmg
        else:
            return -1

    def dead(self):
        if self.current_hp <= 0:  # daca moare
            return True
        else:
            return False

    def can_move(self):
        if self.action_points > 0:  # daca poate sa faca mutare
            return True
        else:
            return False

    def dec_ap(self):
        self.action_points -= 1

    def inc_ap(self):
        self.action_points += 1

    def print(self):
        print("(" + self.name + ", AP:" + str(self.action_points) + "/" + str(self.max_action_points) + "," + str(
            self.current_hp) + "/" + str(self.max_hp) + "," + str(self.dmg) + ")")

    def simple_print(self):
        string = [self.name + " AP:" + str(self.action_points) + " HP:" + str(self.current_hp)]
        return string

    def id_print(self, pos):
        print(str(pos) + " : " + "(" + self.name + ", AP:" + str(self.action_points) + "/" + str(
            self.max_action_points) + "," + str(
            self.current_hp) + "/" + str(self.max_hp) + "," + str(self.dmg) + ")")

    def get_name(self):
        return self.name

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif (self is None) != (other is None):
            return False
        elif self.action_points != other.action_points:
            return False
        elif self.name != other.name:
            return False
        elif self.current_hp != other.current_hp:
            return False
        return True
