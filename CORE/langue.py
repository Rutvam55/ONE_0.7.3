def langue(nom, joueur, v, boutton_state):  
    scnat = boutton_state["1"]
    scnat_1 = boutton_state["1_1"]
    scnat_2 = boutton_state["1_2"]
    
    francais = boutton_state["2"]
    francais_1 = boutton_state["2_1"]
    francais_2 = boutton_state["2_2"]
    
    deutsch = boutton_state["3"]
    deutsch_1 = boutton_state["3_1"]
    deutsch_2 = boutton_state["3_2"]
    
    anglais = boutton_state["4"]
    anglais_1 = boutton_state["4_1"]
    anglais_2 = boutton_state["4_2"]
    
    math = boutton_state["5"]
    math_1 = boutton_state["5_1"]
    
    geo = boutton_state["6"]
    geo_1 = boutton_state["6_1"]
    
    Histo = boutton_state["7"]
    Histo_1 = boutton_state["7_1"]
    Histo_2 = boutton_state["7_2"]

    FR = {
        "main.1.p": "Bienvenue, {name} !\nTu veux faire quoi?",
        "main.2.i": "1. Entrainemant\n2. INL\nP. Parametre\n>\t",
        "main.3.i": "__PARAMETRE__\n1. Langue: {langue}\n2. v: {v}\n>\t",
        "main.4.p": "Appuie sur Entrée pour lancer le quiz avec les modes sélectionnés.",
        "main.5.i": ">\t",
        "main.6.p": "Erreur : aucun mode sélectionné. Sélectionnez au moins un mode.",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "\t1.1. Nom des elemente ({scnat_1})"
    }

    EN = {
        "main.1.p": "Welcome, {name}!\nWhat would you like to do?",
        "main.2.i": "1. Training\nS. Setting\n>\t",
        "main.3.i": "__SETTING__\n1. Language: {langue}\n2. v: {v}",
        "main.4.p": "Press of Enter to start the game.",
        "main.5.i": "Enter your answer (tape 1-5 or (1.2 5.1)): ",
        "main.6.p": "!!! ERROR !!!\n*restart",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "\t1.1. Name of the elemente ({scnat_1})"
    }

    DE = {
        "main.1.p": "Willkommen, {name}!\nWas wollen sie machen?",
        "main.2.i": "1. Aufgaben\nS. Einstellung",
        "main.3.i": "__EINSTELLUNG__\n1. Sprache: {langue}\n2. v: {v}",
        "main.4.p": "Um zu Starten, drucken sie auf Enter.",
        "main.5.i": "Geben sie ihre antwort (tape 1-5 or (1.2 5.1)): ",
        "main.6.p": "!!! FEHLER !!!\n*NEUSTART",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "\t1.1. Name der elemente ({scnat_1})"
    }

    langue_actuelle = joueur["P"]["langue"]
    if langue_actuelle == "EN":
        La = EN
    elif langue_actuelle == "FR":
        La = FR
    elif langue_actuelle == "DE":
        La = DE
    else:
        La = EN  # Par défaut: Français

    # Formatage final
    return {k: v.format(
        name = nom if nom else "Guest",
        langue = joueur["P"]["langue"],
        v = v,
        scnat = "ON" if scnat else "OFF",
        scnat_1 = "ON" if scnat_1 else "OFF",
        scnat_2 = "ON" if scnat_2 else "OFF",
        francais = "ON" if francais else "OFF",
        francais_1 = "ON" if francais_1 else "OFF",
        francais_2 = "ON" if francais_2 else "OFF",
        deutsch = "ON" if deutsch else "OFF",
        deutsch_1 = "ON" if deutsch_1 else "OFF",
        deutsch_2 = "ON" if deutsch_2 else "OFF",
        anglais = "ON" if anglais else "OFF",
        anglais_1 = "ON" if anglais_1 else "OFF",
        anglais_2 = "ON" if anglais_2 else "OFF",
        math = "ON" if math else "OFF",
        math_1 = "ON" if math_1 else "OFF",
        geo = "ON" if geo else "OFF",
        geo_1 = "ON" if geo_1 else "OFF",
        Histo = "ON" if Histo else "OFF",
        Histo_1 = "ON" if Histo_1 else "OFF",
        Histo_2 = "ON" if Histo_2 else "OFF"
    ) for k, v in La.items()}