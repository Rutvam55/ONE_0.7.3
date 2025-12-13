import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
# player sera récupéré dynamiquement depuis CORE.link pour éviter import circulaire

class Francais(Exercise):
    """French exercises"""

    def menu_francais(self, choices, question_num):
        """Main menu for French exercises"""
        vocabulary, persons, agreement, verb_data = DataLoader.load_data("FR")
        import CORE.link as link
        player = link.player

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
