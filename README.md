# ONE - 🚀 L'outil d'apprentissage en ligne de commande

## 🌟 À propos de ONE

**ONE** (Version 0.7.3) est une application développée entièrement en **Python** pour le terminal. Son objectif est simple : vous aider à réviser et à apprendre de nouvelles notions dans plusieurs matières de manière interactive.

Le nom "ONE" vient de l'idée d'un outil **unique** pour l'apprentissage.

### 📚 Matières Actuellement Disponibles :

* **Math** (Exercices de base : addition, soustraction, etc.)
* **Anglais** (Vocabulaire)
* **Français** (Vocabulaire)
* **Deutsch (Allemand)** (Caractéristiques des nouvelles courtes)
* **Sc. Nat. (Sciences Naturelles)** (Tableau périodique des éléments)

## 💻 Installation et Utilisation

### Prérequis

Pour utiliser ONE, vous devez avoir **Python** (version 3.x recommandée) installé sur votre ordinateur.

### ⚙️ Lancement de l'application

Suivez ces étapes simples pour démarrer ONE :

1.  **Télécharger le Code :**
    * Soit vous téléchargez le dossier complet du projet.
    * Soit vous utilisez Git (si installé) :
        ```bash
        git clone [Votre lien GitHub ici]
        cd ONE 
        ```

2.  **Lancer le programme :**
    * Ouvrez votre terminal (ou invite de commande).
    * Allez dans le dossier du projet `ONE` (si ce n'est pas déjà fait).
    * Exécutez l'application avec la commande :
        ```bash
        python main.py
        ```

3.  **Connexion :** Lors du premier lancement, vous serez invité à entrer un nom et un mot de passe. Si c'est un nouveau nom, un profil sera **automatiquement créé** (grâce à votre fonction de sauvegarde !).

---

## 🛠️ Structure du Projet

* `main.py` : Le fichier principal qui gère le menu et l'exécution.
* `def_sauv.py` : Contient toutes les fonctions de gestion des joueurs (sauvegarde, chargement, montée de niveau).
* `link.py` : Lie les fonctions de matière au programme principal.
* `MATIERE/` : **(Dossier)** Contient les fichiers Python spécifiques à chaque matière (`math.py`, `anglais.py`, etc.).
* `.gitignore` : Liste les fichiers à ne pas inclure sur GitHub (comme `sauvegarde.json` et les fichiers temporaires).

---

## 🤝 Contribuer au Projet

Ce projet est encore en développement (Version 0.7.3) ! Si vous avez des idées pour de nouvelles matières, des améliorations de code, ou si vous trouvez un bug, n'hésitez pas à :

1.  Ouvrir une **Issue** (Problème) sur GitHub.
2.  Proposer des changements via une **Pull Request**.

---

## 📝 Auteur

* par Rutvam55

