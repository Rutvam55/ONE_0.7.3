# ===============================
#       PLAYER CLASS
# ===============================
class Player:
    """Player statistics class"""
    def __init__(self, player_data):
        self.name = player_data["nom"]
        self.password = player_data["mot_de_passe"]
        
        # ScNat
        self.scnat_level = player_data["ScNat"]["Level_ScNat"]
        self.scnat_xp = player_data["ScNat"]["xp_ScNat"]
        self.scnat_max_xp = player_data["ScNat"]["Max_xp_ScNat"]
        
        # Francais
        self.francais_level = player_data["Francais"]["Level_Francais"]
        self.francais_xp = player_data["Francais"]["xp_Francais"]
        self.francais_max_xp = player_data["Francais"]["Max_xp_Francais"]
        
        # Deutsch
        self.deutsch_level = player_data["Deutsch"]["Level_Deutsch"]
        self.deutsch_xp = player_data["Deutsch"]["xp_Deutsch"]
        self.deutsch_max_xp = player_data["Deutsch"]["Max_xp_Deutsch"]
        
        # Anglais
        self.anglais_level = player_data["Anglais"]["Level_Anglais"]
        self.anglais_xp = player_data["Anglais"]["xp_Anglais"]
        self.anglais_max_xp = player_data["Anglais"]["Max_xp_Anglais"]

        # Math
        self.math_level = player_data["Math"]["Level_Math"]
        self.math_xp = player_data["Math"]["xp_Math"]
        self.math_max_xp = player_data["Math"]["Max_xp_Math"]

        # Geo
        self.geo_level = player_data["Geo"]["Level_Geo"]
        self.geo_xp = player_data["Geo"]["xp_Geo"]
        self.geo_max_xp = player_data["Geo"]["Max_xp_Geo"]
        
        # Histoire
        self.Histo_level = player_data["Histo"]["Level_Histo"]
        self.Histo_xp = player_data["Histo"]["xp_Histo"]
        self.Histo_max_xp = player_data["Histo"]["Max_xp_Histo"]
        
        # Settings
        self.language = player_data["P"]["langue"]
