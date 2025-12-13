import random
import os
from CORE.input_v import CI
from CORE.dataloader import DataLoader
from CORE.exercise import Exercise
from CORE.funk import sauvegarde, controller_int
from CORE.player import Player
from CORE.button import Button
from CORE.langue import langue
from CORE.couleur import Couleur
from MATIERE.ANGLAIS.anglais import Anglais
from MATIERE.DEUTSCH.deutsch import Deutsch
from MATIERE.FRANCAIS.francais import Francais
from MATIERE.GEO.geo import Geo
from MATIERE.MATH.math import Math
from MATIERE.SCNAT.scnat import ScNat
from MATIERE.HISTO.histo import Histo
from KI.ia import IA

# Global variable for player
player = None

# Get the base directory for file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def set_player(p):
    """Set the global player variable from main.py"""
    global player
    player = p

ci = None
Data_Loader = None
Ex = None
Ang = None
Deu = None
Fra = None
Geog = None
Mat = None
Scn = None
His = None
s = None
buttons = None
ia = None
couleurs = None


def get_ci():
    global ci
    if ci is None:
        ci = CI()
    return ci


def get_data_loader():
    global Data_Loader
    if Data_Loader is None:
        Data_Loader = DataLoader()
    return Data_Loader


def get_exercise():
    global Ex
    if Ex is None:
        Ex = Exercise()
    return Ex


def get_anglais():
    global Ang
    if Ang is None:
        Ang = Anglais()
    return Ang


def get_deutsch():
    global Deu
    if Deu is None:
        Deu = Deutsch()
    return Deu


def get_francais():
    global Fra
    if Fra is None:
        Fra = Francais()
    return Fra


def get_geo():
    global Geog
    if Geog is None:
        Geog = Geo()
    return Geog


def get_math():
    global Mat
    if Mat is None:
        Mat = Math()
    return Mat


def get_scnat():
    global Scn
    if Scn is None:
        Scn = ScNat()
    return Scn


def get_histo():
    global His
    if His is None:
        His = Histo()
    return His


def get_sauvegarde():
    global s
    if s is None:
        s = sauvegarde()
    return s


def get_buttons():
    global buttons
    if buttons is None:
        buttons = Button()
    return buttons


def get_ia():
    global ia
    if ia is None:
        ia = IA()
    return ia


def get_couleurs():
    global couleurs
    if couleurs is None:
        couleurs = Couleur()
    return couleurs