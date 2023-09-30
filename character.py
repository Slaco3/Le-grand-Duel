from abc import ABC, abstractmethod
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

    def safe_attack(self, other):
        damages = random.randint(40,70)
        other.pv -= damages
        return damages


class Barbarian(Character):
    def __init__(self, player_number, user_name):
        super().__init__(player_number, user_name)
        self.pv = 500
        self.fury_mode = False

    def entering_in_fury(self):
        self.fury_mode = True
        self.pv -= 40

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

    def healing(self):
        pv_restoration = random.randint(40, 70)
        self.pv += pv_restoration
        if self.pv > 200:
            self.pv = 200
        return pv_restoration


if __name__ == "__main__":
    warrior = Warrior(1, "Nicolas")
    barbarian = Barbarian(2, "Claire")
    cleric = Cleric(3, "Baptiste")
    
    # print("pv avant attaque :", barbarian.pv)
    # damage = warrior.regular_attack(barbarian)
    # print("damage :", damage)
    # print("pv après attaque", barbarian.pv)
    # if damage:
    #     print(True)
    # else:
    #     print(False)
    
    # cleric.pv = 50
    # print("pv avant",cleric.pv)
    # pv_restoration = cleric.healing()
    # print("pv après",cleric.pv)
    # print("pv récupérés", pv_restoration)

    # print("fury avant :", barbarian.fury_mode)
    # barbarian.entering_in_fury()
    # print("fury après:", barbarian.fury_mode)
    # print("warrior pv avant", warrior.pv)
    # tuple_damages = barbarian.attack_with_fury(warrior)
    # print("différents damages", tuple_damages)
    # print("warrior pv après", warrior.pv)


    

