from models.character import Barbarian, Cleric, Warrior


class View:
    player_number = 0
    game_turn = 0

    def display_rules(self):
        print()
        print("*" *119)
        print("                                        JEU : LE GRAND DUEL   ( 2 joueurs )")                                                     
        print("*" *119)

        print()       
        print("Bienvenue dans l'arène ! Voici les règles du jeu :  ")   
        print()
        print("Vous avez le choix entre 3 classes de personnages : guerrier, barbare ou clerc.")                                                           
        print("Le barbare est le personnage le plus résistant.")     
        print("Il peut entrer en furie pour infliger des dégâts supplémentaires à son adversaire mais cela lui coûte des PV.")     
        print("Le Clerc possède peu de points de vies mais il a la capacité de se soigner.")
        print(f"Il ne peut pas récupérer plus de points de vie que sa santé maximale ({Cleric.MAX_PV} PV).")     
        print("Quant au guerrier c'est un personnage équilibré.")     
        print("Il a la particularité de pouvoir lancer une attaque peu puissante mais fiable.")     
        print()
        print("Chaque joueur joue à tour de rôle. L'objectif est de réduire les PV de l'adversaire à zéro.  ")     
        print("")           
        print("*" *119)          
        
    def prompt_player_user_name(self):
        self.player_number += 1
        user_name = ""
        while user_name == "":
            user_name = input(f"Joueur {self.player_number}, rentres ton pseudo : ")
        return user_name
    
    def prompt_player_character_class(self, player_user_name):
        valid_characters_classes = ("guerrier", "barbare", "clerc")
        player_class_choice = input(f"{player_user_name}, rentres le nom de la classe de ton personnage (guerrier, clerc ou barbare) : ")
        print()
        if player_class_choice.lower().strip() in valid_characters_classes:
            return player_class_choice.lower().strip()
        else:
            return self.prompt_player_character_class(player_user_name)

    def show_player_presentation(self, player):
        if isinstance(player, Warrior):
            print(f"{player.user_name} tu es un fier Guerrier !")
        if isinstance(player, Cleric):
            print(f"{player.user_name} tu incarnes la sagesse du Clerc !")
        if isinstance(player, Barbarian):
            print(f"{player.user_name} tu es un Féroce Barbare !")

    def display_start_of_turn(self):
        self.game_turn += 1
        print("*" * 119)
        print(" " * 45, "---", "TOUR", self.game_turn, "---")
        print()

    def display_players_pv(self, player1, player2):
        print(player1.user_name, ":", player1.pv, "PV")
        print(player2.user_name, ":", player2.pv, "PV")
        print()

    def prompt_for_player_action(self, valid_actions, player):
        print(f"{player.user_name} à toi de jouer !".upper())
        print()
        print("Attaques :")
        for action in valid_actions:
            print("-", action)
        print()
        player_choice = ""
        while not player_choice.lower().strip() in valid_actions:
            player_choice = input(player.user_name + ", rentres l'attaque que tu souhaites envoyer : ")
        return player_choice.lower().strip()
    
    def display_message_regular_attack(self, damages, player, other):
        print()
        if damages:
                print(f"{player.user_name} ton attaque a réussi ! Tu as infligé {damages} points de dégâts à {other.user_name}!")          
        else:
                print(f"{player.user_name} ton attaque a échoué !")

    def display_heal_attack(self, player, pv_restoration):
         print()
         print(f"{player.user_name} tu as récupéré {pv_restoration} PV, il te reste donc {player.pv} PV au total.")

    def display_furie_attack(self, all_damages, player):
        print()
        damages1 = all_damages[0]
        damages2 = all_damages[1]
        damages = all_damages[2]
        if damages1:
            print(f"{player.user_name} le premier assault de ton attaque furie est un succès ! Tu infliges {damages1} points de dêgats à ton adversaire !")
        else:
            print(f"{player.user_name} le premier assault de ton attaque furie a échoué..." )
        if damages2:
            print(f"Le second assault de ton attaque furie est un succès ! Tu infliges {damages2} points de dêgats à ton adversaire !")
        else:
            print(f"Lle second assault de ton attaque furie a échoué..." )

        if damages:
            print(f"En tout, tu as infligé {damages} points de dêgats à ton adversaire.")

    def display_entering_in_furie_mode(self, player):
        print()
        print(f"{player.user_name} tu rentres en mode furie ! Tu t'infliges {Barbarian.FURY_AUTO_DAMAGES} points de dégâts et tu débloques l'attaque furie !")

    def display_death_of_furie(self):
        print("Malheuresement, la blessure que tu t'es infligé a eu raison de toi... ")

    def display_separator_bar(self):
        print("-"*30)
        print()

    def show_winner(self, winner):
        print(f"FELICIATIONS {winner.user_name} tu remportes la bataille ! " )



    