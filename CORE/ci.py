from CORE.dataloader import DataLoader
class CI:
    def __init__(self):
        # créer des instances utilitaires pour un accès via `ci.TEXT` et `ci.INPUT`
        self.TEXT = CI.TEXT()
        self.INPUT = CI.INPUT()
    class TEXT:
        def __init__(self):
            # Charger la configuration de couleur (peut retourner {} si manquant)
            self.COLOR = DataLoader.load_data("COLOR") or {}

        def text_editor(self, text, police = "", text_color = "", background_color = ""):
            """Encapsule le texte avec les codes ANSI pour la couleur et le style."""
            # Fallback en cas d'échec de chargement
            if not self.COLOR:
                print("⚠️ Avertissement : Échec du chargement des données de couleur. Utilisation des codes ANSI par défaut.")
                self.COLOR = {
                    "CODE": "\033[",
                    "RESET": "0",
                    "END CODE": "m",
                    "police": {"FAT": "1", "DIM": "2", "NONE": "0"},
                    "COLOR TEXT": {"GREEN": "32", "RED": "31", "DEFAULT": "39", "RESET": "0"},
                    "BACKGROUND COLOR": {"DEFAULT": "49"}
                }

            # Récupérer les codes (sûrement présents dans self.COLOR)
            style_code = self.COLOR.get("police", {}).get(police, "")
            text_code = self.COLOR.get("COLOR TEXT", {}).get(text_color, "")
            background_code = self.COLOR.get("BACKGROUND COLOR", {}).get(background_color, "")

            code = self.COLOR.get("CODE", "\033[")
            reset = self.COLOR.get("RESET", "0")
            end = self.COLOR.get("END CODE", "m")

            ansi = code
            parts = [part for part in [style_code, text_code, background_code] if part]

            if parts:
                ansi += ";".join(parts) + end
            else:
                ansi = code + self.COLOR.get("COLOR TEXT", {}).get("RESET", "0") + end

            return f"{ansi}{text}{code}{reset}{end}"
    
    def matiere(self, exercise, choices, player, ndq, score):
        """Call the appropriate exercise menu dynamically and update sauvegarde.

        Returns: (exercise_score, xp, streak)
        """

        # determine method name from class name, e.g., language -> menu_language
        method_name = f"menu_{exercise.__class__.__name__.lower()}"
        if not hasattr(exercise, method_name):
            raise AttributeError(f"Exercise object has no method {method_name}")

        # call the exercise menu
        ex_method = getattr(exercise, method_name)
        exercise_score, xp, streak = ex_method(choices, (ndq + 1))

        # update sauvegarde lazily to avoid circular imports
        if exercise_score:
            import CORE.link as link
            link.get_sauvegarde().ajouter_xp(player, exercise.__class__.__name__, 50, True)

        return exercise_score, xp, streak
    
    class INPUT:
        def quit(self, answer):
            if answer.lower() in ["exit", "quitter", "quit", "q", "e"]:
                exit()

        def help(self, answer):
            if answer.lower() in ["help", "aide", "hilfe", "h", "a"]:
                print("Help Menu:")
                print("Type:")
                print("\t- 'q' to quit")
                print("\t- 'h' for help")
                print("\t- '?' for the correct answer")

        def input_1c(self, text, c1):
            print(text)
            answer = input(">\t").strip().lower()
            if c1 == "q":
                self.quit(answer)
            elif c1 == "h":
                self.help(answer)
            else:
                return answer

        def input_2c(self, text, c1, c2):
            print(text)
            answer = input(">\t")
            if c1 == "q" or c2 == "q":
                self.quit(answer)
            elif c1 == "h" or c2 == "h":
                self.help(answer)
            return answer
    