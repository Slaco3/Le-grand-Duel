from abc import ABC
import random


class Character(ABC):
    def __init__(self, player_number, user_name):
        self.player_number = player_number
        self.user_name = user_name

    def regular_attack(self, other):
        attack_is_succes = random.choice((True, True, False))
        damages = random.randint(80,100)
        if attack_is_succes:
            other.pv -= damages
        else:
            damages = 0
        return damages
    

class Warrior(Character):
    def __init__(self, player_number, user_name):
        super().__init__(player_number, user_name)
        self.pv = 300
        self.valid_actions = ["regular attack", "safe attack"]

    def safe_attack(self, other):
        damages = random.randint(40,70)
        other.pv -= damages
        return damages


class Barbarian(Character):
    def __init__(self, player_number, user_name):
        super().__init__(player_number, user_name)
        self.pv = 500
        self.fury_mode = False
        self.valid_actions = ["regular attack", "fury mode"]

    def entering_in_fury(self):
        self.fury_mode = True
        self.pv -= 70
        self.valid_actions.remove("fury mode")
        self.valid_actions.append("fury attack")

    def attack_with_fury(self, other):
        if self.fury_mode == False:
            return 0
        damages1 = self.regular_attack(other)
        damages2 = self.regular_attack(other)
        all_damages = damages1 + damages2
        return damages1, damages2, all_damages
    

class Cleric(Character):
    def __init__(self, player_number, user_name):
        super().__init__(player_number, user_name)
        self.pv = 200
        self.valid_actions = ["regular attack", "heal"]

    def healing(self):
        pv_restoration = random.randint(40, 70)
        if pv_restoration + self.pv < 200:
            self.pv += pv_restoration    
        else:
            pv_restoration = 200 - self.pv
            self.pv = 200
        return pv_restoration

    

