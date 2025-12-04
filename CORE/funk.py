import json
from pathlib import Path

def controller_int(ndc, ndc_max, nombre, raison):
    """Demande un entier à l'utilisateur avec plusieurs tentatives.
    Retourne 0 si toutes les tentatives échouent.
    """
    attempts = ndc
    while attempts > 0:
        try:
            val = int(input(raison + "\n> "))
            return val
        except ValueError:
            attempts -= 1
            print(f"Entrée invalide. Retour au menu principal. ({attempts}/{ndc_max})")
            input("ENTER pour continuer...")
    return 0

class sauvegarde:
    def __init__(self):
        # emplacement du fichier de sauvegarde
        self.ROOT = Path(__file__).parent.parent
        self.DEFAULT_SAVE_FILE = self.ROOT / "DATA" / "sauvegarde.json"

    def charger_sauvegarde(self, chemin_json: str | Path | None = None):
        """Charge la sauvegarde si elle existe, sinon renvoie une structure vide.
        Accepte un chemin ou utilise le chemin par défaut.
        """
        if chemin_json is None:
            chemin = self.DEFAULT_SAVE_FILE
        else:
            chemin = Path(chemin_json)

        if chemin.exists():
            try:
                with open(chemin, "r", encoding="utf-8") as fichier:
                    donnees = json.load(fichier)
            except json.JSONDecodeError:
                print("Erreur : fichier de sauvegarde corrompu. Réinitialisation.")
                return {"players": {}}

            # Migration: supporter l'ancien format plat vers le format imbriqué
            for nom, player in list(donnees.get("players", {}).items()):
                if isinstance(player, dict) and "mot_de_passe" in player and "Francais" not in player:
                    nouveau = {
                        "mot_de_passe": player.get("mot_de_passe"),
                        "best_score": player.get("best_score", 0),
                        "Francais": {
                            "parties_jouees_Francais": player.get("parties_jouees_Francais", 0),
                            "Level_Francais": player.get("Level_Francais", 0),
                            "xp_Francais": player.get("xp_Francais", 0),
                            "Max_xp_Francais": player.get("Max_xp_Francais", 1000),
                        },
                        "Deutsch": {
                            "parties_jouees_Deutsch": player.get("parties_jouees_Deutsch", 0),
                            "Level_Deutsch": player.get("Level_Deutsch", 0),
                            "xp_Deutsch": player.get("xp_Deutsch", 0),
                            "Max_xp_Deutsch": player.get("Max_xp_Deutsch", 1000),
                        },
                        "ScNat": {
                            "parties_jouees_ScNat": player.get("parties_jouees_ScNat", 0),
                            "Level_ScNat": player.get("Level_ScNat", 0),
                            "xp_ScNat": player.get("xp_ScNat", 0),
                            "Max_xp_ScNat": player.get("Max_xp_ScNat", 1000),
                        },
                        "Anglais": {
                            "parties_jouees_Anglais": player.get("parties_jouees_Anglais", 0),
                            "Level_Anglais": player.get("Level_Anglais", 0),
                            "xp_Anglais": player.get("xp_Anglais", 0),
                            "Max_xp_Anglais": player.get("Max_xp_Anglais", 1000),
                        },
                        "Math": {
                            "parties_jouees_Math": player.get("parties_jouees_Math", 0),
                            "Level_Math": player.get("Level_Math", 0),
                            "xp_Math": player.get("xp_Math", 0),
                            "Max_xp_Math": player.get("Max_xp_Math", 1000),
                        },
                        "Geo": {
                            "parties_jouees_Geo": player.get("parties_jouees_Geo", 0),
                            "Level_Geo": player.get("Level_Geo", 0),
                            "xp_Geo": player.get("xp_Geo", 0),
                            "Max_xp_Geo": player.get("Max_xp_Geo", 1000)
                        },
                        "P": {
                            "langue": player.get("langue", "EN")
                        }
                    }
                    donnees["players"][nom] = nouveau
            return donnees

        # fichier introuvable
        return {"players": {}}

    def sauvegarder_auto(self, donnees, chemin_json: str | Path | None = None):
        """Écrit automatiquement les données actuelles dans le fichier JSON."""
        if chemin_json is None:
            chemin = self.DEFAULT_SAVE_FILE
        else:
            chemin = Path(chemin_json)

        # S'assurer que le dossier existe
        chemin.parent.mkdir(parents=True, exist_ok=True)

        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    def ajouter_joueur(self, donnees, nom, mot_de_passe):
        """Ajoute un nouveau player avec des données par défaut."""
        if nom in donnees.get("players", {}):
            print("Ce player existe déjà.")
            return False

        donnees.setdefault("players", {})
        donnees["players"][nom] = {
            "mot_de_passe": mot_de_passe,
            "best_score": 0,
            "Francais": {
                "parties_jouees_Francais": 0,
                "Level_Francais": 0,
                "xp_Francais": 0,
                "Max_xp_Francais": 1000,
            },
            "Deutsch": {
                "parties_jouees_Deutsch": 0,
                "Level_Deutsch": 0,
                "xp_Deutsch": 0,
                "Max_xp_Deutsch": 1000,
            },
            "ScNat": {
                "parties_jouees_ScNat": 0,
                "Level_ScNat": 0,
                "xp_ScNat": 0,
                "Max_xp_ScNat": 1000,
            },
            "Anglais": {
                "parties_jouees_Anglais": 0,
                "Level_Anglais": 0,
                "xp_Anglais": 0,
                "Max_xp_Anglais": 1000
            },
            "Math": {
                "parties_jouees_Math": 0,
                "Level_Math": 0,
                "xp_Math": 0,
                "Max_xp_Math": 1000
            },
            "Geo": {
                "parties_jouees_Geo": 0,
                "Level_Geo": 0,
                "xp_Geo": 0,
                "Max_xp_Geo": 1000
            },
            "P": {
                "langue": "EN"
            }
        }
        return True

    def Level_up(self, player):
        # ScNat
        if player.get("ScNat", {}).get("xp_ScNat", 0) >= player.get("ScNat", {}).get("Max_xp_ScNat", 1000):
            player["ScNat"]["Level_ScNat"] += 1
            player["ScNat"]["xp_ScNat"] = 0
            player["ScNat"]["Max_xp_ScNat"] += 500
            print(f"🎉 Level up ScNat -> {player['ScNat']['Level_ScNat']}")
        # Francais
        if player.get("Francais", {}).get("xp_Francais", 0) >= player.get("Francais", {}).get("Max_xp_Francais", 1000):
            player["Francais"]["Level_Francais"] += 1
            player["Francais"]["xp_Francais"] = 0
            player["Francais"]["Max_xp_Francais"] += 500
            print(f"🎉 Level up Francais -> {player['Francais']['Level_Francais']}")
        # Deutsch
        if player.get("Deutsch", {}).get("xp_Deutsch", 0) >= player.get("Deutsch", {}).get("Max_xp_Deutsch", 1000):
            player["Deutsch"]["Level_Deutsch"] += 1
            player["Deutsch"]["xp_Deutsch"] = 0
            player["Deutsch"]["Max_xp_Deutsch"] += 500
            print(f"🎉 Level up Deutsch -> {player['Deutsch']['Level_Deutsch']}")
        # Anglais
        if player.get("Anglais", {}).get("xp_Anglais", 0) >= player.get("Anglais", {}).get("Max_xp_Anglais", 1000):
            player["Anglais"]["Level_Anglais"] += 1
            player["Anglais"]["xp_Anglais"] = 0
            player["Anglais"]["Max_xp_Anglais"] += 500
            print(f"🎉 Level up Anglais -> {player['Anglais']['Level_Anglais']}")
        # Math
        if player.get("Math", {}).get("xp_Math", 0) >= player.get("Math", {}).get("Max_xp_Math", 1000):
            player["Math"]["Level_Math"] += 1
            player["Math"]["xp_Math"] = 0
            player["Math"]["Max_xp_Math"] += 500
            print(f"🎉 Level up Math -> {player['Math']['Level_Math']}")
        # Geo
        if player.get("Geo", {}).get("xp_Geo", 0) >= player.get("Geo", {}).get("Max_xp_Geo", 1000):
            player["Geo"]["Level_Geo"] += 1
            player["Geo"]["xp_Geo"] = 0
            player["Geo"]["Max_xp_Geo"] += 500
            print(f"🎉 Level up Geo -> {player['Geo']['Level_Geo']}")

    def selectionner_joueur(self, donnees, nom, mot_de_passe):
        """
        Vérifie si le player existe et si le mot de passe est correct.
        Retourne toujours (player, mot_correct)
        player = dict ou None
        mot_correct = True / False
        """
        if "players" not in donnees:
            print("Aucune sauvegarde chargée.")
            return None, False

        # Joueur n'existe pas
        if nom not in donnees["players"]:
            print("Joueur introuvable.")
            return None, False

        player = donnees["players"][nom]

        # Problème de données
        if "mot_de_passe" not in player:
            print("Données du player corrompues.")
            return None, False

        # Mot de passe incorrect
        if player["mot_de_passe"] != mot_de_passe:
            print("Mot de passe incorrect.")
            return None, False

        # Succès
        return player, True
    