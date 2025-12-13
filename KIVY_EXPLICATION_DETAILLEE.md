# 📚 Guide complet du code Kivy - Explication détaillée

## Table des matières
1. [Imports](#imports)
2. [Configuration](#configuration)
3. [Classes Kivy](#classes-kivy)
4. [Structure de l'application](#structure)

---

## 📦 IMPORTS {#imports}

```python
import random
import os
```
- **`import random`** : Module standard Python pour générer des nombres/choix aléatoires
  - Utilisé pour : `random.choice()` - sélectionner un élément aléatoire dans une liste
  
- **`import os`** : Module pour interagir avec le système d'exploitation
  - Utilisé pour : Chemins de fichiers, vérifier si des fichiers existent

---

### Imports Kivy - Les briques de base

```python
from kivy.app import App
```
- **`App`** : Classe principale de TOUTE application Kivy
- C'est la **base de l'application**
- Elle lance la fenêtre et gère le cycle de vie
- **Analogie** : C'est le "responsable" de l'application

```python
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
```
- **`Screen`** : Une page/écran de l'application
  - Exemple : Écran de connexion, menu principal, jeu, etc.
  - Chaque `Screen` est une classe séparée
  
- **`ScreenManager`** : Gestionnaire d'écrans
  - Gère le passage d'un écran à l'autre
  - **Exemple** : `manager.current = 'menu'` va vers l'écran "menu"
  
- **`NoTransition`** : Pas d'animation entre écrans
  - Les écrans changent instantanément (pas de fondu/glissement)

```python
from kivy.uix.boxlayout import BoxLayout
```
- **`BoxLayout`** : Conteneur qui arrange les éléments en ligne ou colonne
- **Orientation** : 
  - `orientation='vertical'` : arrange verticalement (de haut en bas)
  - `orientation='horizontal'` : arrange horizontalement (de gauche à droite)
- **Analogie** : C'est comme une boîte qui place les enfants les uns après les autres

```python
from kivy.uix.gridlayout import GridLayout
```
- **`GridLayout`** : Arrange les éléments en grille (tableau)
- **`cols=2`** : 2 colonnes
- **Analogie** : C'est comme un tableau Excel

```python
from kivy.uix.scrollview import ScrollView
```
- **`ScrollView`** : Permet de défiler quand le contenu est trop grand
- **Exemple** : Liste d'éléments qui ne rentre pas à l'écran

```python
from kivy.uix.label import Label
```
- **`Label`** : Un texte simple (non modifiable)
- **Analogie** : C'est comme écrire du texte sur un papier

```python
from kivy.uix.button import Button
```
- **`Button`** : Bouton cliquable
- **Utilisation** : `button.bind(on_press=ma_fonction)` pour faire quelque chose au clic

```python
from kivy.uix.textinput import TextInput
```
- **`TextInput`** : Zone de saisie texte
- **Propriétés** :
  - `text` : le texte saisi
  - `hint_text` : placeholder (texte gris de suggestion)
  - `password=True` : masquer les caractères (pour les mots de passe)
  - `multiline=False` : une seule ligne (True = plusieurs lignes)

```python
from kivy.uix.popup import Popup
```
- **`Popup`** : Fenêtre modale (boîte de dialogue)
- **Exemple** : Message d'erreur qui apparaît au-dessus
- **Utilisation** : `popup.open()` pour afficher, `popup.dismiss()` pour fermer

```python
from kivy.uix.spinner import Spinner
```
- **`Spinner`** : Menu déroulant
- **Exemple** : Sélectionner une langue
- **Propriétés** : `values=('Option1', 'Option2', 'Option3')`

```python
from kivy.uix.checkbox import CheckBox
```
- **`CheckBox`** : Case à cocher
- **Propriété** : `active=True/False`
- **Exemple** : Sélectionner plusieurs jeux

```python
from kivy.core.window import Window
```
- **`Window`** : Fenêtre de l'application
- **Utilisations** :
  - `Window.size = (1280, 720)` : taille de la fenêtre
  - `Window.title = "ONE"` : titre de la fenêtre

```python
from kivy.graphics import Color, RoundedRectangle
```
- **`Color`** : Définir une couleur (RGBA)
  - Format : `(R, G, B, A)` avec valeurs de 0 à 1
  - **Exemple** : `Color(0.2, 0.6, 0.9, 1)` = bleu
  
- **`RoundedRectangle`** : Rectangle arrondi (pour les arrière-plans)

```python
from kivy.clock import Clock
```
- **`Clock`** : Gestion du temps dans Kivy
- **Utilisations** :
  - `Clock.schedule_once(fonction, délai)` : appel une fois après délai
  - `Clock.schedule_interval(fonction, intervalle)` : appel répété

---

### Imports du projet

```python
from CORE.link import set_player, DataLoader
```
- **`set_player(player)`** : Stocke le joueur connecté globalement
- **`DataLoader`** : Classe pour charger les données (vocabulaires, etc.)

```python
from CORE.funk import sauvegarde
```
- **`sauvegarde()`** : Classe pour gérer la sauvegarde des données

```python
from CORE.button import Button as GameButton
```
- **`GameButton`** : Classe pour gérer la sélection des jeux
- **Renommée en `GameButton`** pour éviter confusion avec `Button` de Kivy

```python
from KI.ia import IA
```
- **`IA()`** : Classe pour l'intelligence artificielle

---

## ⚙️ CONFIGURATION {#configuration}

```python
Window.size = (1280, 720)
```
- **Définit la taille de la fenêtre** : 1280 pixels de large, 720 pixels de haut
- Les résolutions courantes : 1280x720 (HD), 1920x1080 (Full HD), 800x600 (petit)

```python
Window.title = "ONE - Plateforme d'apprentissage"
```
- **Titre affiché en haut de la fenêtre**

```python
VERSION = "0.10.0"
```
- **Numéro de version** de l'application
- Format : `X.Y.Z` (majeur.mineur.patch)

```python
global_player = None
global_data = None
global_sauvegarde = None
```
- **Variables globales** pour stocker les données
- Initialisées à `None` (vide)
- **Pourquoi global ?** Plusieurs écrans ont besoin d'y accéder

---

### Thème de couleurs

```python
THEME = {
    'primary': (0.2, 0.6, 0.9, 1),      # Bleu
    'secondary': (0.9, 0.4, 0.6, 1),    # Rose
    'success': (0.2, 0.8, 0.4, 1),      # Vert
    'danger': (0.9, 0.3, 0.3, 1),       # Rouge
    'warning': (1, 0.7, 0.2, 1),        # Orange
}
```

**Format RGBA** :
- **R** (Red) : 0 = noir, 1 = rouge pur
- **G** (Green) : 0 = noir, 1 = vert pur
- **B** (Blue) : 0 = noir, 1 = bleu pur
- **A** (Alpha) : 0 = transparent, 1 = opaque

**Exemple** :
- `(0.2, 0.6, 0.9, 1)` = peu de rouge + beaucoup de vert + beaucoup de bleu = **BLEU**
- `(1, 0, 0, 1)` = rouge pur
- `(1, 1, 1, 1)` = blanc
- `(0, 0, 0, 1)` = noir

**Utilisation** :
```python
button = Button(background_color=THEME['primary'])  # Bouton bleu
```

---

## 🎨 CLASSES KIVY {#classes-kivy}

### Structure de base d'une classe Screen

```python
class LoginScreen(Screen):
    """Écran de connexion"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sauvegarde = sauvegarde()
        self.build_ui()
```

**Ligne par ligne** :
- **`class LoginScreen(Screen):`** : Crée une nouvelle classe qui hérite de `Screen`
  - **Héritage** : LoginScreen reprend toutes les capacités de Screen
  
- **`def __init__(self, **kwargs):`** : Constructeur (appelé à la création)
  - **`self`** : référence à l'objet lui-même
  - **`**kwargs`** : arguments optionnels (passage de paramètres à Screen)
  
- **`super().__init__(**kwargs)`** : Appelle le constructeur de la classe parent
  - **`super()`** = accéder à la classe parent (Screen)
  - **Important** : Doit être appelé en premier
  
- **`self.sauvegarde = sauvegarde()`** : Crée une instance de sauvegarde
  - **`self.sauvegarde`** : variable de l'instance (propre à LoginScreen)
  - Permet d'accéder dans toutes les méthodes
  
- **`self.build_ui()`** : Appelle la méthode pour construire l'interface

---

## 🏗️ Structure d'une interface {#structure}

### Exemple simple : Écran de connexion

```python
def build_ui(self):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
```

**Décryption** :
- **`layout = BoxLayout(...)`** : Crée un conteneur vertical
  - **`orientation='vertical'`** : arrange de haut en bas
  - **`padding=20`** : 20 pixels d'espace autour (marge intérieure)
  - **`spacing=20`** : 20 pixels entre chaque élément
  
**Visualisation** :
```
┌─────────────────────────┐
│ padding=20 (marge)      │
│ ┌───────────────────┐   │
│ │  Élément 1        │   │
│ └───────────────────┘   │
│   spacing=20 (espace)   │
│ ┌───────────────────┐   │
│ │  Élément 2        │   │
│ └───────────────────┘   │
│ padding=20 (marge)      │
└─────────────────────────┘
```

---

### Ajouter du contenu

```python
title = Label(
    text='ONE',
    font_size='48sp',
    bold=True,
    color=THEME['primary'],
    size_hint_y=0.2
)
layout.add_widget(title)
```

**Explication** :
- **`Label(...)`** : Crée un label (texte)
  - **`text='ONE'`** : Le texte à afficher
  - **`font_size='48sp'`** : Taille : 48 scale-points (proportionnel à l'écran)
  - **`bold=True`** : Texte en gras
  - **`color=THEME['primary']`** : Couleur = bleu (du thème)
  - **`size_hint_y=0.2`** : Prend 20% de la hauteur disponible
  
- **`layout.add_widget(title)`** : Ajoute le label au conteneur

---

### Input de texte

```python
self.username_input = TextInput(
    hint_text='Entrez votre nom',
    multiline=False,
    size_hint_y=0.15
)
layout.add_widget(self.username_input)
```

**Explication** :
- **`TextInput(...)`** : Zone de saisie texte
  - **`hint_text='Entrez votre nom'`** : Placeholder (conseil affiché en gris)
  - **`multiline=False`** : Une seule ligne (True = plusieurs)
  - **`size_hint_y=0.15`** : Prend 15% de la hauteur
  
- **`self.username_input`** : Stocké en variable
  - Permet d'accéder au texte plus tard : `self.username_input.text`

---

## 🔘 Gestion des boutons

```python
login_btn = Button(
    text='Connexion',
    background_color=THEME['primary']
)
login_btn.bind(on_press=self.login)
button_layout.add_widget(login_btn)
```

**Explication** :
- **`Button(...)`** : Crée un bouton
  - **`text='Connexion'`** : Texte du bouton
  - **`background_color=THEME['primary']`** : Couleur bleu
  
- **`login_btn.bind(on_press=self.login)`** : Lie l'action au clic
  - **`bind`** : associer un événement à une fonction
  - **`on_press`** : l'événement du clic
  - **`self.login`** : la fonction à appeler au clic
  
- **`button_layout.add_widget(login_btn)`** : Ajoute le bouton

**Comment fonctionne le bind** :
```python
# Quand l'utilisateur clique sur le bouton
# → Kivy appelle : self.login(instance)
# → instance = le bouton qui a été cliqué
```

---

## 📋 Fonction de connexion

```python
def login(self, instance):
    """Tentative de connexion"""
    global global_player, global_data, global_sauvegarde
```

**Explication** :
- **`def login(self, instance):`** : Fonction appelée au clic du bouton
  - **`self`** : l'objet LoginScreen
  - **`instance`** : le bouton qui a été cliqué
  
- **`global global_player, ...`** : Dire à Python d'utiliser les variables globales
  - **Important** : Sans `global`, Python crée des variables locales
  
```python
username = self.username_input.text.strip()
password = self.password_input.text.strip()
```

**Explication** :
- **`self.username_input.text`** : Récupère le texte saisi
- **`.strip()`** : Enlève les espaces au début et à la fin
  - **Exemple** : `"  Jean  ".strip()` → `"Jean"`

---

## ✅ Validation des données

```python
if not username or not password:
    self.error_label.text = '⚠️ Veuillez remplir tous les champs'
    return
```

**Explication** :
- **`if not username`** : Vérifie si le nom est vide
  - `not ""` → `True` (vide = True)
  - `not "Jean"` → `False` (pas vide = False)
  
- **`or`** : Condition OU (si l'une est vraie, la condition est vraie)
  
- **`self.error_label.text = '...'`** : Affiche le message d'erreur
  
- **`return`** : Arrête la fonction immédiatement

---

## 🔐 Authentification

```python
self.data = self.sauvegarde.charger_sauvegarde(None)
player, password_correct = self.sauvegarde.selectionner_joueur(
    self.data, username, password
)
```

**Explication** :
- **`self.sauvegarde.charger_sauvegarde(None)`** : Charge les données sauvegardées
  - Retourne un dictionnaire avec tous les joueurs
  
- **`self.sauvegarde.selectionner_joueur(...)`** : Cherche le joueur
  - **Retourne 2 valeurs** :
    - **`player`** : Les données du joueur (ou None)
    - **`password_correct`** : True si le mot de passe est correct

---

## 🎯 Navigation entre écrans

```python
if password_correct:
    global_player = player
    global_data = self.data
    global_sauvegarde = self.sauvegarde
    set_player(player)
    self.manager.current = 'menu'
```

**Explication** :
- **Stocker les données globales** :
  - `global_player = player` : Sauvegarde le joueur pour tous les écrans
  
- **`set_player(player)`** : Informe aussi la classe DataLoader
  - Permet aux exercices d'accéder au joueur
  
- **`self.manager.current = 'menu'`** : Change d'écran
  - **`self.manager`** : Le ScreenManager (gestionnaire d'écrans)
  - **`.current = 'menu'`** : Affiche l'écran nommé 'menu'

**Comment les écrans sont nommés** :
```python
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainMenuScreen(name='menu'))
# → Puis naviguer avec self.manager.current = 'login'
```

---

## 🏠 Écran du menu principal

```python
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
```

**Structure identique** aux autres écrans.

```python
menu_layout = GridLayout(cols=2, spacing=20, size_hint_y=0.7)
```

**Explication** :
- **`GridLayout(cols=2, ...)`** : Grille avec 2 colonnes
- **`spacing=20`** : 20 pixels entre les éléments
- **`size_hint_y=0.7`** : Prend 70% de la hauteur

**Visualisation** :
```
┌─────────────────────────┐
│  ┌────────┐ ┌────────┐  │
│  │Bouton1 │ │Bouton2 │  │
│  └────────┘ └────────┘  │
│  ┌────────┐ ┌────────┐  │
│  │Bouton3 │ │Bouton4 │  │
│  └────────┘ └────────┘  │
└─────────────────────────┘
```

---

## 🎮 Gestion des événements

```python
buttons_data = [
    ('Commencer', 'play', THEME['success']),
    ('Paramètres', 'settings', THEME['primary']),
]

for text, action, color in buttons_data:
    btn = Button(text=text, background_color=color)
    btn.bind(on_press=lambda x, a=action: self.on_menu_button(a))
    menu_layout.add_widget(btn)
```

**Explication** :
- **`for text, action, color in buttons_data:`** : Boucle sur chaque tuple
  - **Dépaquetage** : `('Commencer', 'play', THEME['success'])` → `text, action, color`
  
- **`lambda x, a=action: self.on_menu_button(a)`** : Fonction anonyme
  - **`lambda`** : Fonction sans nom
  - **`x`** : L'instance du bouton (ignorée)
  - **`a=action`** : Capture `action` à ce moment
  - **`self.on_menu_button(a)`** : Appelle la fonction avec `action`
  
**Pourquoi `lambda`** ?
```python
# ❌ SANS lambda - tous les boutons appelleraient 'play'
for ...:
    btn.bind(on_press=self.on_menu_button(action))  # action = dernière valeur!

# ✅ AVEC lambda - chaque bouton a sa propre action
for ...:
    btn.bind(on_press=lambda x, a=action: self.on_menu_button(a))
```

---

## 🔄 Variables d'instance vs variables locales

```python
class LoginScreen(Screen):
    def __init__(self):
        self.username_input = TextInput(...)  # Variable d'instance
        
    def login(self):
        username = self.username_input.text  # Accès à la variable d'instance
```

**Différences** :
- **`self.username_input`** : **Variable d'instance**
  - Appartient à l'objet
  - Accessible dans TOUTES les méthodes
  - Vit tant que l'objet existe
  
- **`username`** : **Variable locale**
  - Existe seulement dans la fonction
  - Disparaît à la fin de la fonction
  - Autres fonctions ne peuvent pas y accéder

---

## ⏱️ Utilisation de Clock

```python
Clock.schedule_once(lambda dt: self.load_next_question(), 1)
```

**Explication** :
- **`Clock.schedule_once(..., 1)`** : Appelle la fonction après 1 seconde
  - **`1`** : Délai en secondes
  - **`lambda dt: ...`** : Fonction anonyme (Clock passe un argument `dt`)
  
**Autres utilisations** :
```python
# Appeler chaque seconde
Clock.schedule_interval(fonction, 1)

# Appeler après 0.5 secondes
Clock.schedule_once(fonction, 0.5)

# Arrêter un événement programmé
Clock.unschedule(fonction)
```

---

## 🎨 Utilisation du Markup (texte formaté)

```python
self.feedback_label.text = '[color=00ff00]✅ Correct![/color]'
```

**Explication** :
- **Markup Kivy** : Format pour colorer/styliser du texte
  - **`[color=00ff00]`** : Début couleur verte (hex: 00FF00)
  - **`[/color]`** : Fin de la couleur
  
**Autres formats** :
```python
'[b]Texte gras[/b]'
'[i]Texte italique[/i]'
'[u]Texte souligné[/u]'
'[color=ff0000]Texte rouge[/color]'
'[size=20sp]Texte grande taille[/size]'
```

**Important** : Le label doit avoir `markup=True` pour activer cela :
```python
label = Label(text='...', markup=True)
```

---

## 🗂️ Structure complète de l'application

```python
class OneApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        # ... autres écrans
        
        return sm

if __name__ == '__main__':
    OneApp().run()
```

**Explication** :
- **`class OneApp(App):`** : Classe principale de l'app (hérite d'App)
  
- **`def build(self):`** : Méthode appelée au démarrage
  - **Doit retourner** le widget racine (ScreenManager)
  
- **`sm = ScreenManager(...)`** : Crée le gestionnaire d'écrans
  - **`transition=NoTransition()`** : Pas d'animation
  
- **`sm.add_widget(...)`** : Ajoute chaque écran
  - **`name='login'`** : Identifiant unique pour naviguer
  
- **`if __name__ == '__main__':`** : Vérifie qu'on lance le script directement
  - **`OneApp().run()`** : Crée et lance l'app

---

## 📝 Résumé des concepts clés

| Concept | Explication | Exemple |
|---------|------------|---------|
| **Screen** | Une page/écran | LoginScreen, MainMenuScreen |
| **Widget** | Un élément UI | Button, Label, TextInput |
| **Layout** | Conteneur qui arrange des widgets | BoxLayout, GridLayout |
| **bind** | Lier un événement à une fonction | `button.bind(on_press=fonction)` |
| **add_widget** | Ajouter un widget à un layout | `layout.add_widget(button)` |
| **self** | Référence à l'objet lui-même | `self.username_input` |
| **super()** | Accéder à la classe parent | `super().__init__(**kwargs)` |
| **global** | Utiliser une variable globale | `global global_player` |
| **lambda** | Fonction anonyme | `lambda x: print(x)` |
| **RGBA** | Format couleur (0 à 1) | `(0.2, 0.6, 0.9, 1)` |

---

## 🎓 Exercices pour apprendre

### Exercice 1 : Ajouter un bouton
Ajoutez un bouton "Quitter" qui ferme l'app dans MainMenuScreen.

**Indice** :
```python
from kivy.app import App

quit_btn = Button(text='Quitter', background_color=THEME['danger'])
quit_btn.bind(on_press=App.get_running_app().stop)
```

### Exercice 2 : Changer de couleur
Modifiez la couleur d'un label au clic d'un bouton.

**Indice** :
```python
def change_color(self, instance):
    self.label.color = THEME['success']  # RGBA tuple
```

### Exercice 3 : Ajouter un champ
Ajoutez un champ email à l'écran de connexion avec validation.

---

## 📖 Pour aller plus loin

- **Documentation Kivy** : https://kivy.org/doc/
- **Kivy Garden** : Packages additionnels
- **Événements** : `on_press`, `on_release`, `on_text`, `on_touch_down`, etc.
- **Propriétés** : `text`, `size`, `pos`, `color`, `disabled`, etc.

---

Avez-vous des questions sur une partie spécifique ? 🎯
