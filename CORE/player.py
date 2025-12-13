# ===============================
#       PLAYER CLASS
# ===============================
class Player:
    """Player statistics class"""
    def __init__(self, player_data):
        # Utilise .get pour éviter les KeyError si la structure est incomplète
        self.name = player_data.get("nom") or player_data.get("username") or "<unknown>"
        self.password = player_data.get("mot_de_passe", "")

        # ScNat
        self.scnat_level = player_data.get("ScNat", {}).get("Level_ScNat", 0)
        self.scnat_xp = player_data.get("ScNat", {}).get("xp_ScNat", 0)
        self.scnat_max_xp = player_data.get("ScNat", {}).get("Max_xp_ScNat", 1000)
        
        # Francais
        self.francais_level = player_data.get("Francais", {}).get("Level_Francais", 0)
        self.francais_xp = player_data.get("Francais", {}).get("xp_Francais", 0)
        self.francais_max_xp = player_data.get("Francais", {}).get("Max_xp_Francais", 1000)
        
        # Deutsch
        self.deutsch_level = player_data.get("Deutsch", {}).get("Level_Deutsch", 0)
        self.deutsch_xp = player_data.get("Deutsch", {}).get("xp_Deutsch", 0)
        self.deutsch_max_xp = player_data.get("Deutsch", {}).get("Max_xp_Deutsch", 1000)
        
        # Anglais
        self.anglais_level = player_data.get("Anglais", {}).get("Level_Anglais", 0)
        self.anglais_xp = player_data.get("Anglais", {}).get("xp_Anglais", 0)
        self.anglais_max_xp = player_data.get("Anglais", {}).get("Max_xp_Anglais", 1000)

        # Math
        self.math_level = player_data.get("Math", {}).get("Level_Math", 0)
        self.math_xp = player_data.get("Math", {}).get("xp_Math", 0)
        self.math_max_xp = player_data.get("Math", {}).get("Max_xp_Math", 1000)

        # Geo
        self.geo_level = player_data.get("Geo", {}).get("Level_Geo", 0)
        self.geo_xp = player_data.get("Geo", {}).get("xp_Geo", 0)
        self.geo_max_xp = player_data.get("Geo", {}).get("Max_xp_Geo", 1000)
        
        # Histoire
        self.Histo_level = player_data.get("Histo", {}).get("Level_Histo", 0)
        self.Histo_xp = player_data.get("Histo", {}).get("xp_Histo", 0)
        self.Histo_max_xp = player_data.get("Histo", {}).get("Max_xp_Histo", 1000)
        
        # Settings
        self.language = player_data.get("P", {}).get("langue", "EN")
