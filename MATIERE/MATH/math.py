import random
import os
from CORE.exercise import Exercise
from CORE.dataloader import DataLoader

# Tentative de chargement de la librairie C; si elle est absente, on
# utilise une implémentation Python de secours pour les opérations.
use_c_lib = False
lib = None
try:
    import ctypes
    lib_path = os.path.join(os.path.dirname(__file__), 'math.dll')
    lib = ctypes.CDLL(lib_path)
    # Ne pas forcer d'argtypes ici car l'API C n'est pas garantie.
    use_c_lib = True
except Exception:
    use_c_lib = False

def compute_op(a, b, op):
    if use_c_lib and lib is not None:
        try:
            # Si la librairie C expose une fonction utilitaire, essayer
            # d'appeler `opperateur` avec deux entiers et renvoyer le
            # résultat. En cas d'échec, retomber sur l'implémentation
            # Python.
            return lib.opperateur(int(a), int(b))
        except Exception:
            pass

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        # division entière si divisible, sinon valeur flottante
        try:
            return a // b if a % b == 0 else a / b
        except Exception:
            return 0
    raise ValueError(f"Unknown operator: {op}")

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
                question, correct_answer = self.math_base()
            except Exception as e:
                print(f"Error executing math_base: {e}")
                question, correct_answer = "Default question: 1+1 = ?", 2
            answer = input(question).strip()
            self.check_answer(answer, correct_answer)

        else:
            print(f"❌ Unknown Math choice: {choice}")

        return self.score, self.xp, self.streak
    
    def choisir_un_nombre(self, min, max):
        a = random.randint(min, max)
        b = random.randint(min, max)
        return a, b

    def math_base(self):
        i = ["addition", "soustraction", "multiplication", "division"]
        choix = random.choice(i)
        if choix == "addition":
            op = "+"
            a, b = self.choisir_un_nombre(-100, 100)
            reponse_correct = compute_op(a, b, op)
            if a > 0:
                a = "+" + str(a)
            if b > 0:
                b = "+" + str(b)
        elif choix == "soustraction":
            op = "-"
            a, b = self.choisir_un_nombre(-100, 100)
            reponse_correct = compute_op(a, b, op)
            if a > 0:
                a = "+" + str(a)
            if b > 0:
                b = "+" + str(b)
        elif choix == "multiplication":
            op = "*"
            a, b = self.choisir_un_nombre(-12, 12)
            reponse_correct = compute_op(a, b, op)
            if a > 0:
                a = "+" + str(a)
            if b > 0:
                b = "+" + str(b)
        elif choix == "division":
            op = "/"
            # choisir un diviseur non nul et un quotient, puis fixer a = quotient * b
            b = 0
            while b == 0:
                _, b = self.choisir_un_nombre(-12, 12)
            quotient, _ = self.choisir_un_nombre(-12, 12)
            a = quotient * b
            reponse_correct = quotient
            if a > 0:
                a = "+" + str(a)
            if b > 0:
                b = "+" + str(b)
        question = f"Calcul\n ({a}) {op} ({b}) = ?\n>"
        try:
            return question, int(reponse_correct)
        except Exception:
            return question, reponse_correct
    