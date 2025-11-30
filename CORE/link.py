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
    
    @staticmethod
    def _load_english():
        """Load English vocabulary data"""
        file_path = DataLoader.get_path('MATIERE/ANGLAIS/anglais_voc1.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            data = json.load(f)
            return data["anglais_voc1"]
    
    @staticmethod
    def _load_french():
        """Load French vocabulary and verb data"""
        file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            data = json.load(f)
            vocabulary = data["francais_voc"]
        
        file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais_verb.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            verb_data = json.load(f)
            agreement = verb_data["verbs"]["accord"]
            persons = verb_data["verbs"]["personnes"]
        
        return vocabulary, persons, agreement, verb_data
    
    @staticmethod
    def _load_german():
        """Load German vocabulary data"""
        file_path = DataLoader.get_path('MATIERE/DEUTSCH/deutsch.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            data = json.load(f)
            return data["merkmale_von_Kurzgeschichten"]
    
    @staticmethod
    def _load_scnat():
        """Load natural sciences data"""
        file_path = DataLoader.get_path('MATIERE/SCNAT/scnat.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            data = json.load(f)
            elements = data["elements"]
            atomic_numbers = data["ordnungszahl_von_elementen"]
        
        return elements, atomic_numbers
    
    @staticmethod
    def _load_math():
        """Load mathematics data"""
        from MATIERE.MATH.math import math_base
        return math_base
    
    @staticmethod
    def _load_geography():
        """Load geography data"""
        file_path = DataLoader.get_path('MATIERE/GEO/geo.json')
        with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
            return json.load(f)


class Exercise:
    """Base class for exercises"""
    
    def __init__(self):
        self.score = 0
        self.xp = 0
        self.streak = False
    
    def display_header(self, question_num, subject, stats):
        """Display exercise header with statistics"""
        print(f"{question_num}) {subject}")
        print(f"XP: {stats['xp']}; Level: {stats['level']}; Exercises: {stats['exercises']}")
        print("-" * 40)
    
    def check_answer(self, answer, correct_answer, xp_gain=50, xp_loss=50):
        """Check and validate user answer"""
        if not answer:
            print("❌ No answer provided!")
            self.streak = False
            return self.score, self.xp, self.streak
            
        try:
            if answer == "?":
                print("Correct answer:", correct_answer)
                return self.score, self.xp, False
            elif answer == str(correct_answer):
                print("✅ Correct!")
                self.score += 1
                self.xp += xp_gain
                self.streak = True
            else:
                print(f"❌ Wrong! It was {correct_answer}")
                self.xp -= xp_loss
                self.streak = False
        except Exception:
            self.score, self.xp, self.streak = self._check_numeric_answer(
                answer, correct_answer, xp_gain, xp_loss
            )
        
        return self.score, self.xp, self.streak
    
    def _check_numeric_answer(self, answer, correct_answer, xp_gain, xp_loss):
        """Check numeric answers"""
        try:
            answer = int(answer)
            if answer == correct_answer:
                print("✅ Correct!")
                self.score += 1
                self.xp += xp_gain
                self.streak = True
            else:
                print(f"❌ Wrong! It was {correct_answer}")
                self.xp -= xp_loss
                self.streak = False
        except ValueError:
            print("=" * 40)
            print("❌ Invalid answer!")
            self.streak = False
        
        return self.score, self.xp, self.streak
    
    def limit_elements(self, elements_dict, level):
        """Return a limited dictionary based on level"""
        limits = [5, 10, 15, 20, 25, 30, 35]
        max_elements = limits[min(level, len(limits) - 1)]
        return dict(islice(elements_dict.items(), max_elements))


class Math(Exercise):
    """Mathematics exercises"""
    
    def menu_math(self, choices, question_num):
        """Main menu for math exercises"""
        math_base = DataLoader.load_data("Math")
        
        stats = {
            'xp': player['Math']['xp_Math'],
            'level': player['Math']['Level_Math'],
            'exercises': player['Math']['parties_jouees_Math']
        }
        self.display_header(question_num, "Math", stats)
        
        choice = random.choice(choices)
        
        if choice == "base":
            question, correct_answer = math_base()
            answer = input(question)
            self.score, self.xp, self.streak = self.check_answer(answer, correct_answer)
        
        return self.score, self.xp, self.streak


class Francais(Exercise):
    """French exercises"""
    
    def menu_francais(self, choices, question_num):
        """Main menu for French exercises"""
        vocabulary, persons, agreement, verb_data = DataLoader.load_data("FR")
        
        stats = {
            'xp': player['Francais']['xp_Francais'],
            'level': player['Francais']['Level_Francais'],
            'exercises': player['Francais']['parties_jouees_Francais']
        }
        self.display_header(question_num, "French", stats)
        
        choice = random.choice(choices)
        
        if choice == "voc dif":
            self._exercise_vocabulary(vocabulary)
        elif choice == "verb":
            self._exercise_verbs(verb_data, persons)
        
        return self.score, self.xp, self.streak
    
    def _exercise_vocabulary(self, vocabulary):
        """French vocabulary exercise"""
        translation, word = random.choice(list(vocabulary.items()))
        answer = input(f"How do you say '{word}' in French?\nEnter your answer: ").strip()
        self.score, self.xp, self.streak = self.check_answer(answer, translation)
    
    def _exercise_verbs(self, verb_data, persons):
        """French verb conjugation exercise"""
        verb = random.choice(verb_data["verbs"]["list"])
        answer, correct_answer = self._conjugate_verb(verb, persons, verb_data)
        self.score, self.xp, self.streak = self.check_answer(answer, correct_answer)
    
    def _conjugate_verb(self, verb, persons, verb_data):
        """Conjugate a French verb"""
        subject = random.choice(persons)
        tense = random.choice(["présent", "passé composé", "imparfait", "plus-que-parfait"])
        answer = input(f"Conjugate '{verb}' at {tense}:\n> {subject} ")
        # verb_data is the full verbs JSON; conjugations live under verb_data["verbs"][verb]
        verbs_root = verb_data.get("verbs", {})
        verb_entry = verbs_root.get(verb, {})

        try:
            if tense == "présent":
                correct_answer = verb_entry["présent"][subject]
            elif tense == "passé composé":
                # construct passé composé as present + participe passé when available
                aux_present = verb_entry.get("présent", {}).get(subject)
                part = verb_entry.get("participe passé")
                if aux_present and part:
                    correct_answer = f"{aux_present} {part}"
                else:
                    correct_answer = ""
            elif tense == "imparfait":
                correct_answer = verb_entry["imparfait"][subject]
            elif tense == "plus-que-parfait":
                # plus-que-parfait = imparfait + participe passé
                imp = verb_entry.get("imparfait", {}).get(subject)
                part = verb_entry.get("participe passé")
                if imp and part:
                    correct_answer = f"{imp} {part}"
                else:
                    correct_answer = ""
        except Exception:
            # Fallback: empty correct_answer to avoid crashing
            correct_answer = ""

        return answer, correct_answer


class Deutsch(Exercise):
    """German exercises"""
    
    def menu_deutsch(self, choices, question_num):
        """Main menu for German exercises"""
        features = DataLoader.load_data("DE")
        
        stats = {
            'xp': player['Deutsch']['xp_Deutsch'],
            'level': player['Deutsch']['Level_Deutsch'],
            'exercises': player['Deutsch']['parties_jouees_Deutsch']
        }
        self.display_header(question_num, "German", stats)
        
        choice = random.choice(choices)
        
        if choice == "Merkmale von Kurzgeschichten (Einfach)":
            self._exercise_features_easy(features)
        elif choice == "Merkmale von Kurzgeschichten (Schwer)":
            self._exercise_features_hard(features, question_num)
        
        return self.score, self.xp, self.streak
    
    def _exercise_features_easy(self, features):
        """Easy features exercise"""
        answer = input("Write one of the 10 'Merkmalen von Kurzgeschichten':\n> ")
        
        if answer in features:
            print("✅ Correct!")
            self.score += 1
            self.xp += 25
            self.streak = True
        elif answer == "?":
            print("Possible answers:", features)
        else:
            print("❌ Wrong! Try again.")
            self.xp -= 25
            self.streak = False
    
    def _exercise_features_hard(self, features, question_num):
        """Hard features exercise"""
        found_answers = []
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{question_num}) German - Hard Mode")
            print("-" * 40)
            
            if set(found_answers) == set(features):
                print("🎉 Congratulations! You found all the features!")
                self.xp = 50 * len(found_answers)
                self.score = len(found_answers)
                self.streak = True
                break
            
            answer = input(f"What are the 'Merkmale von Kurzgeschichten'?\n"
                         f"Found: {found_answers}\n"
                         f"Enter your answer (or '?' to quit): ")
            
            if answer in features:
                found_answers.append(answer)
                print("✅ Added!")
            elif answer == "?":
                break
            else:
                print("❌ Not found.")
            
            input("Press ENTER to continue...")


class ScNat(Exercise):
    """Natural sciences exercises"""
    
    def menu_scnat(self, choices, question_num):
        """Main menu for natural sciences exercises"""
        elements, atomic_numbers = DataLoader.load_data("ScNat")
        
        stats = {
            'xp': player['ScNat']['xp_ScNat'],
            'level': player['ScNat']['Level_ScNat'],
            'exercises': player['ScNat']['parties_jouees_ScNat']
        }
        self.display_header(question_num, "Natural Sciences", stats)
        
        choice = random.choice(choices)
        
        if choice == "element":
            self._exercise_element(elements)
        elif choice == "ordnungszahl":
            self._exercise_atomic_number(atomic_numbers)
        
        return self.score, self.xp, self.streak
    
    def _exercise_element(self, elements):
        """Chemical elements exercise"""
        element_subset = self.limit_elements(elements, player["ScNat"]["Level_ScNat"])
        if not element_subset:
            print("❌ No elements available for this level.")
            return
            
        symbol, correct_answer = random.choice(list(element_subset.items()))
        
        answer = input(f"What is the element with symbol '{symbol}'?\n> ").strip()
        
        if answer == "?":
            print("Correct answer:", correct_answer)
        else:
            self.score, self.xp, self.streak = self.check_answer(answer, correct_answer)
    
    def _exercise_atomic_number(self, atomic_numbers):
        """Atomic number exercise"""
        element_subset = self.limit_elements(atomic_numbers, player["ScNat"]["Level_ScNat"])
        if not element_subset:
            print("❌ No elements available for this level.")
            return
            
        symbol, correct_answer = random.choice(list(element_subset.items()))
        
        answer = input(f"What is the atomic number of '{symbol}'?\n> ").strip()
        
        if answer == "?":
            print("Correct answer:", correct_answer)
        else:
            self.score, self.xp, self.streak = self.check_answer(answer, correct_answer)


class Anglais(Exercise):
    """English exercises"""
    
    def menu_anglais(self, choices, question_num):
        """Main menu for English exercises"""
        vocabulary = DataLoader.load_data("EN")
        level = player["Anglais"]["Level_Anglais"]
        filtered_vocabulary = self.limit_elements(vocabulary, level)
        
        if not filtered_vocabulary:
            print("❌ No vocabulary available for this level.")
            return 0, 0, False
        
        stats = {
            'xp': player['Anglais']['xp_Anglais'],
            'level': player['Anglais']['Level_Anglais'],
            'exercises': player['Anglais']['parties_jouees_Anglais']
        }
        self.display_header(question_num, "English", stats)
        
        choice = random.choice(choices)
        
        if choice == "voc easy":
            self._exercise_easy_vocabulary(filtered_vocabulary)
        elif choice == "voc impossible":
            self._exercise_hard_vocabulary(filtered_vocabulary)
        
        return self.score, self.xp, self.streak
    
    def _exercise_easy_vocabulary(self, vocabulary):
        """Easy vocabulary exercise (multiple choice)"""
        # vocabulary: dict mapping english_word -> french_translation
        if not vocabulary:
            print("❌ No vocabulary available.")
            return

        english_word, correct_translation = random.choice(list(vocabulary.items()))

        # build wrong options from other translations
        all_translations = list(vocabulary.values())
        wrong_pool = [t for t in all_translations if t != correct_translation]
        wrong_answers = []
        if wrong_pool:
            # sample up to 3 wrong answers
            import random as _rand
            count = min(3, len(wrong_pool))
            wrong_answers = _rand.sample(wrong_pool, count)

        options = [correct_translation] + wrong_answers
        _rand.shuffle(options)

        letters = ["A", "B", "C", "D"]
        for letter, option in zip(letters, options):
            print(f"{letter}. {option}")

        answer = input(f"Choose the correct translation for '{english_word}':\nEnter your answer (A-D): ").strip().upper()

        if answer in letters:
            index = letters.index(answer)
            selected = options[index]
            self.score, self.xp, self.streak = self.check_answer(selected, correct_translation)
    
    def _exercise_hard_vocabulary(self, vocabulary):
        """Hard vocabulary exercise (free response)"""
        # vocabulary: dict mapping english_word -> french_translation
        if not vocabulary:
            print("❌ No vocabulary available.")
            return

        english_word, french_translation = random.choice(list(vocabulary.items()))
        # Ask user to write the English word for the given French translation
        answer = input(f"Write the English word for '{french_translation}':\nEnter your answer: ").strip()

        # correct answer is the english_word
        self.score, self.xp, self.streak = self.check_answer(answer, english_word)


class Geo(Exercise):
    """Geography exercises"""
    
    def menu_geo(self, choices, question_num):
        """Main menu for geography exercises"""
        geo_data = DataLoader.load_data("Geo")
        
        stats = {
            'xp': player['Geo']['xp_Geo'],
            'level': player['Geo']['Level_Geo'],
            'exercises': player['Geo']['parties_jouees_Geo']
        }
        self.display_header(question_num, "Geography", stats)
        
        result = self._execute_question(geo_data, question_num)
        
        return self.score, self.xp, result
    
    def _execute_question(self, data, question_num):
        """Execute a complete question"""
        question, correct_answer, question_type = self._step_one(data)
        answer = self._step_two(question, question_type, question_num)
        result = self._step_three(correct_answer, answer)
        
        if result:
            self.score += 1
            self.xp += 50
            self.streak = True
        else:
            self.xp -= 50
            self.streak = False
        
        return self.streak
    
    def _step_one(self, data):
        """Select a question type"""
        question_type = random.choice(["int", "booleen", "str"])
        questions_list = data.get("question", {}).get(question_type, [])

        # questions_list in JSON can be a dict (mapping question->answer)
        # or a sequence. Ensure we always pick a (question, correct_answer)
        if isinstance(questions_list, dict):
            items = list(questions_list.items())
            if items:
                question, correct_answer = random.choice(items)
            else:
                question, correct_answer = "Default question", None
        else:
            # assume it's a sequence; try to pick one safely
            try:
                question_item = random.choice(questions_list)
            except Exception:
                question_item = None

            if isinstance(question_item, tuple) and len(question_item) == 2:
                question, correct_answer = question_item
            elif isinstance(question_item, dict):
                # dict inside a list -> take its first item
                question, correct_answer = next(iter(question_item.items()))
            elif question_item is not None:
                question, correct_answer = question_item, None
            else:
                question, correct_answer = "Default question", None
        
        return question, correct_answer, question_type
    
    def _step_two(self, question, question_type, question_num):
        """Get user answer"""
        if question_type == "str":
            return input(f"{question_num}: {question}\n> ")
        elif question_type == "booleen":
            answer = input(f"{question_num}: {question} (Y/N)\n> ").lower()
            return answer == "y"
        elif question_type == "int":
            while True:
                try:
                    return int(input(f"{question_num}: {question}\n> "))
                except ValueError:
                    print("❌ Please enter a valid number.")
        
        return None
    
    def _step_three(self, correct_answer, answer):
        """Validate answer"""
        # If the correct answer can be multiple values
        if isinstance(correct_answer, list):
            lowered = [str(x).lower() for x in correct_answer]
            if str(answer).lower() in lowered:
                print("✅ Correct!")
                return True
            else:
                print(f"❌ Incorrect! The answer was one of: {correct_answer}")
                return False

        # If the correct answer is a mapping (e.g. options -> bool)
        if isinstance(correct_answer, dict):
            # If user provided a string that matches an option key
            if isinstance(answer, str):
                if answer in correct_answer and bool(correct_answer.get(answer)):
                    print("✅ Correct!")
                    return True
                else:
                    print("❌ Incorrect! Correct options:")
                    for k, v in correct_answer.items():
                        print(f" - {k}: {v}")
                    return False
            # If answer is boolean (Y/N) but correct_answer is a dict of options,
            # we cannot directly compare — show correct options and mark incorrect.
            print("❌ Incorrect! Correct options:")
            for k, v in correct_answer.items():
                print(f" - {k}: {v}")
            return False

        # Fallback: simple string comparison
        if str(answer).lower() == str(correct_answer).lower():
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Incorrect! The answer was: {correct_answer}")
            return False
