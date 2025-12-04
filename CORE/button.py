# ===============================
#       BUTTON CLASS
# ===============================

class Button:
    """Button management for subject selection"""
    
    def __init__(self):
        self.state = {
            "1": False,
            "1_1": True,
            "1_2": True,

            "2": False,
            "2_1": True,
            "2_2": True,

            "3": False,
            "3_1": True,
            "3_2": True,

            "4": False,
            "4_1": True,
            "4_2": True,

            "5": False,
            "5_1": True,

            "6": False,
            "6_1": True,
            
            "7": False,
            "7_1": True,
            "7_2": True
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
        choices_francais = []
        choices_deutsch = []
        choices_anglais = []
        choices_math = []
        choices_geo = []
        choices_Histoire = []
        
        # -------- SCNAT --------
        if self.state["1"] and (self.state["1_1"] or self.state["1_2"]):
            menu.append("ScNat")
            if self.state["1_1"]:
                choices_scnat.append("element")
            if self.state["1_2"]:
                choices_scnat.append("ordnungszahl")

        # -------- FRANCAIS --------
        if self.state["2"] and (self.state["2_1"] or self.state["2_2"]):
            menu.append("Francais")
            if self.state["2_1"]:
                choices_francais.append("voc dif")
            if self.state["2_2"]:
                choices_francais.append("verb")

        # -------- DEUTSCH --------
        if self.state["3"] and (self.state["3_1"] or self.state["3_2"]):
            menu.append("Deutsch")
            if self.state["3_1"]:
                choices_deutsch.append("Merkmale von Kurzgeschichten (Einfach)")
            if self.state["3_2"]:
                choices_deutsch.append("Merkmale von Kurzgeschichten (Schwer)")

        # -------- ANGLAIS --------
        if self.state["4"] and (self.state["4_1"] or self.state["4_2"]):
            menu.append("Anglais")
            if self.state["4_1"]:
                choices_anglais.append("voc easy")
            if self.state["4_2"]:
                choices_anglais.append("voc impossible")

        # -------- MATH --------
        if self.state["5"] and self.state["5_1"]:
            menu.append("Math")
            if self.state["5_1"]:
                choices_math.append("base")

        # -------- GEO --------
        if self.state["6"] and self.state["6_1"]:
            menu.append("Geo")
            if self.state["6_1"]:
                choices_geo.append("platten tektonik")

        if self.state["7"] and self.state["7_1"]:
            menu.append("Histo")
            if self.state["7_1"]:
                choices_Histoire.append("platten tektonik")
            if self.state["7_2"]:
                choices_Histoire.append("industrialisierung")
            
        
        return menu, choices_scnat, choices_francais, choices_deutsch, choices_anglais, choices_math, choices_geo, choices_Histoire
