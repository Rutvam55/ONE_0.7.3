# Correction : Retirez la f-string et insérez le placeholder `{name}`
def langue(nom, joueur, v):
    Fr = {
        "main.1.p": f"Bienvenue, {nom} !\nTu veux faire quoi?",
        "main.2.i": "1. Entrainemant\nP. Parametre",
        "main.3.i": f'__PARAMETRE__\n1. Langue: {joueur["P"]["langue"]}\n2. v: {v}',
        "main.4.p": "Appuie sur Entrée pour lancer le quiz avec les modes sélectionnés.",
        "main.5.i": "Entrer votre réponse (tape 1-5 pour basculer): ",
        "main.6.p": "Erreur : aucun mode sélectionné. Sélectionnez au moins un mode."
    }

    En = {
        "main.1.p": f"Welcome, {nom}!\nWhat would you like to do?",
        "main.2.i": "1. Training\nS. Setting",
        "main.3.i": f'__SETTING__\n1. Language: {joueur["P"]["langue"]}\n2. v: {v}',
        "main.4.p": "Press of Enter to start the game.",
        "main.5.i": "Enter your answer (tape 1-5 or (1.2 5.1)): ",
        "main.6.p": "!!! ERROR !!!\n*restart"
    } 
    if joueur["Parametre"]["langue"] == "Englich":
        La = En
    if joueur["Parametre"]["langue"] == "Francais":
        La = Fr
    return La
#.format(name = nom if nom else 'Invité')