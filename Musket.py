from Unit import Unit



class Musket(Unit):
    def __init__(self):
        self.name = "Musket"
        self.max_action_points = 2
        self.action_points = self.max_action_points
        self.max_hp = 10
        self.current_hp = self.max_hp
        self.dmg = 3

    def attack(self, target):
        if self.action_points > 0:  # daca poate sa faca mutare
            self.action_points = self.action_points - 1
            if target.get_name() == "Musket":
                target.current_hp = target.current_hp - self.dmg
                return self.dmg
            elif target.get_name() == "Cav":
                target.current_hp = target.current_hp - (self.dmg - 1)
                return self.dmg - 1
            elif target.get_name() == "Halb":
                target.current_hp = target.current_hp - self.dmg
                return self.dmg
        else:
            return -1


