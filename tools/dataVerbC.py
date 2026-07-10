import json
import os

# 2. Bestehende Daten laden
datei_name = "/home/rutvam55/CODE/ONE/data/DATA_en.json"
alle_verben = {}

if os.path.exists(datei_name):
    try:
        with open(datei_name, "r", encoding="utf-8") as file:
            alle_verben = json.load(file)
    except json.JSONDecodeError:
        alle_verben = {}

# 1. Benutzereingaben sammeln
infinitive = input("Bitte schreiben sie den \033[1minfinitive\033[0m vom verb den sie rein schreiben wollen.\n>>\t")
while infinitive in alle_verben:
    infinitive = input("Bitte schreiben sie den \033[1minfinitive\033[0m vom verb den sie rein schreiben wollen.\n>>\t")


# Liste der Pronomen für die automatische Abfrage
pronomen = ["I", "you", "he", "she", "it", "we", "they"]

# Dictionnaires für die Zeiten vorbereiten
present_simple_daten = {}
present_continuous_daten = {}
present_perfect_daten = {}
past_simple_daten = {}
past_continuous_daten = {}
going_to_futur_daten = {}
will_futur_daten = {}


# --- PRESENT simple ---
print("\n\033[1mPresent Simple\033[0m")
print("\033[1m----------- --\033[0m")

erste_eingabe = input(f"Bitte schreiben sie den verb correct in den \033[1mersten personn singular ({pronomen[0]})\033[0m vom verb rein.\nZeit: \033[1mpresent simple\033[0m\n>>\t")
# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            present_simple_daten[pronomen[i]] = verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            present_simple_daten[pronomen[i]] = input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        present_simple_daten[pronomen[i]] = infinitive+"s" if pronomen[i] in ["he", "she", "it"] else ""
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    present_simple_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        present_simple_daten[p] = input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")


# --- PRESENT CONTINUOUS ---
print("\n\033[1mPresent Continuous\033[0m")
print("\033[1m---------------\033[0m")

erste_eingabe = input(f"Bitte schreiben sie den verb correct in den \033[1mersten personn singular ({pronomen[0]})\033[0m vom verb rein.\nZeit: \033[1mpresent continuous\033[0m\n>>\t")
temp=erste_eingabe
# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            present_continuous_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else "am " if pronomen[i] == "I" else "are ")+verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            present_continuous_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else "am " if pronomen[i] == "I" else "are ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        present_continuous_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else "am " if pronomen[i] == "I" else "are ")+infinitive+"ing"
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    present_continuous_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        present_continuous_daten[p] = ("is " if pronomen[i] in ["he", "she", "it"] else "am " if pronomen[i] == "I" else "are ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");



# --- PRESENT PERFECT ---
print("\n\033[1mPresent Perfect\033[0m")
print("\033[1m---------------\033[0m")

erste_eingabe = input(f"Bitte schreiben sie den verb correct in den \033[1mersten personn singular ({pronomen[0]})\033[0m vom verb rein.\nZeit: \033[1mpresent perfect\033[0m\n>>\t")
# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            present_perfect_daten[pronomen[i]] = ("has " if pronomen[i] in ["he", "she", "it"] else "have ")+verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            present_perfect_daten[pronomen[i]] = ("has " if pronomen[i] in ["he", "she", "it"] else "have ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        present_perfect_daten[pronomen[i]] = ("has " if pronomen[i] in ["he", "she", "it"] else "have ")+infinitive+"ed"
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    present_perfect_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        present_perfect_daten[p] = ("has " if pronomen[i] in ["he", "she", "it"] else "have ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");



# --- PAST SIMPLE ---
print("\n\033[1mPast Simple\033[0m")
print("\033[1m-------- --\033[0m")

# Das gleiche System für Past Simple (auch hier funktionieren jetzt die Schleifen)
erste_eingabe_past = input(f"Bitte schreiben sie den verb correct in den \033[1mersten personn singular ({pronomen[0]})\033[0m vom verb rein.\nZeit: \033[1mpast simple\033[0m\n>>\t")

if erste_eingabe_past.startswith("[") and "]" in erste_eingabe_past:
    anzahl_wiederholungen = int(erste_eingabe_past[1:erste_eingabe_past.index("]")])
    verb_form = erste_eingabe_past[erste_eingabe_past.index("]") + 1:].strip()
    
    for i in range(7):
        if i < anzahl_wiederholungen:
            past_simple_daten[pronomen[i]] = verb_form
        else:
            past_simple_daten[pronomen[i]] = input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        past_simple_daten[pronomen[i]] = infinitive+"ed"
else:
    past_simple_daten[pronomen[0]] = erste_eingabe_past
    for p in pronomen[1:]:
        past_simple_daten[p] = input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");

        
# --- PAST CONTINUOUS ---
print("\n\033[1mPast Continuous\033[0m")
print("\033[1m---------------\033[0m")

# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
erste_eingabe = temp
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            past_continuous_daten[pronomen[i]] = ("was " if pronomen[i] in ["he", "she", "it", "I"] else "were ")+verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            past_continuous_daten[pronomen[i]] = ("was " if pronomen[i] in ["he", "she", "it", "I"] else "were ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        past_continuous_daten[pronomen[i]] = ("was " if pronomen[i] in ["he", "she", "it", "I"] else "were ")+infinitive+"ing"
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    past_continuous_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        past_continuous_daten[p] = ("was " if pronomen[i] in ["he", "she", "it", "I"] else "were ")+input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");


# --- GOING TO FUTUR ---
print("\n\033[1mGoing To Futur\033[0m")
print("\033[1m---- ---------\033[0m")

erste_eingabe = "[7]"+infinitive
# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            going_to_futur_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else ("am " if pronomen[i]=="I" else "are "))+"going to "+verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            going_to_futur_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else ("am " if pronomen[i]=="I" else "are "))+"going to "+input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        going_to_futur_daten[pronomen[i]] = ("is " if pronomen[i] in ["he", "she", "it"] else ("am " if pronomen[i]=="I" else "are "))+"going to "+infinitive
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    going_to_futur_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        going_to_futur_daten[p] = ("is " if pronomen[i] in ["he", "she", "it"] else ("am " if pronomen[i]=="I" else "are "))+"going to "+input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");


# --- WILL FUTUR ---
print("\n\033[1mWill Futur\033[0m")
print("\033[1m----------\033[0m")

erste_eingabe = "[7]"+infinitive
# Prüfen, ob eine Abkürzung eingegeben wurde, z.B. "[6] played"
if erste_eingabe.startswith("[") and "]" in erste_eingabe:
    # Zahl extrahieren (zwischen den Klammern)
    anzahl_wiederholungen = int(erste_eingabe[1:erste_eingabe.index("]")])
    
    # Den eigentlichen Verb-Teil herausschneiden (alles nach der Klammer und dem Leerzeichen)
    verb_form = erste_eingabe[erste_eingabe.index("]") + 1:].strip()
    
    # Die Form für die gewünschte Anzahl an Pronomen eintragen
    for i in range(7):
        if i < anzahl_wiederholungen:
            will_futur_daten[pronomen[i]] = "will "+verb_form
        else:
            # Falls die Zahl kleiner als 7 war, den Rest normal abfragen
            will_futur_daten[pronomen[i]] = "will "+input(f"Bitte schreiben sie den verb correct in den \033[1m{pronomen[i]}\033[0m vom verb rein.\n>>\t")
elif "{i}" == erste_eingabe:
    for i in range(7):
        will_futur_daten[pronomen[i]] = "will "+infinitive
else:
    # Keine Abkürzung: Erste Person speichern und den Rest normal abfragen
    will_futur_daten[pronomen[0]] = erste_eingabe
    for p in pronomen[1:]:
        will_futur_daten[p] = "will "+input(f"Bitte schreiben sie den verb correct in den \033[1m{p}\033[0m vom verb rein.\n>>\t")
print("finish...");



# Struktur zusammenbauen
neues_verb_daten = {
    "present simple": present_simple_daten,
    "present continuous": present_continuous_daten,
    "present perfect": present_perfect_daten,
    "past simple": past_simple_daten,
    "past continuous": past_continuous_daten,
    "going to futur": going_to_futur_daten,
    "will futur": will_futur_daten
}

# 3. Hinzufügen und Speichern
alle_verben[infinitive] = neues_verb_daten
with open(datei_name, "w", encoding="utf-8") as file:
    json.dump(alle_verben, file, indent=4, ensure_ascii=False)

print(f"\nDas Verb '{infinitive}' wurde erfolgreich gespeichert!")
