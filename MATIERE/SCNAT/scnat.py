import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
# 'player' est accédé dynamiquement depuis CORE.link pour éviter les import circulaires.

class ScNat(Exercise):
    """Natural sciences exercises"""

    def menu_scnat(self, choices, question_num):
        """Main menu for natural sciences exercises"""
        elements, atomic_numbers = DataLoader.load_data("ScNat")
        # importer localement link pour récupérer le player courant (évite boucle d'import)
        import CORE.link as link
        player = link.player

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
        import CORE.link as link
        player = link.player
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
        import CORE.link as link
        player = link.player
        level = player.get("ScNat", {}).get("Level_ScNat", 1)
        element_subset = self.limit_elements(atomic_numbers, level)
        if not element_subset:
            print("❌ No elements available for this level.")
            return

        symbol, correct_answer = random.choice(list(element_subset.items()))

        answer = input(f"What is the atomic number of '{symbol}'?\n> ").strip()

        self.check_answer(answer, correct_answer)
