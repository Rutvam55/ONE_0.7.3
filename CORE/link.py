import random
import os
from itertools import islice
import json

# Global variable for player
player = None

# Get the base directory for file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def set_player(p):
    """Set the global player variable from main.py"""
    global player
    player = p


class DataLoader:
    """Class for loading data from JSON files"""

    ENCODING = "utf-8"

    @staticmethod
    def get_path(relative_path):
        """Get absolute path from relative path"""
        return os.path.join(BASE_DIR, relative_path)

    @staticmethod
    def load_data(subject):
        """Load data according to the specified subject"""
        if subject == "EN":
            return DataLoader._load_english()
        elif subject == "FR":
            return DataLoader._load_french()
        elif subject == "DE":
            return DataLoader._load_german()
        elif subject == "ScNat":
            return DataLoader._load_scnat()
        elif subject == "Math":
            return DataLoader._load_math()
        elif subject == "Geo":
            return DataLoader._load_geography()
        elif subject == "Histo":
            return DataLoader._load_histo()
        elif subject == "COLOR":
            return DataLoader._load_color()

    @staticmethod
    def _load_english():
        """Load English vocabulary data"""
        try:
            file_path = DataLoader.get_path('MATIERE/ANGLAIS/anglais_voc1.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                return data.get("anglais_voc1", {})
        except FileNotFoundError:
            print("Error: English data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in English data file.")
            return {}

    @staticmethod
    def _load_french():
        """Load French vocabulary and verb data"""
        vocabulary = {}
        persons = []
        agreement = {}
        verb_data = {}

        try:
            file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                vocabulary = data.get("francais_voc", {})
        except FileNotFoundError:
            print("Error: French vocabulary file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in French vocabulary file.")

        try:
            file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais_verb.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                verb_data = json.load(f)
                persons = verb_data.get("verbs", {}).get("personnes", [])
                agreement = verb_data.get("verbs", {}).get("accord", {})
        except FileNotFoundError:
            print("Error: French verb file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in French verb file.")

        return vocabulary, persons, agreement, verb_data

    @staticmethod
    def _load_german():
        """Load German vocabulary data"""
        try:
            file_path = DataLoader.get_path('MATIERE/DEUTSCH/deutsch.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                return data.get("merkmale_von_Kurzgeschichten", [])
        except FileNotFoundError:
            print("Error: German data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in German data file.")
            return []

    @staticmethod
    def _load_scnat():
        """Load natural sciences data"""
        elements = {}
        atomic_numbers = {}
        try:
            file_path = DataLoader.get_path('MATIERE/SCNAT/scnat.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                elements = data.get("elements", {})
                atomic_numbers = data.get("ordnungszahl_von_elementen", {})
        except FileNotFoundError:
            print("Error: Natural Sciences data file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in Natural Sciences data file.")

        return elements, atomic_numbers

    @staticmethod
    def _load_math():
        """Load mathematics data"""
        try:
            # NOTE: Assuming 'math_base' is available in the expected file path
            from MATIERE.MATH.math import math_base
            return math_base
        except ImportError:
            print("Error: Math base function not found. Returning a dummy function.")
            def dummy_math_base():
                return "2 + 2 = ?", 4
            return dummy_math_base


    @staticmethod
    def _load_geography():
        """Load geography data"""
        try:
            file_path = DataLoader.get_path('MATIERE/GEO/geo.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: Geography data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in Geography data file.")
            return {}
        
    def _load_histo():
        try:
            file_path = DataLoader.get_path('MATIERE/HISTO/histo.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: History data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in History data file.")
            return {}
        
    def _load_color():
        try:
            file_path = DataLoader.get_path('DATA/police.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: COLOR data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in COLOR data file.")
            return {}


class Exercise:
    """Base class for exercises"""

    def __init__(self):
        self.score = 0
        self.xp = 0
        self.streak = False
        # Last result indicator: True=Correct, False=Incorrect, None=Hint/Skip
        self.last_result = False

    def display_header(self, question_num, subject, stats):
        """Display exercise header with statistics"""
        print(f"{question_num}) {subject}")
        print(f"XP: {stats['xp']}; Level: {stats['level']}; Exercises: {stats['exercises']}")
        print("-" * 40)

    def _check_numeric_answer(self, answer, correct_answer, xp_gain, xp_loss):
        """Check numeric answers and return result indicator (True/False)"""
        try:
            # Try to convert both to float for numeric comparison, allowing integers too
            numeric_answer = float(answer)
            numeric_correct = float(correct_answer)
            if numeric_answer == numeric_correct:
                print("✅ Correct!")
                self.score += 1
                self.xp += xp_gain
                self.streak = True
                return True
            else:
                print(f"❌ Wrong! It was {correct_answer}")
                self.xp -= xp_loss
                self.streak = False
                return False
        except ValueError:
            # If conversion to number failed, it's definitively wrong
            print(f"❌ Wrong! It was {correct_answer}")
            self.xp -= xp_loss
            self.streak = False
            return False

    def _validate_answer_and_update_state(self, answer, correct_answer, xp_gain=50, xp_loss=50):
        """
        Check and validate user answer, update score/xp/streak.
        Returns the result indicator: True (Correct), False (Incorrect), or None (Hint/Skip).
        """
        if not answer:
            print("❌ No answer provided!")
            self.streak = False
            return False

        answer_stripped = str(answer).strip()

        # Handle the '?' to show correct answer (Hint/Skip)
        if answer_stripped == "?":
            print("Correct answer:", correct_answer)
            self.streak = False # Streak is reset if they ask for answer
            return None

        # Check for simple string match (case-insensitive)
        elif answer_stripped.lower() == str(correct_answer).strip().lower():
            print("✅ Correct!")
            self.score += 1
            self.xp += xp_gain
            self.streak = True
            return True
        else:
            # Attempt to check if answer is numeric, only if simple string match failed
            # _check_numeric_answer handles the printing and state update
            is_correct = self._check_numeric_answer(answer_stripped, correct_answer, xp_gain, xp_loss)
            return is_correct
            
        # Fallback (Should be caught by the branches above)
        return False

    def check_answer(self, answer, correct_answer, xp_gain=50, xp_loss=50):
        """
        Public method to check answer, update state, and return the simplified result.
        Returns: True (Correct), None (Hint/Skip), or False (Incorrect).
        """
        self.last_result = self._validate_answer_and_update_state(answer, correct_answer, xp_gain, xp_loss)
        return self.last_result

    def limit_elements(self, elements_dict, level):
        """Return a limited dictionary based on level"""
        limits = [5, 10, 15, 20, 25, 30, 35]
        # Use the minimum of the level and the max index of limits
        max_elements = limits[min(level - 1, len(limits) - 1)] if level > 0 else limits[0]
        return dict(islice(elements_dict.items(), max_elements))


class Math(Exercise):
    """Mathematics exercises"""

    def menu_math(self, choices, question_num):
        """Main menu for math exercises"""
        math_base = DataLoader.load_data("Math")

        stats = {
            'xp': player.get('Math', {}).get('xp_Math', 0),
            'level': player.get('Math', {}).get('Level_Math', 1),
            'exercises': player.get('Math', {}).get('parties_jouees_Math', 0)
        }
        self.display_header(question_num, "Math", stats)

        if not choices:
            print("❌ No choices provided for Math.")
            return self.score, self.xp, self.streak

        choice = random.choice(choices)

        if choice == "base":
            try:
                question, correct_answer = math_base()
            except Exception as e:
                print(f"Error executing math_base: {e}")
                question, correct_answer = "Default question: 1+1 = ?", 2 # Fallback
            answer = input(question).strip()
            
            # Use the new check_answer method
            self.check_answer(answer, correct_answer)

        else:
            print(f"❌ Unknown Math choice: {choice}")

        return self.score, self.xp, self.streak


class Francais(Exercise):
    """French exercises"""

    def menu_francais(self, choices, question_num):
        """Main menu for French exercises"""
        vocabulary, persons, agreement, verb_data = DataLoader.load_data("FR")

        stats = {
            'xp': player.get('Francais', {}).get('xp_Francais', 0),
            'level': player.get('Francais', {}).get('Level_Francais', 1),
            'exercises': player.get('Francais', {}).get('parties_jouees_Francais', 0)
        }
        self.display_header(question_num, "French", stats)

        if not choices:
            print("❌ No choices provided for French.")
            return self.score, self.xp, self.streak

        choice = random.choice(choices)

        if choice == "voc dif":
            self._exercise_vocabulary(vocabulary)
        elif choice == "verb":
            self._exercise_verbs(verb_data, persons)
        else:
            print(f"❌ Unknown French choice: {choice}")

        return self.score, self.xp, self.streak

    def _exercise_vocabulary(self, vocabulary):
        """French vocabulary exercise"""
        if not vocabulary:
            print("❌ No vocabulary data available.")
            return

        translation, word = random.choice(list(vocabulary.items()))
        answer = input(f"How do you say '{word}' in French?\nEnter your answer: ").strip()
        
        self.check_answer(answer, translation)

    def _exercise_verbs(self, verb_data, persons):
        """French verb conjugation exercise"""
        if not verb_data.get("verbs", {}).get("list") or not persons:
            print("❌ No verb or person data available.")
            return

        verb = random.choice(verb_data["verbs"]["list"])
        answer, correct_answer = self._conjugate_verb(verb, persons, verb_data)
        
        self.check_answer(answer, correct_answer)

    def _conjugate_verb(self, verb, persons, verb_data):
        """Conjugate a French verb"""
        subject = random.choice(persons)
        tense = random.choice(["présent", "passé composé", "imparfait", "plus-que-parfait"])
        answer = input(f"Conjugate '{verb}' at {tense}:\n> {subject} ").strip()
        verbs_root = verb_data.get("verbs", {})
        verb_entry = verbs_root.get(verb, {})
        correct_answer = ""

        try:
            if tense == "présent":
                correct_answer = verb_entry.get("présent", {}).get(subject, "")
            elif tense == "passé composé":
                aux_present = verb_entry.get("présent", {}).get(subject)
                part = verb_entry.get("participe passé")
                if aux_present and part:
                    correct_answer = f"{aux_present} {part}"
            elif tense == "imparfait":
                correct_answer = verb_entry.get("imparfait", {}).get(subject, "")
            elif tense == "plus-que-parfait":
                imp = verb_entry.get("imparfait", {}).get(subject)
                part = verb_entry.get("participe passé")
                if imp and part:
                    correct_answer = f"{imp} {part}"
        except Exception as e:
            print(f"Error during conjugation: {e}")
            correct_answer = ""

        return answer, correct_answer


class Deutsch(Exercise):
    """German exercises"""

    def menu_deutsch(self, choices, question_num):
        """Main menu for German exercises"""
        features = DataLoader.load_data("DE")

        stats = {
            'xp': player.get('Deutsch', {}).get('xp_Deutsch', 0),
            'level': player.get('Deutsch', {}).get('Level_Deutsch', 1),
            'exercises': player.get('Deutsch', {}).get('parties_jouees_Deutsch', 0)
        }
        self.display_header(question_num, "German", stats)

        if not choices:
            print("❌ No choices provided for German.")
            return self.score, self.xp, self.streak

        choice = random.choice(choices)

        if choice == "Merkmale von Kurzgeschichten (Einfach)":
            self._exercise_features_easy(features)
        elif choice == "Merkmale von Kurzgeschichten (Schwer)":
            self._exercise_features_hard(features, question_num)
        else:
            print(f"❌ Unknown German choice: {choice}")

        return self.score, self.xp, self.streak

    def _exercise_features_easy(self, features):
        """Easy features exercise"""
        if not features:
            print("❌ No features data available.")
            return

        answer = input("Write one of the 'Merkmalen von Kurzgeschichten':\n> ").strip()

        # Simple check for easy mode (no check_answer call here, use custom logic)
        if answer == "?":
            print("Possible answers:", features)
            self.streak = False
            return
        elif answer in features:
            print("✅ Correct!")
            self.score += 1
            self.xp += 25
            self.streak = True
        else:
            print("❌ Wrong! Try again.")
            self.xp -= 25
            self.streak = False

    def _exercise_features_hard(self, features, question_num):
        """Hard features exercise - Returns score, xp, streak"""
        if not features:
            print("❌ No features data available.")
            return

        found_answers = set()
        features_set = set(features)
        initial_xp = self.xp
        initial_score = self.score

        while True:
            # os.system('cls' if os.name == 'nt' else 'clear') # Keep this commented for simplicity
            print(f"{question_num}) German - Hard Mode")
            print("-" * 40)

            if found_answers == features_set:
                print("🎉 Congratulations! You found all the features!")
                # Update final stats based on achievement
                self.xp = initial_xp + (50 * len(found_answers))
                self.score = initial_score + len(found_answers)
                self.streak = True
                break

            answer = input(f"What are the 'Merkmale von Kurzgeschichten'?\n"
                         f"Found: {list(found_answers)}\n"
                         f"Enter your answer (or '?' to quit): ").strip()

            if answer == "?":
                break # Exit the loop
            elif answer in features_set and answer not in found_answers:
                found_answers.add(answer)
                print("✅ Added!")
            elif answer in found_answers:
                print("Already found.")
            else:
                print("❌ Not found.")

            # input("Press ENTER to continue...") # Keep this commented for simplicity

        # The end of the loop will return the final updated score/xp/streak
        return


class ScNat(Exercise):
    """Natural sciences exercises"""

    def menu_scnat(self, choices, question_num):
        """Main menu for natural sciences exercises"""
        elements, atomic_numbers = DataLoader.load_data("ScNat")

        stats = {
            'xp': player.get('ScNat', {}).get('xp_ScNat', 0),
            'level': player.get('ScNat', {}).get('Level_ScNat', 1),
            'exercises': player.get('ScNat', {}).get('parties_jouees_ScNat', 0)
        }
        self.display_header(question_num, "Natural Sciences", stats)

        if not choices:
            print("❌ No choices provided for Natural Sciences.")
            return self.score, self.xp, self.streak

        choice = random.choice(choices)

        if choice == "element":
            self._exercise_element(elements)
        elif choice == "ordnungszahl":
            self._exercise_atomic_number(atomic_numbers)
        else:
            print(f"❌ Unknown ScNat choice: {choice}")

        return self.score, self.xp, self.streak

    def _exercise_element(self, elements):
        """Chemical elements exercise"""
        level = player.get("ScNat", {}).get("Level_ScNat", 1)
        element_subset = self.limit_elements(elements, level)
        if not element_subset:
            print("❌ No elements available for this level.")
            return

        symbol, correct_answer = random.choice(list(element_subset.items()))

        answer = input(f"What is the element with symbol '{symbol}'?\n> ").strip()

        self.check_answer(answer, correct_answer)

    def _exercise_atomic_number(self, atomic_numbers):
        """Atomic number exercise"""
        level = player.get("ScNat", {}).get("Level_ScNat", 1)
        element_subset = self.limit_elements(atomic_numbers, level)
        if not element_subset:
            print("❌ No elements available for this level.")
            return

        symbol, correct_answer = random.choice(list(element_subset.items()))

        answer = input(f"What is the atomic number of '{symbol}'?\n> ").strip()

        self.check_answer(answer, correct_answer)


class Anglais(Exercise):
    """English exercises"""

    def menu_anglais(self, choices, question_num):
        """Main menu for English exercises"""
        vocabulary = DataLoader.load_data("EN")
        level = player.get("Anglais", {}).get("Level_Anglais", 1)
        filtered_vocabulary = self.limit_elements(vocabulary, level)

        stats = {
            'xp': player.get('Anglais', {}).get('xp_Anglais', 0),
            'level': player.get('Anglais', {}).get('Level_Anglais', 1),
            'exercises': player.get('Anglais', {}).get('parties_jouees_Anglais', 0)
        }
        self.display_header(question_num, "English", stats)

        if not filtered_vocabulary:
            print("❌ No vocabulary available for this level.")
            return self.score, self.xp, False

        if not choices:
            print("❌ No choices provided for English.")
            return self.score, self.xp, self.streak

        choice = random.choice(choices)

        if choice == "voc easy":
            self._exercise_easy_vocabulary(filtered_vocabulary)
        elif choice == "voc impossible":
            self._exercise_hard_vocabulary(filtered_vocabulary)
        else:
            print(f"❌ Unknown English choice: {choice}")

        return self.score, self.xp, self.streak

    def _exercise_easy_vocabulary(self, vocabulary):
        """Easy vocabulary exercise (multiple choice)"""
        if not vocabulary:
            print("❌ No vocabulary available.")
            return

        english_word, correct_translation = random.choice(list(vocabulary.items()))

        all_translations = list(vocabulary.values())
        wrong_pool = [t for t in all_translations if t != correct_translation]
        wrong_answers = []
        if wrong_pool:
            import random as _rand
            count = min(3, len(wrong_pool))
            wrong_answers = _rand.sample(wrong_pool, count)

        options = [correct_translation] + wrong_answers
        random.shuffle(options)

        letters = ["A", "B", "C", "D"]
        for letter, option in zip(letters, options):
            print(f"{letter}. {option}")

        answer = input(f"Choose the correct translation for '{english_word}':\nEnter your answer (A-D or '?'): ").strip().upper()

        if answer == "?":
            print("Correct answer:", correct_translation)
            self.streak = False
            return # Don't update score/xp
        elif answer in letters:
            try:
                index = letters.index(answer)
                selected = options[index]
                # Check the selected option against the correct translation
                self.check_answer(selected, correct_translation, xp_gain=50, xp_loss=50)
            except IndexError:
                # Should not happen if answer is in letters, but as a safeguard
                print("❌ Invalid selection.")
                self.streak = False
        else:
            print("❌ Invalid answer format.")
            self.streak = False


    def _exercise_hard_vocabulary(self, vocabulary):
        """Hard vocabulary exercise (free response)"""
        if not vocabulary:
            print("❌ No vocabulary available.")
            return

        english_word, french_translation = random.choice(list(vocabulary.items()))
        answer = input(f"Write the English word for '{french_translation}':\nEnter your answer: ").strip()

        # correct answer is the english_word
        self.check_answer(answer, english_word)


class Geo(Exercise):
    """Geography exercises"""

    def menu_geo(self, choices, question_num):
        """Main menu for geography exercises"""
        geo_data = DataLoader.load_data("Geo")

        stats = {
            'xp': player.get('Geo', {}).get('xp_Geo', 0),
            'level': player.get('Geo', {}).get('Level_Geo', 1),
            'exercises': player.get('Geo', {}).get('parties_jouees_Geo', 0)
        }
        self.display_header(question_num, "Geography", stats)

        if not geo_data:
            print("❌ No geography data available.")
            return self.score, self.xp, self.streak

        self._execute_question(geo_data, question_num)

        return self.score, self.xp, self.streak

    def _execute_question(self, data, question_num):
        """Execute a complete question"""
        question, correct_answer, question_type = self._step_one(data)
        if correct_answer is None:
            print("❌ Could not select a valid question.")
            self.streak = False
            return # Exit, self.score and self.xp are unchanged

        answer = self._step_two(question, question_type, question_num)

        # We use a custom validation for Geo because of the complex answer types (list, dict, bool)
        self._validate_geo_answer(correct_answer, answer)

    def _step_one(self, data):
        """Select a question type"""
        question_type = random.choice(["int", "booleen", "str"])
        questions_list = data.get("question", {}).get(question_type, [])
        question, correct_answer = "Default question", None

        # Handle different structures for questions_list
        if isinstance(questions_list, dict):
            items = list(questions_list.items())
            if items:
                question, correct_answer = random.choice(items)
        elif isinstance(questions_list, list) and questions_list:
            question_item = random.choice(questions_list)
            if isinstance(question_item, tuple) and len(question_item) == 2:
                question, correct_answer = question_item
            elif isinstance(question_item, dict):
                # dict inside a list -> take its first item
                question, correct_answer = next(iter(question_item.items()))
            elif question_item is not None:
                print(f"Warning: Question format in list is ambiguous: {question_item}")
                question, correct_answer = question_item, None


        return question, correct_answer, question_type

    def _step_two(self, question, question_type, question_num):
        """Get user answer"""
        if question_type == "str":
            return input(f"{question_num}: {question}\n> ").strip()
        elif question_type == "booleen":
            answer = input(f"{question_num}: {question} (Y/N or ?)\n> ").strip().lower()
            if answer == "?":
                return "?"
            return answer == "y"
        elif question_type == "int":
            while True:
                try:
                    raw_input = input(f"{question_num}: {question}\n> ").strip()
                    if raw_input == "?":
                        return "?"
                    return int(raw_input)
                except ValueError:
                    print("❌ Please enter a valid number or '?' for the answer.")

        return None

    def _validate_geo_answer(self, correct_answer, answer):
        """Validate answer for Geo questions, update state, and return simple result."""
        
        # Check for hint/skip request
        if str(answer) == "?":
            print(f"Correct answer: {correct_answer}")
            self.xp -= 50 # Penalty for hint
            self.streak = False
            self.last_result = None
            return

        is_correct = False
        
        # If the correct answer can be multiple values (list)
        if isinstance(correct_answer, list):
            lowered = [str(x).strip().lower() for x in correct_answer]
            if str(answer).strip().lower() in lowered:
                is_correct = True
            else:
                print(f"❌ Incorrect! The answer was one of: {correct_answer}")

        # If the correct answer is a mapping (dict)
        elif isinstance(correct_answer, dict):
            str_answer = str(answer).strip()
            if str_answer in correct_answer and bool(correct_answer.get(str_answer)):
                is_correct = True
            else:
                print("❌ Incorrect! Correct options:")
                correct_options = [k for k, v in correct_answer.items() if v]
                print(f"The answer was one of: {correct_options}")

        # Fallback: simple string comparison, robust to numbers
        elif str(answer).strip().lower() == str(correct_answer).strip().lower():
            is_correct = True
        else:
            print(f"❌ Incorrect! The answer was: {correct_answer}")

        if is_correct:
            print("✅ Correct!")
            self.score += 1
            self.xp += 50
            self.streak = True
        else:
            if not str(answer) == "?": # Avoid double penalty if already penalized for '?'
                self.xp -= 50
                self.streak = False
        
        self.last_result = is_correct
        return is_correct

class Histo(Exercise):
    """Exercices d'histoire"""
 
    def steps(self):
        """Exécute toutes les étapes d'un exercice"""
        answer, correct_answer = self.step_one()
        juge = self.step_two(answer, correct_answer)
        self.step_three(juge)
        # ajoute d'autres étapes si nécessaire
 
    def step_one(self):
        """Première étape"""
        data = DataLoader.load_data("Histo")
        question, correct_answer = self._get_question(data)
        answer = input(f"{question}\n>\t")
        return answer, correct_answer
 
    def step_two(self, answer, correct_answer):
        juge = False
        if answer == correct_answer:
            juge = True
        elif answer == "?":
            juge = None
        else:
            juge = False
        return juge
 
    def step_three(juge):
        if juge == True:
            score = True
            xp = True
            Streak = True
        elif juge == None:
            score = None
            xp = None
            Streak = None
        else:
            score = False
            xp = False
            Streak = False
        return score, xp, Streak
 
    def _get_question(self, data):
        """Retourne une question aléatoire depuis les données"""
        # si data est un dict ou une liste de dicts
        if isinstance(data, dict):
            question, correct_answer = random.choice(list(data.items()))
        elif isinstance(data, list):
            item = random.choice(data)
            if isinstance(item, dict):
                question, correct_answer = next(iter(item.items()))
            else:
                question, correct_answer = str(item), None
        else:
            question, correct_answer = "Question par défaut", None
        return question, correct_answer