import random
import os
import pwinput
from CORE.link import set_player, Math, Francais, Deutsch, ScNat, Anglais, Geo, DataLoader, Histo
from CORE.funk import controller_int, sauvegarde
from CORE.langue import langue
from CORE.button import Button
from KI.ia import IA

VERSION = "0.10.0"

COLOR = DataLoader.load_data("COLOR")
# Fallback en cas d'échec de chargement (pour prévenir le TypeError de la fois précédente)
if COLOR is None:
    print("⚠️\u001b[1; 31m Avertissement : Échec du chargement des données de couleur. Utilisation des codes ANSI par défaut.\u001b[0m")
    COLOR = {
        "CODE": "\033[",
        "END CODE": "m",
        "police": {"FAT": "1", "DIM": "2", "NONE": "0"},
        "COLOR TEXT": {"RESET": "0", "GREEN": "32", "RED": "31", "DEFAULT": "39"},
        "BACKGROUND COLOR": {"DEFAULT": "49"}
    }

def text_editor(text, police = "", text_color = "", background_color = ""):
    """Encapsule le texte avec les codes ANSI pour la couleur et le style."""
    
    # Correction de l'AttributeError: .get doit être appelé sur les sous-dictionnaires (ex: COLOR["police"])
    # et non sur le résultat qui est une chaîne (ex: COLOR["police"][police])
    style_code = COLOR["police"].get(police, "")
    text_code = COLOR["COLOR TEXT"].get(text_color, "")
    background_code = COLOR["BACKGROUND COLOR"].get(background_color, "")

    code = COLOR["CODE"]
    end = COLOR["END CODE"]
    
    ansi = code
    # On filtre les parties vides et on les joint par des points-virgules
    parts = [part for part in [style_code, text_code, background_code] if part]
    
    # Si 'parts' est vide, on utilise seulement le code de reset pour l'appliquer.
    if parts:
        ansi += ";".join(parts) + end
    else:
        # Si aucun style, on utilise le code de reset au début pour éviter un crash
        ansi = code + COLOR["COLOR TEXT"]["RESET"] + end

    # Le code de reset est appliqué après le texte pour réinitialiser le terminal
    return f"{ansi}{text}{code}{COLOR["COLOR TEXT"]["RESET"]}{end}"


ia = IA()
s = sauvegarde()

def calculate_percentage(correct_answers, total_questions):
    """Calculate percentage of correct answers"""
    return (correct_answers / total_questions) * 100 if total_questions > 0 else 0



# ===============================
#       MAIN PROGRAM
# ===============================

buttons = Button()
running = True
connection = False

while running:

    data = s.charger_sauvegarde(None)

    # =================================
    #  LOGIN
    # =================================
    while not connection:
        os.system("cls" if os.name == "nt" else "clear")
        print(text_editor("=== ONE ===", police = "FAT", text_color = "DEFAULT", background_color = "DEFAULT"))
        password_correct = False
        attempts = 3

        if attempts == 0 and password_correct is False:
            print("Too many incorrect attempts. Exiting.")
            exit()

        username = input(text_editor("Enter your name.\n>\t", police = "UNDERLINE", text_color = "DEFAULT", background_color = "DEFAULT"))
        if not username:
            print("Username cannot be empty.")
            input("Press ENTER to continue...")
            continue
            
        password = pwinput.pwinput(prompt = text_editor("Enter your password.\n>\t", police = "UNDERLINE", text_color = "DEFAULT", background_color = "DEFAULT"), mask='#')
        if not password:
            print("Password cannot be empty.")
            input("Press ENTER to continue...")
            continue
            
        player, password_correct = s.selectionner_joueur(data, username, password)
        while True:
            if player is None:
                create = input(text_editor("Player not found.\nCreate one? (Y/N)\n>\t", police = "DIM", text_color = "RED", background_color = "DEFAULT")).lower()

                if create in ["y", "oui", "yes", "ja"]:
                    if s.ajouter_joueur(data, username, password):
                        player = data["players"][username]
                        s.sauvegarder_auto(data, )
                        break
                    else:
                        print("ERROR")
                        continue
                elif create in ["n", "non", "no", "nein"]:
                    while password_correct is False and attempts > 0:
                        username = input("Enter your name.\n>\t")
                        password = pwinput.pwinput(prompt="Enter your password.\n>\t", mask='#')
                        player, password_correct = s.selectionner_joueur(data, username, password)
                        if password_correct is True:
                            break
                        attempts -= 1
                        print(f"Password: {password}\nAttempts remaining: {attempts}/3")
                    if attempts == 0 and password_correct is False:
                        print("Too many incorrect attempts. Exiting.")
                        exit()
                else:
                    print("Sorry we don't understand.")
            else:
                break

        connection = True
        set_player(player)

    # ===============================
    #       LANGUAGE
    # ===============================
    L = langue(username, player, VERSION, buttons.state)



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
                    boole = "ON" if buttons.state[btn] else "OFF"
                    if boole == "ON":
                        state = text_editor("ON", police = "FAT", text_color = "GREEN", background_color = "DEFAULT")
                    else:
                        state = text_editor("OFF", police = "FAT", text_color = "RED", background_color = "DEFAULT")
                    print(f"({state}) {txt} ")
                    return boole

                state = show("1", "1. Sciens Naturelle")
                if state == "ON":
                    _ = show("1_1", "\t1.1 Element Namen")
                    _ = show("1_2", "\t1.2 Ordnungszahl")

                state = show("2", "2. Francais")
                if state == "ON":
                    _ = show("2_1", "\t2.1 Vocabulary (difficult)")
                    _ = show("2_2", "\t2.2 Verbs")

                state = show("3", "3. Deutsch")
                if state == "ON":
                    _ = show("3_1", "\t3.1 Kurzgeschichten (easy)")
                    _ = show("3_2", "\t3.2 Kurzgeschichten (hard)")

                state = show("4", "4. Anglais")
                if state == "ON":
                    _ = show("4_1", "\t4.1 Easy vocabulary")
                    _ = show("4_2", "\t4.2 Impossible vocabulary")

                state = show("5", "5. Math")
                if state == "ON":
                    _ = show("5_1", "\t5.1 Base")

                state = show("6", "6. Geography")
                if state == "ON":
                    _ = show("6_1", "\t6.1 les plaque tektonique")

                state = show("7", "7. History")
                if state == "ON":
                    _ = show("7_1", "\t7.1 Theorie der platten tektonik")
                    _ = show("7_2", "\t7.2 Induastrialisierung")

                action = input("\nq: Quit\nENTER to validate, or choose a button.\n>\t").strip()

                mapping = {
                    "1": "1",
                    "1.1": "1_1",
                    "1.2": "1_2",

                    "2": "2",
                    "2.1": "2_1",
                    "2.2": "2_2",

                    "3": "3",
                    "3.1": "3_1",
                    "3.2": "3_2",

                    "4": "4",
                    "4.1": "4_1",
                    "4.2": "4_2",

                    "5": "5",
                    "5.1": "5_1",

                    "6": "6",
                    "6.1": "6_1",

                    "7": "7",
                    "7.1": "7_1",
                    "7.2": "7_2"
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
            menu, choices_scnat, choices_francais, choices_deutsch, choices_anglais, choices_math, choices_geo, choices_histo = buttons.collect()
            
            if not menu:
                print("No games selected in settings.")
                input("Press ENTER to continue...")
                continue
            
            mode_choice = input("Select mode:\n1: Infinite\n2: Normal\n>\t").strip().lower()
            
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
                    elif selected_game == "Histo":
                        exercise = Histo()
                        score, xp, streak = exercise.menu_histo(choices_histo, question_num)
                    else:
                        print("Game selection error.")
                        streak = False
                    
                    if exercise_score == True:
                        score += 1
                    elif exercise_score == None or exercise_score == False:
                        score = score
                    if xp == True:
                        XP += 50
                    elif xp == False:
                        XP -= 50
                    if streak == True or streak == None:
                        streak = True
                    else:
                        streak = False

                    s.Level_up(player)
                    s.sauvegarder_auto(data)
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
                    elif selected_game == "Francais":
                        exercise = Francais()
                        exercise_score, xp, streak = exercise.menu_francais(choices_francais, (i + 1))
                    elif selected_game == "Deutsch":
                        exercise = Deutsch()
                        exercise_score, xp, streak = exercise.menu_deutsch(choices_deutsch, (i + 1))
                    elif selected_game == "Anglais":
                        exercise = Anglais()
                        exercise_score, xp, streak = exercise.menu_anglais(choices_anglais, (i + 1))
                    elif selected_game == "Math":
                        exercise = Math()
                        exercise_score, xp, streak = exercise.menu_math(choices_math, (i + 1))
                    elif selected_game == "Geo":
                        exercise = Geo()
                        exercise_score, xp, streak = exercise.menu_geo(choices_geo, (i + 1))
                    else:
                        print("Game selection error.")
                        streak = False
                    
                    if exercise_score == True:
                        score += 1
                    elif exercise_score == None or exercise_score == False:
                        score = score
                    if xp == True:
                        XP += 50
                    elif xp == False:
                        XP -= 50
                    if streak == True or streak == None:
                        streak = True
                    else:
                        streak = False


                    s.Level_up(player)
                    s.sauvegarder_auto(data)
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
                s.sauvegarder_auto(data, )

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
