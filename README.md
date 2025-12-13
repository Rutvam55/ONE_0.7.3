# ONE — Assistant d'entraînement (v0.10.1)

**ONE** est une application console éducative multi-matières écrite en Python. Ce projet propose des exercices en Français, Anglais, Deutsch, Math, Sciences Naturelles, Géographie et Histoire. Les progrès des joueurs sont sauvegardés dans un fichier JSON local (`DATA/sauvegarde.json`).

**But**: s'entraîner de façon ludique, suivre le XP et les niveaux par matière.

**Version**: v0.10.1

---

**Prérequis**

- Windows (tests réalisés sous Windows)
- Python 3.10 — 3.12 recommandé
- Pip

Librairies Python nécessaires (minimum):
- `pwinput` (pour la saisie sécurisée du mot de passe)

Installation rapide des dépendances (PowerShell) :

```powershell
python -m pip install --upgrade pip
python -m pip install pwinput
```

Remarque: le projet contient aussi des modules Kivy et des documents pédagogiques si tu veux créer une interface graphique — ces dépendances sont optionnelles.

---

**Lancer l'application**

Ouvrir PowerShell dans le dossier du projet (`ONE_Build`) puis :

```powershell
python .\main.py
```

Suivre les instructions à l'écran pour créer un joueur, vous connecter et lancer des exercices.

---

**Structure du dépôt (essentiel)**

- `main.py` : point d'entrée console principale.
- `CORE/` : code coeur (gestion des joueurs, exercices, sauvegarde, utilitaires).
  - `funk.py` : gestion des sauvegardes (`sauvegarde` class), migration et utilitaires XP.
  - `player.py` : classe `Player` (structure des statistiques).
  - `link.py` : loader de données et classes d'exercices (Math, Francais, ...).
  - `button.py` : gestion des boutons / sélection de matières.
- `DATA/` : données JSON et fichier `sauvegarde.json`.
- `KI/` : module IA (INLL) utilisé pour l'apprentissage adaptatif.
- `MATIERE/` : fichiers de contenu (vocabulaires, questions...)
- `EXPLICATION_SAUVEGARDE.md`, `KIVY_EXPLICATION_DETAILLEE.md` : documentation pédagogique.

---

**Sauvegarde et dépannage**

- Le fichier principal de sauvegarde est : `DATA\sauvegarde.json`.
- Pour vérifier que la sauvegarde fonctionne :
  1. Lancer `main.py`.
  2. Créer un compte (ou se connecter avec un compte existant).
  3. Jouer quelques questions dans un mode court.
  4. Ouvrir `DATA\sauvegarde.json` et vérifier que les champs `xp_...` et `parties_jouees_...` ont augmenté.

Si le fichier JSON est corrompu ou que tu veux repartir à zéro :

- Option 1 (réinitialiser) : supprimer `DATA\sauvegarde.json` (le programme le recréera au prochain enregistrement).
- Option 2 (debug) : ajouter des `print()` temporaires autour de `s.sauvegarder_auto(data)` pour vérifier que la fonction est appelée.

Permissions : si l'écriture échoue, assure-toi que ton compte utilisateur a les droits d'écriture sur le dossier `DATA`.

---

**Sécurité des mots de passe**

Actuellement les mots de passe sont stockés en clair dans `sauvegarde.json`. Pour plus de sécurité, il est recommandé de migrer vers un système de hachage (par ex. `bcrypt`). Si tu veux, je peux t'aider à :

- ajouter `bcrypt` comme dépendance ;
- migrer les comptes existants (détecter les mots de passe non hachés et les convertir lors de la prochaine connexion) ;
- mettre à jour `selectionner_joueur` pour vérifier les hachages.

---

**Tests**

Il n'y a pas encore de tests automatiques dans le dépôt. Pour commencer on peut ajouter des tests unitaires minimalistes avec `pytest` pour `CORE/funk.py` (migration, ajout de joueur, ajout XP et Level_up).

Exemple d'installation :

```powershell
python -m pip install pytest
```

Je peux générer un dossier `tests/` et quelques tests si tu veux.

---

**Bonnes pratiques et idées d'amélioration**

- Hacher les mots de passe (bcrypt).
- Centraliser la logique d'ajout XP (déjà partiellement fait dans `s.ajouter_xp`).
- Paramétrer les paliers de level-up via un fichier de config (JSON) plutôt que des +500 fixes.
- Ajouter des logs (`logging`) pour remplacer les `print()`.
- Extraire la configuration (couleurs, textes) dans `DATA/` et documenter la structure.
- Ajouter une interface graphique Kivy (optionnel) — il y a déjà des ressources dans le projet.

---

**Contribuer**

Si tu veux que je t'aide à :

- préparer une release `v0.10.1` (bump de version + changelog),
- ajouter tests unitaires,
- hacher les mots de passe,

réponds avec l'option choisie et je l'implémente.

---

# Auteur
- Rutvam55
