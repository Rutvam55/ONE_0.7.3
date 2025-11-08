import random
import os
from itertools import islice
from  def_sauv import correction
joueur = None
def set_joueur(j):
    """Définir la variable globale joueur depuis main.py"""
    global joueur
    joueur = j


# Math
from MATIERE.math import math_base
def Math(i, ndq):
    while True:
        print(f"{ndq}) Math\nXP Math: {joueur["Math"]["xp_Math"]}; Level Math: {joueur["Math"]["Level_Math"]}; Exercise Math: {joueur["Math"]["parties_jouees_Math"]}")
        print("-" * 40)
        score = 0
        xp = 0
        streak = False
        choix = random.choice(i)
        if choix == "base":
            question, reponse_correct = math_base()
            reponse = input(question)
        if reponse == "?":
            print("reponse correct: ", reponse_correct)
            streak = True
            break
        else:
            try:
                reponse = int(reponse)
                if reponse == reponse_correct:
                    print("✅ Correct !")
                    score += 1
                    xp += 25
                    streak = True
                    break
                else:
                    print(f"❌ Mauvais ! C’était {reponse_correct}")
                    streak = False
                    xp -= 25
                    break
            except:
                print("=" * 40)
                print("NON VALID")
    return score, xp, streak


# Francais
from MATIERE.francais import francais_voc
def Francais(i, ndq):
    choix = random.choice(i)
    print(f"{ndq}) Francais\nXP Francais: {joueur["Francais"]["xp_Francais"]}; Level Francais: {joueur["Francais"]["Level_Francais"]}; Exercise Francais: {joueur["Francais"]["parties_jouees_Francais"]}")
    print("-" * 40)
    score = 0
    xp = 0
    streak = False
    if choix == "voc dif":
        question = random.choice(list(francais_voc.items()))
        mot, traduction = question
        reponse = input(f"Comment dit-on '{mot}' en Francais?\nEntrer votre réponse: ").strip().capitalize()
    streak, xp, score = correction(reponse, traduction, streak, xp, score)
    return score, xp, streak


# Deutsch
from MATIERE.deutsch import merkmale_von_Kurzgeschichten
def Deutsch(i, ndq):
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    if choix == "Merkmale von Kurzgeschichten (Einfach)":
        print(f"{ndq}) Deutsch\nXP Deutsch: {joueur["Deutsch"]["xp_Deutsch"]}; Level Deutsch: {joueur["Deutsch"]["Level_Deutsch"]}; Exercise Deutsch: {joueur["Deutsch"]["parties_jouees_Deutsch"]}")
        print("-" * 40)
        reponse = input("Schreib einen von denen 10 merkmalen von Kurzgeschichten\n> ")
        if reponse in merkmale_von_Kurzgeschichten:
            print("✅ Correct !")
            score += 1
            xp += 25
        elif reponse == "?":
            print(merkmale_von_Kurzgeschichten)
        else:
            xp -= 25
            print("❌ Mauvais ! Réessaye.")
    elif choix == "Merkmale von Kurzgeschichten (Schwer)":
        reponse_finale = []
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{ndq}) Deutsch\nXP Deutsch: {joueur["Deutsch"]["xp_Deutsch"]}; Level Deutsch: {joueur["Deutsch"]["Level_Deutsch"]}; Exercise Deutsch: {joueur["Deutsch"]["parties_jouees_Deutsch"]}")
            print("-" * 40)
            if set(reponse_finale) == set(merkmale_von_Kurzgeschichten):
                print("Félicitations, tu as trouvé tous les merkmale von Kurzgeschichten !")
                xp = 50 * len(reponse_finale)
                score = len(reponse_finale)
                streak = True
                break
            reponse = input(f"Was sind die Merkmale von Kurzgeschichten?\nRéponses trouvées : {reponse_finale}\nEntrer votre réponse (ou '?' pour abandonner) : ")
            if reponse == "?":
                print(merkmale_von_Kurzgeschichten)
                print(reponse_finale)
                streak = True
                break
            elif reponse in merkmale_von_Kurzgeschichten and reponse not in reponse_finale:
                reponse_finale.append(reponse)
                score += 1
                xp += 100
                print("✅ Correct !")
            else:
                xp -= 50
                print("❌ Mauvais ! Réessaye.")
            input("Appuyez sur Entrée pour continuer...")
    return score, xp, streak


# ScNat
from MATIERE.scnat import elements
from MATIERE.scnat import ordnungszahl_von_elementen
def limiter_elements(elements_dict, niveau):
    """Retourne un dictionnaire limité en fonction du niveau."""
    limites = [5, 10, 15, 20, 25, 30, 35]
    max_elements = limites[min(niveau, len(limites) - 1)]
    return dict(islice(elements_dict.items(), max_elements))
def ScNat(i, ndq):
    while True:
        score = 0
        xp = 0
        streak = False
        choix = random.choice(i)
        print(f"{ndq}) ScNat\nXP ScNat: {joueur["ScNat"]["xp_ScNat"]}; Level ScNat: {joueur["ScNat"]["Level_ScNat"]}; Exercise ScNat: {joueur["ScNat"]["parties_jouees_ScNat"]}")
        print("-" * 40)
        if choix == "element":
            element_subset = limiter_elements(elements, joueur["ScNat"]["Level_ScNat"])
            question = random.choice(list(element_subset.items()))
            symbole, reponse_correct = question
            reponse = input(f"Wie heißt das Element mit dem Symbol '{symbole}'?\n> ").strip().capitalize()
        elif choix == "ordnungszahl":
            element_subset = limiter_elements(ordnungszahl_von_elementen, joueur["ScNat"]["Level_ScNat"])
            symbole, reponse_correct = random.choice(list(element_subset.items()))
            reponse = input(f"Was ist das ordnungszahl von '{symbole}'?\n> ")
        if reponse == "?":
            print("REPONSE CORRECT: ", reponse_correct)
            break
        else:
            if choix == "ordnungszahl":
                try:
                    reponse = int(reponse)
                    if reponse == reponse_correct:
                        print("✅ Correct !")
                        score += 1
                        xp += 50
                        streak = True
                        break
                    else:
                        print(f"❌ Mauvais ! C’était {reponse_correct}")
                        xp -= 50
                        streak = False
                        break
                except:
                    print("=" * 40)
                    print("NON VALIDER")
            else:
                if reponse == reponse_correct:
                    print("✅ Correct !")
                    score += 1
                    xp += 50
                    streak = True
                    break
                else:
                    print(f"❌ Mauvais ! C’était {reponse_correct}")
                    streak = False
                    break
    return score, xp, streak


# Anglais
from MATIERE.anglais import Anglais_voc1_famille, Anglais_voc2_school, Anglais_voc3_loisire, Anglais_voc4_natur, Anglais_voc5_nourriture, Anglais_voc6_vetement, Anglais_voc7_technologie, Anglais_voc8_lieux, Anglais_voc9_corps_sante_menage, Anglais_voc10_vie_metiers_voyages, Anglais_voc11
def Anglais(i, ndq):
    Anglais_voc = [
        Anglais_voc1_famille,
        Anglais_voc2_school,
        Anglais_voc3_loisire,
        Anglais_voc4_natur,
        Anglais_voc5_nourriture,
        Anglais_voc6_vetement,
        Anglais_voc7_technologie,
        Anglais_voc8_lieux,
        Anglais_voc9_corps_sante_menage,
        Anglais_voc10_vie_metiers_voyages,
        Anglais_voc11
        ]

    # Dans la fonction Anglais(i) :
    niveau = joueur.get("Anglais", {}).get("Level_Anglais", 0)

    # Utilise seulement les N dictionnaires de vocabulaire jusqu'au niveau actuel
    # Par exemple : Level 0 -> 1 dictionnaire; Level 1 -> 2 dictionnaires
    # Le niveau est limité au nombre de dictionnaires disponibles
    Anglais_voc = Anglais_voc[:min(niveau + 1, len(Anglais_voc))]

    if not Anglais_voc:
        # Cas d'erreur si le niveau est trop haut ou pas de voc
        Anglais_voc = [Anglais_voc1_famille] 

    print(f"{ndq}) Anglais\nXP Anglais: {joueur["Anglais"]["xp_Anglais"]}; Level Anglais: {joueur["Anglais"]["Level_Anglais"]}; Exercise Anglais: {joueur["Anglais"]["parties_jouees_Anglais"]}")
    print("-" * 40)
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    if choix == "voc easy":
        question = random.choice(list(random.choice(Anglais_voc).items()))
        mauvaise_repose_1 = random.choice(list(random.choice(Anglais_voc).keys()))
        mauvaise_repose_2 = random.choice(list(random.choice(Anglais_voc).keys()))
        mauvaise_repose_3 = random.choice(list(random.choice(Anglais_voc).keys()))
        traduction, mot = question
        valeur = [traduction, mauvaise_repose_1, mauvaise_repose_2, mauvaise_repose_3]
        random.shuffle(valeur)
        A = valeur[0]
        B = valeur[1]
        C = valeur[2]
        D = valeur[3]
        reponse = input(f"Chose the correct translation for '{mot}':\nA. {A}\nB. {B}\nC. {C}\nD. {D}\nEnter your answer (A-D): ").strip().upper()
        if (reponse == "A" and A == traduction) or (reponse == "B" and B == traduction) or (reponse == "C" and C == traduction) or (reponse == "D" and D == traduction):
            print("✅ Correct !")
            score += 1
            xp += 25
            streak = True
        elif reponse == "?":
            print(f"C’était {traduction}")
            streak = True
        else:
            print(f"❌ Mauvais ! C’était {traduction}")
            xp -= 25
            streak = False
    elif choix == "voc difficile":
        question = random.choice(list(random.choice(Anglais_voc).items()))
        mot, traduction = question
        reponse = input(f"Written '{mot}' in English?\nEnter your answer:    ")
        streak, xp, score = correction(reponse, traduction, streak, xp, score)
    #elif choix == "verb":
    #    pass
    return score, xp, streak
