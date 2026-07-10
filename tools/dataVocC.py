import json
import os

# 2. Bestehende Daten laden
datei_name = "/home/rutvam55/CODE/ONE/data/DATA_enVoc.json"
all_words = {}

if os.path.exists(datei_name):
    try:
        with open(datei_name, "r", encoding="utf-8") as file:
            all_words = json.load(file)
    except json.JSONDecodeError:
        all_words = {}

# 1. Benutzereingaben sammeln
word = input("Bitte schreiben sie den wort auf Englich.\n>>\t")
while word in all_words:
    print(f"{word} ist schon gespeichert")
    word = input("Bitte schreiben sie den wort auf Englich.\n>>\t")


# Liste der Pronomen für die automatische Abfrage
language = ["EN", "FR", "DE", "LU"]

EN = word
FR = input("Schreibe das wort auf Französich.\n>>\t")
DE = input("Schreibe das wort auf Deutsch.\n>>\t")
LU = input("Schreibe das wort auf Luxemburg.\n>>\t")

# Struktur zusammenbauen
neues_wort_daten = {
    "EN": EN,
    "FR": FR,
    "DE": DE,
    "LU": LU
}

# 3. Hinzufügen und Speichern
all_words[infinitive] = neues_wort_daten
with open(datei_name, "w", encoding="utf-8") as file:
    json.dump(all_words, file, indent=4, ensure_ascii=False)

print(f"\nDas Verb '{infinitive}' wurde erfolgreich gespeichert!")
