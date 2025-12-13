import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
class Deutsch(Exercise):
    """German exercises"""

    def menu_deutsch(self, choices, question_num):
        """Main menu for German exercises"""
        features = DataLoader.load_data("DE")
        import CORE.link as link
        player = link.player

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
