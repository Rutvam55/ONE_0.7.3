import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DataLoader:
    """Class for loading data from JSON files"""

    ENCODING = "utf-8"

    @staticmethod
    def get_path(relative_path):
        """Get absolute path from relative path"""
        return os.path.join(BASE_DIR, relative_path)

    @staticmethod
    def load_data(subject):
        """Load data according to the specified subject"""
        if subject == "EN":
            return DataLoader._load_english()
        elif subject == "FR":
            return DataLoader._load_french()
        elif subject == "DE":
            return DataLoader._load_german()
        elif subject == "ScNat":
            return DataLoader._load_scnat()
        elif subject == "Math":
            return DataLoader._load_math()
        elif subject == "Geo":
            return DataLoader._load_geography()
        elif subject == "Histo":
            return DataLoader._load_histo()
        elif subject == "COLOR":
            return DataLoader._load_color()

    @staticmethod
    def _load_english():
        """Load English vocabulary data"""
        try:
            file_path = DataLoader.get_path('MATIERE/ANGLAIS/anglais_voc1.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                return data.get("anglais_voc1", {})
        except FileNotFoundError:
            print("Error: English data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in English data file.")
            return {}

    @staticmethod
    def _load_french():
        """Load French vocabulary and verb data"""
        vocabulary = {}
        persons = []
        agreement = {}
        verb_data = {}

        try:
            file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                vocabulary = data.get("francais_voc", {})
        except FileNotFoundError:
            print("Error: French vocabulary file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in French vocabulary file.")

        try:
            file_path = DataLoader.get_path('MATIERE/FRANCAIS/francais_verb.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                verb_data = json.load(f)
                persons = verb_data.get("verbs", {}).get("personnes", [])
                agreement = verb_data.get("verbs", {}).get("accord", {})
        except FileNotFoundError:
            print("Error: French verb file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in French verb file.")

        return vocabulary, persons, agreement, verb_data

    @staticmethod
    def _load_german():
        """Load German vocabulary data"""
        try:
            file_path = DataLoader.get_path('MATIERE/DEUTSCH/deutsch.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                return data.get("merkmale_von_Kurzgeschichten", [])
        except FileNotFoundError:
            print("Error: German data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in German data file.")
            return []

    @staticmethod
    def _load_scnat():
        """Load natural sciences data"""
        elements = {}
        atomic_numbers = {}
        try:
            file_path = DataLoader.get_path('MATIERE/SCNAT/scnat.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                data = json.load(f)
                elements = data.get("elements", {})
                atomic_numbers = data.get("ordnungszahl_von_elementen", {})
        except FileNotFoundError:
            print("Error: Natural Sciences data file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in Natural Sciences data file.")

        return elements, atomic_numbers

    @staticmethod
    def _load_math():
        """Load mathematics data"""
        try:
            # NOTE: Assuming 'math_base' is available in the expected file path
            from MATIERE.MATH.math import math_base
            return math_base
        except ImportError:
            print("Error: Math base function not found. Returning a dummy function.")
            def dummy_math_base():
                return "2 + 2 = ?", 4
            return dummy_math_base


    @staticmethod
    def _load_geography():
        """Load geography data"""
        try:
            file_path = DataLoader.get_path('MATIERE/GEO/geo.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: Geography data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in Geography data file.")
            return {}
        
    def _load_histo():
        try:
            file_path = DataLoader.get_path('MATIERE/HISTO/histo.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: History data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in History data file.")
            return {}
        
    def _load_color():
        try:
            file_path = DataLoader.get_path('DATA/police.json')
            with open(file_path, 'r', encoding=DataLoader.ENCODING) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: COLOR data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in COLOR data file.")
            return {}
