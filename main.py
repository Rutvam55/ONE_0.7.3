import random
import os
import pwinput
from CORE.link import set_player, Math, Francais, Deutsch, ScNat, Anglais, Geo
from CORE.funk import sauvegarder_auto, charger_sauvegarde, ajouter_joueur, Level_up, selectionner_joueur, controller_int, DEFAULT_SAVE_FILE
from CORE.langue import langue
from KI.ia import IA

VERSION = "0.9.0"

ia = IA()


def calculate_percentage(correct_answers, total_questions):
    """Calculate percentage of correct answers"""
    return (correct_answers / total_questions) * 100 if total_questions > 0 else 0


# ===============================
#       BUTTON CLASS
# ===============================

class Button:
    """Button management for subject selection"""
    
    def __init__(self):
        self.state = {
            "scnat_1": False,
            "scnat_1_1": False,
            "scnat_1_2": False,

            "francais_2": False,
            "francais_2_1": False,
            "francais_2_2": False,

            "deutsch_3": False,
            "deutsch_3_1": False,
            "deutsch_3_2": True,

            "anglais_4": False,
            "anglais_4_1": False,
            "anglais_4_2": False,

            "math_5": False,
            "math_5_1": False,

            "geo_6": False,
        }

    def toggle(self, name):
        """Toggle button state"""
        if name in self.state:
            self.state[name] = not self.state[name]
        else:
            print(f"[ERROR] '{name}' does not exist.")

    def collect(self):
        """Collect active menu choices"""
        menu = []
        choices_scnat = []
        choices_francais = []
        choices_deutsch = []
        choices_anglais = []
        choices_math = []
        choices_geo = []
        
        # -------- SCNAT --------
        if self.state["scnat_1"]:
            menu.append("ScNat")
            if self.state["scnat_1_1"]:
                choices_scnat.append("element")
            if self.state["scnat_1_2"]:
                choices_scnat.append("ordnungszahl")

        # -------- FRANCAIS --------
        if self.state["francais_2"]:
            menu.append("Francais")
            if self.state["francais_2_1"]:
                choices_francais.append("voc dif")
            if self.state["francais_2_2"]:
                choices_francais.append("verb")

        # -------- DEUTSCH --------
        if self.state["deutsch_3"]:
            menu.append("Deutsch")
            if self.state["deutsch_3_1"]:
                choices_deutsch.append("Merkmale von Kurzgeschichten (Einfach)")
            if self.state["deutsch_3_2"]:
                choices_deutsch.append("Merkmale von Kurzgeschichten (Schwer)")

        # -------- ANGLAIS --------
        if self.state["anglais_4"]:
            menu.append("Anglais")
            if self.state["anglais_4_1"]:
                choices_anglais.append("voc easy")
            if self.state["anglais_4_2"]:
                choices_anglais.append("voc impossible")

        # -------- MATH --------
        if self.state["math_5"]:
            menu.append("Math")
            if self.state["math_5_1"]:
                choices_math.append("base")

        # -------- GEO --------
        if self.state["geo_6"]:
            menu.append("Geo")
        
        return menu, choices_scnat, choices_francais, choices_deutsch, choices_anglais, choices_math, choices_geo


# ===============================
#       MAIN PROGRAM
# ===============================

buttons = Button()
running = True
connection = False

while running:

    data = charger_sauvegarde(DEFAULT_SAVE_FILE)

    # =================================
    #  LOGIN
    # =================================
    while not connection:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== ONE ===")
        password_correct = False
        attempts = 3

        if attempts == 0 and password_correct is False:
            print("Too many incorrect attempts. Exiting.")
            exit()

        username = input("Enter your name.\n> ")
        if not username:
            print("Username cannot be empty.")
            input("Press ENTER to continue...")
            continue
            
        password = pwinput.pwinput(prompt="Enter your password.\n> ", mask='#')
        if not password:
            print("Password cannot be empty.")
            input("Press ENTER to continue...")
            continue
            
        player, password_correct = selectionner_joueur(data, username, password)

        if player is None:
            create = input("Player not found. Create one? (y/n) ")

            if create.lower() == "y":
                if ajouter_joueur(data, username, password):
                    player = data["joueurs"][username]
                    sauvegarder_auto(data, DEFAULT_SAVE_FILE)
                else:
                    print("ERROR")
                    continue
            else:
                while password_correct is False and attempts > 0:
                    username = input("Enter your name.\n> ")
                    password = pwinput.pwinput(prompt="Enter your password.\n> ", mask='#')
                    player, password_correct = selectionner_joueur(data, username, password)
                    if password_correct is True:
                        break
                    attempts -= 1
                    print(f"Password: {password}\nAttempts remaining: {attempts}/3")
                if attempts == 0 and password_correct is False:
                    print("Too many incorrect attempts. Exiting.")
                    exit()

        connection = True
        set_player(player)

    # ===============================
    #       LANGUAGE
    # ===============================
    L = langue(username, player, VERSION, buttons.state)

    # ===============================
    #       PLAYER CLASS
    # ===============================
    class Player:
        """Player statistics class"""
        def __init__(self, player_data):
            self.name = player_data["nom"]
            self.password = player_data["mot_de_passe"]
            
            # ScNat
            self.scnat_level = player_data["ScNat"]["Level_ScNat"]
            self.scnat_xp = player_data["ScNat"]["xp_ScNat"]
            self.scnat_max_xp = player_data["ScNat"]["Max_xp_ScNat"]
            
            # Francais
            self.francais_level = player_data["Francais"]["Level_Francais"]
            self.francais_xp = player_data["Francais"]["xp_Francais"]
            self.francais_max_xp = player_data["Francais"]["Max_xp_Francais"]
            
            # Deutsch
            self.deutsch_level = player_data["Deutsch"]["Level_Deutsch"]
            self.deutsch_xp = player_data["Deutsch"]["xp_Deutsch"]
            self.deutsch_max_xp = player_data["Deutsch"]["Max_xp_Deutsch"]
            
            # Anglais
            self.anglais_level = player_data["Anglais"]["Level_Anglais"]
            self.anglais_xp = player_data["Anglais"]["xp_Anglais"]
            self.anglais_max_xp = player_data["Anglais"]["Max_xp_Anglais"]

            # Math
            self.math_level = player_data["Math"]["Level_Math"]
            self.math_xp = player_data["Math"]["xp_Math"]
            self.math_max_xp = player_data["Math"]["Max_xp_Math"]

            # Geo
            self.geo_level = player_data["Geo"]["Level_Geo"]
            self.geo_xp = player_data["Geo"]["xp_Geo"]
            self.geo_max_xp = player_data["Geo"]["Max_xp_Geo"]
            
            # Settings
            self.language = player_data["P"]["langue"]

    # ===============================
    #       MAIN MENU
    # ===============================
    while True:

        print(L["main.1.p"])
        choice = input(L["main.2.i"]).strip()

        # =======================================
        #         SETTINGS
        # =======================================
        if choice == "1":

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=========== SETTINGS ===========")

                def show(btn, txt):
                    """Show button state"""
                    state = "ON" if buttons.state[btn] else "OFF"
                    print(f"{txt} ({state})")

                show("scnat_1", "1. ScNat")
                show("scnat_1_1", "  1.1 Element Namen")
                show("scnat_1_2", "  1.2 Ordnungszahl")

                show("francais_2", "2. Francais")
                show("francais_2_1", "  2.1 Vocabulary (difficult)")
                show("francais_2_2", "  2.2 Verbs")

                show("deutsch_3", "3. Deutsch")
                show("deutsch_3_1", "  3.1 Kurzgeschichten (easy)")
                show("deutsch_3_2", "  3.2 Kurzgeschichten (hard)")

                show("anglais_4", "4. Anglais")
                show("anglais_4_1", "  4.1 Easy vocabulary")
                show("anglais_4_2", "  4.2 Impossible vocabulary")

                show("math_5", "5. Math")
                show("math_5_1", "  5.1 Base")

                show("geo_6", "6. Geography")

                print("\nq: Quit\nENTER to validate, or choose a button.")

                action = input("> ").strip()

                mapping = {
                    "1": "scnat_1",
                    "1.1": "scnat_1_1",
                    "1.2": "scnat_1_2",

                    "2": "francais_2",
                    "2.1": "francais_2_1",
                    "2.2": "francais_2_2",

                    "3": "deutsch_3",
                    "3.1": "deutsch_3_1",
                    "3.2": "deutsch_3_2",

                    "4": "anglais_4",
                    "4.1": "anglais_4_1",
                    "4.2": "anglais_4_2",

                    "5": "math_5",
                    "5.1": "math_5_1",

                    "6": "geo_6"
                }
                
                if action in mapping:
                    buttons.toggle(mapping[action])
                elif action == "":
                    break
                elif action.lower() == "q" or action.lower() == "quit":
                    print("Goodbye!")
                    running = False
                    exit()
                else:
                    print("Invalid choice.")
                    input("Press ENTER to continue...")
            
            # =======================================
            #         START GAMES
            # =======================================
            menu, choices_scnat, choices_francais, choices_deutsch, choices_anglais, choices_math, choices_geo = buttons.collect()
            
            if not menu:
                print("No games selected in settings.")
                input("Press ENTER to continue...")
                continue
            
            mode_choice = input("Select mode:\n1: Infinite\n2: Normal\n> ").strip().lower()
            
            # =====================================
            #            INFINITE MODE
            # =====================================
            if mode_choice in ["1", "infinite"]:
                streak = True
                question_num = 0
                
                while streak:
                    question_num += 1
                    selected_game = random.choice(menu)
                    
                    if selected_game == "ScNat":
                        exercise = ScNat()
                        score, xp, streak = exercise.menu_scnat(choices_scnat, question_num)
                    elif selected_game == "Francais":
                        exercise = Francais()
                        score, xp, streak = exercise.menu_francais(choices_francais, question_num)
                    elif selected_game == "Deutsch":
                        exercise = Deutsch()
                        score, xp, streak = exercise.menu_deutsch(choices_deutsch, question_num)
                    elif selected_game == "Anglais":
                        exercise = Anglais()
                        score, xp, streak = exercise.menu_anglais(choices_anglais, question_num)
                    elif selected_game == "Math":
                        exercise = Math()
                        score, xp, streak = exercise.menu_math(choices_math, question_num)
                    elif selected_game == "Geo":
                        exercise = Geo()
                        score, xp, streak = exercise.menu_geo(choices_geo, question_num)
                    else:
                        print("Game selection error.")
                        streak = False
                    
                    Level_up(player)
                    sauvegarder_auto(data, DEFAULT_SAVE_FILE)
                    os.system('cls' if os.name == 'nt' else 'clear')

            # =====================================
            #            NORMAL MODE
            # =====================================
            elif mode_choice in ["2", "normal"]:
                streak = True
                attempts = 5
                max_attempts = attempts
                score = 0
                question_num = 0
                
                question_num = controller_int(attempts, max_attempts, question_num, "How many questions do you want?")
                total_questions = question_num
                
                for i in range(question_num):
                    selected_game = random.choice(menu)
                    
                    if selected_game == "ScNat":
                        exercise = ScNat()
                        exercise_score, xp, streak = exercise.menu_scnat(choices_scnat, (i + 1))
                        score += exercise_score
                    elif selected_game == "Francais":
                        exercise = Francais()
                        exercise_score, xp, streak = exercise.menu_francais(choices_francais, (i + 1))
                        score += exercise_score
                    elif selected_game == "Deutsch":
                        exercise = Deutsch()
                        exercise_score, xp, streak = exercise.menu_deutsch(choices_deutsch, (i + 1))
                        score += exercise_score
                    elif selected_game == "Anglais":
                        exercise = Anglais()
                        exercise_score, xp, streak = exercise.menu_anglais(choices_anglais, (i + 1))
                        score += exercise_score
                    elif selected_game == "Math":
                        exercise = Math()
                        exercise_score, xp, streak = exercise.menu_math(choices_math, (i + 1))
                        score += exercise_score
                    elif selected_game == "Geo":
                        exercise = Geo()
                        exercise_score, xp, streak = exercise.menu_geo(choices_geo, (i + 1))
                        score += exercise_score
                    else:
                        print("Game selection error.")
                        streak = False
                    
                    Level_up(player)
                    sauvegarder_auto(data, DEFAULT_SAVE_FILE)
                    if i < question_num - 1:
                        input("Press ENTER to continue...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                percentage = calculate_percentage(score, question_num)
                input(f"Your result:\nScore: {score}\nSuccess percentage: {percentage}%\nPress ENTER to continue...")

        # =======================================
        #         INLL (AI Learning)
        # =======================================
        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== INLL (Intelligent Natural Language Learning) ===")
            lang_choice = input(
                "In which language do you want to write?\n"
                "1. French\n"
                "2. English\n"
                "3. German\n> "
            ).strip()
            
            mapping = {
                "1": ("FR", "Write your text in French:\n> "),
                "2": ("EN", "Write your text in English:\n> "),
                "3": ("DE", "Write your text in German:\n> ")
            }
            
            if lang_choice not in mapping:
                print("Invalid choice. Returning to menu.")
                continue
            
            lang_code, message = mapping[lang_choice]
            print("Hello! You can start writing your text. Type 'q' to quit.")
            
            while True:
                text = input(message)

                if text.lower() == "q":
                    break
                
                if text == "":
                    print("No text entered.")
                    continue
                
                # AI Learning
                new_words = ia.learn_words(text, lang_code)

                if new_words:
                    print("New words learned:")
                    print(f"{lang_code}: {new_words}")
                
                answer = ia.answer_generation(text)
                print(f"\n---\nAI Response: {answer}\n---\n")

        # =======================================
        #         SETTINGS (Player)
        # =======================================
        elif choice.lower() == "s" or choice.lower() == "p":
            os.system("cls" if os.name == "nt" else "clear")
            settings_choice = input("What do you want to do?\n1. Change language\n> ").strip()
            
            if settings_choice == "1":
                lang_selected = input(
                    f"Select language:\n"
                    f"1. French ({'ON' if player['P'].get('langue', 'FR') == 'FR' else 'OFF'})\n"
                    f"2. English ({'ON' if player['P'].get('langue', 'FR') == 'EN' else 'OFF'})\n"
                    f"3. German ({'ON' if player['P'].get('langue', 'FR') == 'DE' else 'OFF'})\n> "
                ).strip()
                
                try:
                    if lang_selected == "1":
                        player['P']['langue'] = "FR"
                    elif lang_selected == "2":
                        player['P']['langue'] = "EN"
                    elif lang_selected == "3":
                        player['P']['langue'] = "DE"
                    else:
                        print("Invalid choice.")
                except Exception as e:
                    print(f"Error: {e}")
                
                input("Press ENTER to continue...")
                sauvegarder_auto(data, DEFAULT_SAVE_FILE)

        # =======================================
        #         QUIT GAME
        # =======================================
        elif choice.lower() == "q":
            print("Goodbye!")
            running = False
            break

        else:
            print("Invalid choice.")
            input("Press ENTER to continue...")
