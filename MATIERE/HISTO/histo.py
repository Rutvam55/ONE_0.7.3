import random

from CORE.exercise import Exercise
from CORE.dataloader import DataLoader

class Histo(Exercise):
    """Exercices d'histoire"""
 
    def menu_histo(self):
        """Exécute toutes les étapes d'un exercice"""
        answer, correct_answer = self.step_one()
        self.juge = self.step_two(answer, correct_answer)
        self.score, self.xp, self.streak = self.step_three(self.juge)
        return self.score, self.xp, self.streak
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
 