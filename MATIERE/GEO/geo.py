import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
class Geo(Exercise):
    """Geography exercises"""

    def menu_geo(self, choices, question_num):
        """Main menu for geography exercises"""
        geo_data = DataLoader.load_data("Geo")
        import CORE.link as link
        player = link.player

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
  