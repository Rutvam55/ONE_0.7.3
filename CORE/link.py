import random
import os
from itertools import islice
import json

def load_data(wath):
    if wath == "EN":
        with open('MATIERE/ANGLAIS/anglais_voc1.json', 'r', encoding='utf-8') as f:
            anglais_voc1_data = json.load(f)
            anglais_voc1 = anglais_voc1_data["anglais_voc1"]
        return anglais_voc1
    elif wath == "FR":
        with open('MATIERE/FRANCAIS/francais.json', 'r', encoding='utf-8') as f:
            francais_data = json.load(f)
            francais_voc = francais_data["francais_voc"]
        with open('MATIERE/FRANCAIS/francais_verb.json', 'r', encoding='utf-8') as f:
            francais_verbs_data = json.load(f)
            accord = francais_verbs_data["verbs"]["accord"]
            personne = francais_verbs_data["verbs"]["personnes"]
        return francais_voc, personne, accord, francais_verbs_data
    elif wath == "DE":
        with open('MATIERE/DEUTSCH/deutsch.json', 'r', encoding='utf-8') as f:
            deutsch_data = json.load(f)
            merkmale_von_Kurzgeschichten = deutsch_data["merkmale_von_Kurzgeschichten"]
        return merkmale_von_Kurzgeschichten
    elif wath == "ScNat":
        with open('MATIERE/SCNAT/scnat.json', 'r', encoding='utf-8') as f:
            ScNat_data = json.load(f)
            ScNat_elements = ScNat_data["elements"]
            ScNat_ordnungszahl_von_elementen = ScNat_data["ordnungszahl_von_elementen"]
        return ScNat_elements, ScNat_ordnungszahl_von_elementen
    elif wath == "Math":
        from MATIERE.MATH.math import math_base
        return math_base
    

def verbe_type(verb_typ, personne, francais_verbs_data):
    sujet = random.choice(personne)
    temps = random.choice(["présent", "passé composé", "imparfait", "plus-que-parfait"])    
    reponse = input(f"Conjugaison du verbe '{verb_typ}' au {temps}:\n> {sujet} ")
    if temps == "présent":
        reponse_correct = francais_verbs_data[verb_typ][temps][sujet]
    elif temps == "passé composé":
        temps == "participe passé"
        reponse_correct = francais_verbs_data[verb_typ]["present"][sujet] + " " + francais_verbs_data[verb_typ][temps]
    elif temps == "imparfait":
        reponse_correct = francais_verbs_data[verb_typ][temps][sujet]
    elif temps == "plus-que-parfait":
        reponse_correct = francais_verbs_data[verb_typ]["imparfait"][sujet] + " " + francais_verbs_data[verb_typ]["participe passé"]
    return reponse, reponse_correct

joueur = None
def set_joueur(j):
    """Définir la variable globale joueur depuis main.py"""
    global joueur
    joueur = j

def control(score, xp, streak, reponse, reponse_correct, max):
    try:
        if reponse == "?":
            print("reponse correct: ", reponse_correct)
        elif reponse == reponse_correct:
            print("✅ Correct !")
            score += 1
            xp += 50
            streak = True
        else:
            print(f"❌ Mauvais ! C’était {reponse_correct}")
            xp -= 50
            streak = False
        return score, xp, streak
    except:
        while max != 0:
            try:
                reponse = int(reponse)
                if reponse == "?":
                    print("reponse correct: ", reponse_correct)
                    break
                elif reponse == reponse_correct:
                    print("✅ Correct !")
                    score += 1
                    xp += 50
                    streak = True
                    max = 0
                else:
                    print(f"❌ Mauvais ! C’était {reponse_correct}")
                    xp -= 50
                    streak = False
                    max = 0
                return score, xp, streak
            except:
                print("=" * 40)
        return score, xp, streak


# Math
def Math(i, ndq, L):
    math_base = load_data("Math")
    print(f"{ndq}) Math\nXP Math: {joueur['Math']['xp_Math']}; Level Math: {joueur['Math']['Level_Math']}; Exercise Math: {joueur['Math']['parties_jouees_Math']}")
    print("-" * 40)
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    if choix == "base":
        question, reponse_correct = math_base()
        reponse = input(question)
        score, xp, streak = control(score, xp, streak, reponse, reponse_correct, 5)
    return score, xp, streak


# Francais
def Francais(i, ndq, L):
    francais_voc, personne, accord, francais_verbs_data = load_data("FR")
    choix = random.choice(i)
    print(f"{ndq}) Francais\nXP Francais: {joueur['Francais']['xp_Francais']}; Level Francais: {joueur['Francais']['Level_Francais']}; Exercise Francais: {joueur['Francais']['parties_jouees_Francais']}")
    print("-" * 40)
    score = 0
    xp = 0
    streak = False
    if choix == "voc dif":
        question = random.choice(list(francais_voc.items()))
        traduction, mot = question
        reponse = input(f"Comment dit-on '{mot}' en Francais?\nEntrer votre réponse: ").strip().capitalize()
    elif choix == "verb":
        verbe_typ = random.choice(francais_verbs_data["verbs"]["list"])
        reponse, traduction = verbe_type(verbe_typ, personne, francais_verbs_data)
    score, xp, streak = control(score, xp, streak, reponse, traduction, 5)
    return score, xp, streak


# Deutsch
def Deutsch(i, ndq, L):
    merkmale_von_Kurzgeschichten = load_data("DE")
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    if choix == "Merkmale von Kurzgeschichten (Einfach)":
        print(f"{ndq}) Deutsch\nXP Deutsch: {joueur['Deutsch']['xp_Deutsch']}; Level Deutsch: {joueur['Deutsch']['Level_Deutsch']}; Exercise Deutsch: {joueur['Deutsch']['parties_jouees_Deutsch']}")
        print("-" * 40)
        reponse = input("Schreib einen von denen 10 merkmalen von Kurzgeschichten\n> ")
        if reponse in merkmale_von_Kurzgeschichten:
            print("✅ Correct !")
            score += 1
            xp += 25
            streak = True
        elif reponse == "?":
            print(merkmale_von_Kurzgeschichten)
        else:
            xp -= 25
            streak = False
            print("❌ Mauvais ! Réessaye.")
    elif choix == "Merkmale von Kurzgeschichten (Schwer)":
        reponse_finale = []
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{ndq}) Deutsch\nXP Deutsch: {joueur['Deutsch']['xp_Deutsch']}; Level Deutsch: {joueur['Deutsch']['Level_Deutsch']}; Exercise Deutsch: {joueur['Deutsch']['parties_jouees_Deutsch']}")
            print("-" * 40)
            if set(reponse_finale) == set(merkmale_von_Kurzgeschichten):
                print("Félicitations, tu as trouvé tous les merkmale von Kurzgeschichten !")
                xp = 50 * len(reponse_finale)
                score = len(reponse_finale)
                streak = True
                break
            reponse = input(f"Was sind die Merkmale von Kurzgeschichten?\nRéponses trouvées : {reponse_finale}\nEntrer votre réponse (ou '?' pour abandonner) : ")
            if reponse in merkmale_von_Kurzgeschichten:
                reponse_finale.append(reponse)
                print("✅ Ajouté !")
            elif reponse == "?":
                break
            else:
                print("❌ Pas trouvé.")
            input("Appuyez sur Entrée pour continuer...")
    return score, xp, streak


# ScNat
def limiter_elements(elements_dict, niveau):
    """Retourne un dictionnaire limité en fonction du niveau."""
    limites = [5, 10, 15, 20, 25, 30, 35]
    max_elements = limites[min(niveau, len(limites) - 1)]
    return dict(islice(elements_dict.items(), max_elements))
def ScNat(i, ndq, L):
    elements, ordnungszahl_von_elementen = load_data("ScNat")
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    print(f"{ndq}) ScNat\nXP ScNat: {joueur['ScNat']['xp_ScNat']}; Level ScNat: {joueur['ScNat']['Level_ScNat']}; Exercise ScNat: {joueur['ScNat']['parties_jouees_ScNat']}")
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
    else:
        if choix == "ordnungszahl":
            try:
                reponse = int(reponse)
                if reponse == reponse_correct:
                    print("✅ Correct !")
                    score += 1
                    xp += 50
                    streak = True
                else:
                    print(f"❌ Mauvais ! C’était {reponse_correct}")
                    xp -= 50
                    streak = False
            except:
                print("=" * 40)
                print("NON VALIDER")
        else:
            if reponse == reponse_correct:
                print("✅ Correct !")
                score += 1
                xp += 50
                streak = True
            else:
                print(f"❌ Mauvais ! C’était {reponse_correct}")
                streak = False
    return score, xp, streak


# Anglais
def Anglais(i, ndq, L):
    Anglais_voc1 = load_data("EN")
    niveau = joueur["Anglais"]["Level_Anglais"]
    Anglais_voc_filtered = limiter_elements(Anglais_voc1, niveau)
    if not Anglais_voc_filtered:
        print("Aucun vocabulaire disponible pour ce niveau.")
        return 0, 0, False

    print(f"{ndq}) Anglais\nXP Anglais: {joueur['Anglais']['xp_Anglais']}; Level Anglais: {joueur['Anglais']['Level_Anglais']}; Exercise Anglais: {joueur['Anglais']['parties_jouees_Anglais']}")
    print("-" * 40)
    score = 0
    xp = 0
    streak = False
    choix = random.choice(i)
    if choix == "voc easy":
        question = random.choice(list(random.choice(Anglais_voc_filtered).items()))
        mauvaise_repose_1 = random.choice(list(random.choice(Anglais_voc_filtered).keys()))
        mauvaise_repose_2 = random.choice(list(random.choice(Anglais_voc_filtered).keys()))
        mauvaise_repose_3 = random.choice(list(random.choice(Anglais_voc_filtered).keys()))
        traduction, mot = question
        valeur = [traduction, mauvaise_repose_1, mauvaise_repose_2, mauvaise_repose_3]
        random.shuffle(valeur)
        A = valeur[0]
        B = valeur[1]
        C = valeur[2]
        D = valeur[3]
        reponse = input(f"Chose the correct translation for '{mot}':\nA. {A}\nB. {B}\nC. {C}\nD. {D}\nEnter your answer (A-D): ").strip().upper()
        score, xp, streak = control(score, xp, streak, reponse, traduction, 5)
    elif choix == "voc impossible":
        question = random.choice(list(random.choice(Anglais_voc_filtered).items()))
        mot, traduction = question
        reponse = input(f"Written '{mot}' in English?\nEnter your answer:    ")
        score, xp, streak = control(score, xp, streak, reponse, traduction, 5)
    #elif choix == "verb":
    #    pass
    return score, xp, streak
