# ===============================
#       BUTTON CLASS
# ===============================

class Button:
    """Button management for subject selection"""
    
    def __init__(self):
        self.state = {
            # Note: children buttons are TRUE by default.
            # They become effective only when the parent button is enabled.

            "1": False,
            "1_1": True,
            "1_2": True,
            "EN": False,
            "FR": False,
            "DE": False,

            "2": False,
            "2_1": True,
            "2_2": True,

            "3": False,
            "3_1": True,

            "4": False,
            "4_1": True,

            "5": False,
            "5_1": True,
            "5_2": True,
        }

    def toggle(self, name):
        """Toggle button state"""
        if name in self.state:
            self.state[name] = not self.state[name]
        else:
            print(f"[ERROR] '{name}' does not exist.")

    def collect(self):
        """Collect active menu choices"""
        menu = []
        choices_scnat = []
        choices_langue = []
        ch_langue = []
        choices_math = []
        choices_geo = []
        choices_Histoire = []
        
        # -------- LANGUAGE SELECTION --------
        if self.state["1"] and (self.state["FR"] or self.state["DE"] or self.state["EN"]):
            menu.append("Language")
            if self.state["1_1"]:
                choices_langue.append("Vocabulary")
            if self.state["1_2"]:
                choices_langue.append("Conjugation")
            if self.state["FR"]:
                ch_langue.append("French")
            if self.state["DE"]:
                ch_langue.append("German")
            if self.state["EN"]:
                ch_langue.append("English")

        # -------- SCNAT --------
        if self.state["2"] and (self.state["2_1"] or self.state["2_2"]):
            menu.append("ScNat")
            if self.state["2_1"]:
                choices_scnat.append("element")
            if self.state["2_2"]:
                choices_scnat.append("ordnungszahl")

        # -------- MATH --------
        if self.state["3"] and self.state["3_1"]:
            menu.append("Math")
            if self.state["3_1"]:
                choices_math.append("base")

        # -------- GEO --------
        if self.state["4"] and self.state["4_1"]:
            menu.append("Geo")
            if self.state["4_1"]:
                choices_geo.append("platten tektonik")

        if self.state["5"] and self.state["5_1"]:
            menu.append("Histo")
            if self.state["5_1"]:
                choices_Histoire.append("platten tektonik")
            if self.state["5_2"]:
                choices_Histoire.append("industrialisierung")
            
        
        return menu, ch_langue, choices_langue, choices_scnat, choices_math, choices_geo, choices_Histoire
