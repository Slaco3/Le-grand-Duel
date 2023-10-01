import time

from character import Warrior, Barbarian, Cleric


class Controller:
    def __init__(self, view):
        self.view = view

    def create_character_with_class_choice(self, class_choice, player_number, user_name):
        if class_choice == "guerrier":
            character = Warrior(player_number, user_name)
        if class_choice == "barbare":
            character = Barbarian(player_number, user_name)
        if class_choice == "clerc":
            character = Cleric(player_number, user_name)
        return character

    def get_players(self):
        user_name_player1 = self.view.prompt_player_user_name()
        class_choice_player1 = self.view.prompt_player_character_class(user_name_player1)
        player1 = self.create_character_with_class_choice(class_choice_player1, 1, user_name_player1)
        self.player1 = player1

        user_name_player2 = self.view.prompt_player_user_name()
        class_choice_player2 = self.view.prompt_player_character_class(user_name_player2)
        player2 = self.create_character_with_class_choice(class_choice_player2, 2, user_name_player2)
        self.player2 = player2

    def setup_turn(self):
        self.view.display_start_of_turn()
        self.view.display_players_pv(self.player1, self.player2)

    def launch_warrior_actions(self, player, other, attack_name):
        if attack_name == "regular attack":
            damages = player.regular_attack(other)
            self.view.display_message_regular_attack(damages, player, other)
        if attack_name == "safe attack":
            damages = player.safe_attack(other) 
            self.view.display_message_regular_attack(damages, player, other)

    def launch_cleric_actions(self, player, other, attack_name):
        if attack_name == "regular attack":
            damages = player.regular_attack(other)
            self.view.display_message_regular_attack(damages, player, other)
        if attack_name ==  "heal":
            pv_restoration = player.healing()
            self.view.display_heal_attack(player, pv_restoration)

    def launch_barbarian_actions(self, player, other, attack_name):
        if attack_name == "regular attack":
            damages = player.regular_attack(other)
            self.view.display_message_regular_attack(damages, player, other)
        if attack_name == "fury mode":
            damages = player.entering_in_fury() 
            self.view.display_entering_in_furie_mode(player)
            if player.pv < 0:
                self.view.display_death_of_furie()
        if attack_name == "fury attack":
            all_damages = player.attack_with_fury(other)
            self.view.display_furie_attack(all_damages, player, other)
     
    def launch_attack(self, player, other, attack_name):
        if isinstance(player, Warrior):
            self.launch_warrior_actions(player, other, attack_name)
        if isinstance(player, Cleric):
            self.launch_cleric_actions(player, other, attack_name)
        if isinstance(player, Barbarian):
            self.launch_barbarian_actions(player, other, attack_name)

    def one_player_loose(self):
        if self.player1.pv < 0 or self.player2.pv < 0:
            return True

    def play_entire_turn(self):
        player_choice = self.view.prompt_for_player_action(self.player1.valid_actions, self.player1)
        self.launch_attack(self.player1, self.player2,player_choice)
        time.sleep(3)
        if self.one_player_loose():
            return False
     
        self.view.display_players_pv(self.player1, self.player2)
   
        player_choice = self.view.prompt_for_player_action(self.player2.valid_actions, self.player2)
        self.launch_attack(self.player2, self.player1, player_choice)
        time.sleep(3)
        if self.one_player_loose():
            return False
        return True

    def determining_winner(self):
        if self.player1.pv > self.player2.pv:
            return self.player1
        return self.player2

    def run(self):
        self.view.display_rules()
        self.get_players()
        while True:
            self.setup_turn()
            if not self.play_entire_turn():
                break
        self.view.display_players_pv(self.player1, self.player2)
        winner = self.determining_winner()
        self.view.show_winner(winner)
      
        
