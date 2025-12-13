# 📚 Explication complète du système de sauvegarde

## 🔍 Comment fonctionne la sauvegarde ?

### 1️⃣ **La classe `sauvegarde` - Vue d'ensemble**

```python
class sauvegarde:
    def __init__(self):
        self.ROOT = Path(__file__).parent.parent
        self.DEFAULT_SAVE_FILE = self.ROOT / "DATA" / "sauvegarde.json"
```

**Explication ligne par ligne** :

- **`class sauvegarde:`** : Définit une classe pour gérer les sauvegardes
  - **Classe** = groupe de fonctions et données liées

- **`def __init__(self):`** : Constructeur (appelé à la création)
  - **Appelé automatiquement** quand on fait `sauvegarde()`

- **`self.ROOT = Path(__file__).parent.parent`** : Trouve le répertoire racine
  - **`__file__`** = chemin du fichier courant (funk.py)
  - **`Path(...)`** = objet chemin Python
  - **`.parent`** = dossier parent
  - **`.parent.parent`** = grand-parent
  - **Exemple** : `funk.py` → `CORE` → `ONE_Build` ✅
  
- **`self.DEFAULT_SAVE_FILE = self.ROOT / "DATA" / "sauvegarde.json"`** : Définit le chemin
  - **`/`** = opérateur de concaténation de chemins
  - **Résultat** : `ONE_Build/DATA/sauvegarde.json`

---

## 💾 Fonction 1 : `charger_sauvegarde()`

```python
def charger_sauvegarde(self, chemin_json: str | Path | None = None):
    """Charge la sauvegarde si elle existe, sinon renvoie une structure vide."""
```

### Paramètre

- **`chemin_json: str | Path | None = None`**
  - **`str | Path | None`** = accepte 3 types
    - Chaîne de caractères (`"DATA/sauvegarde.json"`)
    - Objet Path (`Path("DATA/sauvegarde.json")`)
    - Rien (`None`)
  - **`= None`** = valeur par défaut (optionnel)

### Corps de la fonction

```python
if chemin_json is None:
    chemin = self.DEFAULT_SAVE_FILE
else:
    chemin = Path(chemin_json)
```

**Explication** :
- **Si le chemin est vide** → utiliser le chemin par défaut
- **Sinon** → utiliser le chemin fourni

```python
if chemin.exists():
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
```

**Explication** :
- **`chemin.exists()`** : Vérifie si le fichier existe
  - Retourne `True` ou `False`
  
- **`with open(chemin, "r", encoding="utf-8")`** : Ouvre le fichier
  - **`"r"`** = lecture (read)
  - **`encoding="utf-8"`** = accepte les accents
  - **`with`** = ferme automatiquement après
  
- **`json.load(fichier)`** : Lit le JSON
  - Convertit JSON → dictionnaire Python

```python
except json.JSONDecodeError:
    print("Erreur : fichier de sauvegarde corrompu. Réinitialisation.")
    return {"players": {}}
```

**Explication** :
- **`except`** : Si une erreur se produit
- **`json.JSONDecodeError`** = le fichier n'est pas du JSON valide
- **Retour** : Un dictionnaire vide avec structure vide

```python
return {"players": {}}
```

**Cas où le fichier n'existe pas** : Retourne une structure vide

---

## 💾 Fonction 2 : `sauvegarder_auto()`

### ❓ C'EST LA PLUS IMPORTANTE POUR VOUS !

```python
def sauvegarder_auto(self, donnees, chemin_json: str | Path | None = None):
    """Écrit automatiquement les données actuelles dans le fichier JSON."""
```

**Explication** :
- **`donnees`** = les données à sauvegarder (dictionnaire)
- **`chemin_json`** = où sauvegarder (optionnel)

```python
if chemin_json is None:
    chemin = self.DEFAULT_SAVE_FILE
else:
    chemin = Path(chemin_json)
```

**Same as above** : Même logique

```python
chemin.parent.mkdir(parents=True, exist_ok=True)
```

**⚠️ IMPORTANT** :
- **`chemin.parent`** = le dossier contenant le fichier
  - Exemple : chemin = `/DATA/sauvegarde.json` → parent = `/DATA`
  
- **`mkdir(...)`** = créer le dossier
  - **`parents=True`** = créer aussi les dossiers parents s'ils manquent
  - **`exist_ok=True`** = ne pas errorer si le dossier existe
  
**Pourquoi ?** Sinon, si `/DATA` n'existe pas, ça crash !

```python
with open(chemin, "w", encoding="utf-8") as fichier:
    json.dump(donnees, fichier, indent=4, ensure_ascii=False)
```

**Explication** :
- **`"w"`** = écriture (write)
  - Crée le fichier s'il n'existe pas
  - Écrase s'il existe
  
- **`json.dump(donnees, fichier, ...)`** : Écrit en JSON
  - **`donnees`** = ce qu'on écrit
  - **`fichier`** = où on écrit
  - **`indent=4`** = indentation pour la lisibilité
  - **`ensure_ascii=False`** = accepte les accents

---

## 🔐 Fonction 3 : `ajouter_joueur()`

```python
def ajouter_joueur(self, donnees, nom, mot_de_passe):
    """Ajoute un nouveau player avec des données par défaut."""
```

**Explication** :
- **`donnees`** = le dictionnaire existant
- **`nom`** = nom du joueur
- **`mot_de_passe`** = le mot de passe

```python
if nom in donnees.get("players", {}):
    print("Ce player existe déjà.")
    return False
```

**Explication** :
- **`donnees.get("players", {})`** : Récupère les joueurs (ou dict vide)
  - **`.get(...)`** = accès sûr (ne crash pas)
  
- **`if nom in ...:`** : Vérifie si le joueur existe
- **`return False`** : Arrête et retourne False (erreur)

```python
donnees.setdefault("players", {})
donnees["players"][nom] = { ... }
return True
```

**Explication** :
- **`setdefault("players", {})`** : Crée "players" s'il manque
- **Ajoute** le nouveau joueur
- **`return True`** : Succès !

---

## 🎯 POURQUOI ÇA NE SAUVEGARDE PAS ?

### ✅ Checklist de diagnostic

#### 1️⃣ Le dossier `DATA` existe-t-il ?

```
ONE_Build/
├── DATA/           ← DOIT EXISTER
│   └── sauvegarde.json
├── CORE/
├── KI/
└── ...
```

**Comment vérifier** :
```powershell
# Depuis ONE_Build
Test-Path "DATA"
Test-Path "DATA\sauvegarde.json"
```

**Si manquant** : Créer le dossier
```powershell
mkdir DATA
```

---

#### 2️⃣ Vous appelez `sauvegarder_auto()` ?

**❌ ERREUR COURANTE** :
```python
s = sauvegarde()
data = s.charger_sauvegarde(None)
# Vous modifiez data...
# MAIS vous n'appelez PAS sauvegarder_auto() !
```

**✅ CORRECT** :
```python
s = sauvegarde()
data = s.charger_sauvegarde(None)
# Vous modifiez data...
s.sauvegarder_auto(data)  # ← IMPORTANT !
```

---

#### 3️⃣ Dans quelle situation ?

```python
# ✅ EXEMPLE: Création de compte
if s.ajouter_joueur(data, nom, mdp):
    s.sauvegarder_auto(data)  # SAUVEGARDER APRÈS !
```

```python
# ✅ EXEMPLE: Modification XP
player['Francais']['xp_Francais'] += 50
s.sauvegarder_auto(data)  # SAUVEGARDER APRÈS !
```

---

#### 4️⃣ Erreurs d'écriture ?

Ajoutez du debugging :

```python
def sauvegarder_auto(self, donnees, chemin_json=None):
    if chemin_json is None:
        chemin = self.DEFAULT_SAVE_FILE
    else:
        chemin = Path(chemin_json)
    
    print(f"📝 Tentative de sauvegarde à: {chemin}")
    
    try:
        chemin.parent.mkdir(parents=True, exist_ok=True)
        print(f"✅ Dossier {chemin.parent} créé/vérifié")
        
        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        
        print(f"✅ Fichier sauvegardé avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")
```

---

## 📋 Exemple complet de sauvegarde

```python
# 1. Créer une instance
s = sauvegarde()

# 2. Charger les données existantes
data = s.charger_sauvegarde(None)
print(f"Données chargées: {data}")

# 3. Ajouter un joueur
if s.ajouter_joueur(data, "Jean", "password123"):
    print("✅ Joueur créé")
    
    # 4. SAUVEGARDER !
    s.sauvegarder_auto(data)
    print("✅ Sauvegardé!")
else:
    print("❌ Joueur existe déjà")

# 5. Vérifier que c'est sauvegardé
data2 = s.charger_sauvegarde(None)
print(f"Données rechargées: {data2}")

if "Jean" in data2.get("players", {}):
    print("✅✅ La sauvegarde fonctionne!")
else:
    print("❌❌ La sauvegarde NE fonctionne pas!")
```

---

## 🐛 Problèmes courants

### Problème 1 : "Le fichier n'existe pas"

**Cause** : Le dossier `DATA` manque

**Solution** :
```powershell
# Créer le dossier
mkdir DATA

# Vérifier
ls DATA
```

---

### Problème 2 : "Erreur d'accès"

**Cause** : Permissions insuffisantes

**Solution** :
```powershell
# Vérifier les permissions
Get-Item DATA | Select-Object

# Ou relancer en admin
# Clic droit → "Run as Administrator"
```

---

### Problème 3 : "Le fichier reste vide"

**Cause** : Vous n'appelez pas `sauvegarder_auto()`

**Solution** :
```python
# ❌ AVANT
data = s.charger_sauvegarde(None)
s.ajouter_joueur(data, "Jean", "mdp")

# ✅ APRÈS
data = s.charger_sauvegarde(None)
s.ajouter_joueur(data, "Jean", "mdp")
s.sauvegarder_auto(data)  # ← AJOUTEZ CETTE LIGNE !
```

---

### Problème 4 : "Le JSON est mal formaté"

**Cause** : Mauvaises données

**Solution** :
```python
# Vérifier les données
import json
with open("DATA/sauvegarde.json", "r") as f:
    try:
        data = json.load(f)
        print("✅ JSON valide")
    except json.JSONDecodeError as e:
        print(f"❌ JSON invalide: {e}")
```

---

## 🔄 Flux complet de sauvegarde

```
┌─────────────────────────────────────────┐
│ 1. Créer instance: s = sauvegarde()    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│ 2. Charger: data = s.charger_...()     │
│    Retourne: {"players": {...}}        │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│ 3. Modifier data                        │
│    data["players"]["Jean"] = {...}     │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│ 4. Sauvegarder: s.sauvegarder_auto(data)│
│    Écrit dans: DATA/sauvegarde.json    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│ 5. Vérifier: Ouvrir le fichier JSON    │
│    et vérifier que les données sont là │
└─────────────────────────────────────────┘
```

---

## 🎯 Résumé rapide

| Action | Code | Pourquoi |
|--------|------|---------|
| **Charger** | `data = s.charger_sauvegarde()` | Récupérer les données existantes |
| **Modifier** | `data["players"]["Jean"]["xp_Francais"] = 100` | Changer quelque chose |
| **Sauvegarder** | `s.sauvegarder_auto(data)` | **OBLIGATOIRE** pour écrire dans le fichier |
| **Vérifier** | `data2 = s.charger_sauvegarde()` | Confirmer que c'est sauvegardé |

---

## ❓ Avez-vous un exemple spécifique où ça ne marche pas ?

Donnez-moi le code que vous utilisez et je pourrais identifier le problème ! 🔍
