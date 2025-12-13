import random
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader
# 'player' est récupéré dynamiquement depuis CORE.link dans les méthodes pour éviter les import circulaires

def opperateur(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b

def choisir_un_nombre(min, max):
    a = random.randint(min, max)
    b = random.randint(min, max)
    return a, b

def math_base():
    i = ["addition", "soustraction", "multiplication", "division"]
    choix = random.choice(i)
    if choix == "addition":
        op = "+"
        a, b = choisir_un_nombre(-100, 100)
        reponse_correct = opperateur(a, b, op)
        if a > 0:
            a = "+" + str(a)
        if b > 0:
            b = "+" + str(b)
    elif choix == "soustraction":
        op = "-"
        a, b = choisir_un_nombre(-100, 100)
        reponse_correct = opperateur(a, b, op) 
        if a > 0:
            a = "+" + str(a)
        if b > 0:
            b = "+" + str(b)
    elif choix == "multiplication":
        op = "*"
        a, b = choisir_un_nombre(-12, 12)
        reponse_correct = opperateur(a, b, op)
        if a > 0:
            a = "+" + str(a)
        if b > 0:
            b = "+" + str(b)
    elif choix == "division":
        op = "/"
        b = 0
        while b == 0:
            reponse_correct, b = choisir_un_nombre(-12, 12)
        a = reponse_correct * b
        if a > 0:
            a = "+" + str(a)
        if b > 0:
            b = "+" + str(b)
    question = f"Calcul\n ({a}) {op} ({b}) = ?\n>"
    return question, int(reponse_correct)



class Math(Exercise):
    """Mathematics exercises"""

    def menu_math(self, choices, question_num):
        """Main menu for math exercises"""
        math_base = DataLoader.load_data("Math")
        import CORE.link as link
        player = link.player

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
