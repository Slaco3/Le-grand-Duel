class View:
    player_number = 0

    def prompt_player_user_name(self):
        self.player_number += 1
        user_name = ""
        while user_name == "":
            user_name = input(f"Joueur {View.player_number}, rentres ton pseudo : ")
        return user_name
    
    def prompt_player_character_class(self, player_user_name):
        valid_characters_classes = ("guerrier", "barbare", "clerc")
        player_class_choice = input(f"{player_user_name}, rentres le nom de la classe de ton personnage (guerrier, clerc ou barbare) : ")
        if player_class_choice.lower().strip() in valid_characters_classes:
            return player_class_choice.lower().strip()
        else:
            return self.prompt_player_character_class(player_user_name)

















if __name__ == '__main__':
    view = View()
    user_name = view.prompt_player_user_name()
    player_class = view.prompt_player_character_class(user_name)

    print(player_class)

