from itertools import islice


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
