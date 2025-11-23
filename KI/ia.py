import json
import re
import unicodedata
from difflib import get_close_matches


class IA:

    def __init__(self, path="DATA/memoir.json", similarity_cutoff=0.80):
        self.path = path
        self.similarity_cutoff = similarity_cutoff   # 0.80 = plus strict

        # Charger le vocabulaire appris
        vocab_FR, vocab_EN, vocab_DE = self.load_data("MEMOIR")

        # Sets pour vitesse et éviter doublons
        self.vocab_FR = set(vocab_FR)
        self.vocab_EN = set(vocab_EN)
        self.vocab_DE = set(vocab_DE)

    # ----------------------------------------------------------
    #   CHARGEMENT ET SAUVEGARDE
    # ----------------------------------------------------------
    def load_data(self, what):
        """Charge les listes depuis JSON ou retourne listes vides."""
        
        try:
            if what == "MEMOIR":
                with open(self.path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                return (
                    data.get("vocab_FR", []),
                    data.get("vocab_EN", []),
                    data.get("vocab_DE", [])
                )
        except:
            return [], [], []

        return [], [], []

    def save_memory(self):
        """Sauvegarde des vocabulaires appris."""
        data = {
            "vocab_FR": sorted(list(self.vocab_FR)),
            "vocab_EN": sorted(list(self.vocab_EN)),
            "vocab_DE": sorted(list(self.vocab_DE)),
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # ----------------------------------------------------------
    #   NORMALISATION DES MOTS
    # ----------------------------------------------------------
    def normalize_word(self, w):
        w = w.lower().strip()
        w = unicodedata.normalize("NFKD", w)
        w = "".join(c for c in w if not unicodedata.combining(c))
        w = re.sub(r"[^\w\-]", "", w)
        return w

    def tokenize(self, sentence):
        sentence = sentence.replace("’", "'")
        sentence = ''.join(c for c in sentence if c.isprintable())
        sentence = sentence.lower()
        sentence = re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç\s]", " ", sentence)
        words = sentence.split()
        return [self.normalize_word(w) for w in words if w.strip()]

    # ----------------------------------------------------------
    #   RECHERCHE DES MOTS SIMILAIRES
    # ----------------------------------------------------------
    def find_closest(self, word, vocab):
        if not vocab:
            return None
        matches = get_close_matches(word, vocab, n=1, cutoff=self.similarity_cutoff)
        return matches[0] if matches else None

    # ----------------------------------------------------------
    #   APPRENTISSAGE DES MOTS
    # ----------------------------------------------------------
    def learn_words(self, sentence, language):
        words = self.tokenize(sentence)

        if language == "FR":
            vocab = self.vocab_FR
        elif language == "EN":
            vocab = self.vocab_EN
        elif language == "DE":
            vocab = self.vocab_DE
        else:
            return {"added": [], "recognized_as": {}, "all_recognized": []}

        added = []
        recognized_as = {}
        all_recognized = []

        vocab_list = list(vocab)

        for w in words:
            if w in vocab:
                all_recognized.append(w)
                continue

            close = self.find_closest(w, vocab_list)
            if close:
                recognized_as[w] = close
                all_recognized.append(close)
            else:
                vocab.add(w)
                added.append(w)
                all_recognized.append(w)
                vocab_list.append(w)

        if added:
            self.save_memory()

        return {
            "added": added,
            "recognized_as": recognized_as,
            "all_recognized": all_recognized
        }

    # ----------------------------------------------------------
    #   DÉTECTION AUTOMATIQUE DE LA LANGUE
    # ----------------------------------------------------------
    def detect_language(self, words):
        score = {"FR": 0, "EN": 0, "DE": 0}

        for w in words:
            if w in self.vocab_FR:
                score["FR"] += 1
            if w in self.vocab_EN:
                score["EN"] += 1
            if w in self.vocab_DE:
                score["DE"] += 1

        best = max(score, key=score.get)

        if score[best] == 0:
            return None
        return best

    # ----------------------------------------------------------
    #   GÉNÉRATION DE RÉPONSE
    # ----------------------------------------------------------
    def knows(self, word, language):
        nw = self.normalize_word(word)

        if language == "FR":
            vocab = self.vocab_FR
        elif language == "EN":
            vocab = self.vocab_EN
        elif language == "DE":
            vocab = self.vocab_DE
        else:
            return False, None

        if nw in vocab:
            return True, nw

        close = self.find_closest(nw, list(vocab))
        return (False, close) if close else (False, None)

# ----------------------------------------------------------
    #   SIGNAL WORD DETECTOR (détection matière)
    # ----------------------------------------------------------
    def signal_words_detector(self, words):
        sources = {
            "ScNat": "MATIERE/SCNAT/scnat.json",
            "EN": "MATIERE/EN/english.json",
            "DE_Kurz": "MATIERE/DE/de_kurzgeschichten.json",
            "FR_Verbe": "MATIERE/FR/fr_verbe.json",
            "FR_Vocab": "MATIERE/FR/fr_vocabulaire.json"
        }
        from MATIERE.MATH.math import math_base
        for matiere, chemin in sources.items():
            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except:
                continue

            # Pour chaque mot demandé
            for w in words:
                if w in data:   # mot détecté dans la matière
                    return matiere, w, data[w]

        return None, None, None
    
    def knowledge_question(self, words):
        # récupérer les mots sous forme simple
        w = set(words)

        # Exemple : élément chimique B
        if {"element", "b"} <= w:
            return "L’élément B du tableau périodique est le Bore (Boron)."

        # Exemple : 2+2
        if "2" in w and "2" in w and ("+" in w or "plus" in w):
            return "2 + 2 = 4"

        # Exemple : demander un élément chimique
        elements = {
            "h": "Hydrogène",
            "he": "Hélium",
            "li": "Lithium",
            "be": "Béryllium",
            "b": "Bore",
            "c": "Carbone",
            "n": "Azote",
            "o": "Oxygène",
            "f": "Fluor",
            "ne": "Néon"
        }

        # détecter : element X
        for w2 in words:
            if w2 in elements:
                return f"L’élément {w2.upper()} est {elements[w2]}."

        return None
    # ----------------------------------------------------------
    #   RÉPONSE AUTOMATIQUE
    # ---------------------------------------------------------
    def answer_generation(self, texte):
        # 3) Base de connaissances simple
        words = self.tokenize(texte)
        knowledge = self.knowledge_question(words)
        if knowledge:
            return knowledge

        if not words:
            return "Je n'ai rien compris."

        # 1. Détection de langue
        language = self.detect_language(words)

        if not language:
            return "Je ne comprends pas la langue de cette phrase."

        # 2. Vérifier si une matière spéciale est détectée
        matiere, mot_detecte, resultat = self.signal_words_detector(words)

        if matiere:
            return f"[{matiere}] Le mot « {mot_detecte} » signifie : {resultat}"

        # 3. Mots normaux
        mots_connus = []
        mots_proches = {}

        for w in words:
            known, match = self.knows(w, language)
            if known:
                mots_connus.append(w)
            elif match:
                mots_proches[w] = match

        # Réponse : mots reconnus
        if mots_connus:
            return f"[{language}] Je reconnais ces mots : {', '.join(mots_connus)}."

        # Réponse : corrections
        if mots_proches:
            corrections = [f"{w} → {c}" for w, c in mots_proches.items()]
            return f"[{language}] Tu voulais dire : " + ", ".join(corrections)

        # Rien
        return f"[{language}] Je ne comprends pas encore ce texte."


