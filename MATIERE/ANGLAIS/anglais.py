import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
class Anglais(Exercise):
    """English exercises"""

    def menu_anglais(self, choices, question_num):
        """Main menu for English exercises"""
        vocabulary = DataLoader.load_data("EN")
        # récupérer dynamiquement le player pour éviter import circulaire
        import CORE.link as link
        player = link.player
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
