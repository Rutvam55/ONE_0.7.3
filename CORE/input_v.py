class CI:
    def matiere(self, exercise, choices, player, ndq, score):
        """Call the appropriate exercise menu dynamically and update sauvegarde.

        Returns: (exercise_score, xp, streak)
        """
        # determine method name from class name, e.g., Anglais -> menu_anglais
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
        answer = input(">\t")
        if c1 == "q":
            self.quit(answer)
        elif c1 == "h":
            self.help(answer)
    
    def input_2c(self, text, c1, c2):
        print(text)
        answer = input(">\t")
        if c1 == "q" or c2 == "q":
            self.quit(answer)
        elif c1 == "h" or c2 == "h":
            self.help(answer)