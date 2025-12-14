from CORE.dataloader import DataLoader


class Couleur:
    """Gestion des couleurs et styles de texte via codes ANSI.

    Cette classe récupère les paramètres de couleur via `DataLoader`.
    """

    def __init__(self):
        # Charger la configuration de couleur (peut retourner {} si manquant)
        self.COLOR = DataLoader.load_data("COLOR") or {}

    def text_editor(self, text, police = "", text_color = "", background_color = ""):
        """Encapsule le texte avec les codes ANSI pour la couleur et le style."""
        # Fallback en cas d'échec de chargement
        if not self.COLOR:
            self.COLOR = {
                "CODE": "\033[",
                "RESET": "0",
                "END CODE": "m",
                "police": {"FAT": "1", "DIM": "2", "NONE": "0"},
                "COLOR TEXT": {"GREEN": "32", "RED": "31", "DEFAULT": "39", "RESET": "0"},
                "BACKGROUND COLOR": {"DEFAULT": "49"}
            }

        # Récupérer les codes (sûrement présents dans self.COLOR)
        style_code = self.COLOR.get("police", {}).get(police, "")
        text_code = self.COLOR.get("COLOR TEXT", {}).get(text_color, "")
        background_code = self.COLOR.get("BACKGROUND COLOR", {}).get(background_color, "")

        code = self.COLOR.get("CODE", "\033[")
        reset = self.COLOR.get("RESET", "0")
        end = self.COLOR.get("END CODE", "m")

        ansi = code
        parts = [part for part in [style_code, text_code, background_code] if part]

        if parts:
            ansi += ";".join(parts) + end
        else:
            ansi = code + self.COLOR.get("COLOR TEXT", {}).get("RESET", "0") + end

        return f"{ansi}{text}{code}{reset}{end}"
from CORE.dataloader import DataLoader


class Couleur:
    """Gestion des couleurs et styles de texte via codes ANSI.

    Cette classe récupère les paramètres de couleur via `DataLoader`.
    Pour éviter les import circulaires, on importe directement `DataLoader`.
    """

    def __init__(self):
        # Charger la configuration de couleur (peut retourner {} si manquant)
        self.COLOR = DataLoader.load_data("COLOR") or {}

    def text_editor(self, text, police = "", text_color = "", background_color = ""):
        """Encapsule le texte avec les codes ANSI pour la couleur et le style."""
        # Fallback en cas d'échec de chargement
        if not self.COLOR:
            print("⚠️ Avertissement : Échec du chargement des données de couleur. Utilisation des codes ANSI par défaut.")
            self.COLOR = {
                "CODE": "\033[",
                "RESET": "0",
                "END CODE": "m",
                "police": {"FAT": "1", "DIM": "2", "NONE": "0"},
                "COLOR TEXT": {"GREEN": "32", "RED": "31", "DEFAULT": "39", "RESET": "0"},
                "BACKGROUND COLOR": {"DEFAULT": "49"}
            }

        # Récupérer les codes (sûrement présents dans self.COLOR)
        style_code = self.COLOR.get("police", {}).get(police, "")
        text_code = self.COLOR.get("COLOR TEXT", {}).get(text_color, "")
        background_code = self.COLOR.get("BACKGROUND COLOR", {}).get(background_color, "")

        code = self.COLOR.get("CODE", "\033[")
        reset = self.COLOR.get("RESET", "0")
        end = self.COLOR.get("END CODE", "m")

        ansi = code
        parts = [part for part in [style_code, text_code, background_code] if part]

        if parts:
            ansi += ";".join(parts) + end
        else:
            ansi = code + self.COLOR.get("COLOR TEXT", {}).get("RESET", "0") + end

        return f"{ansi}{text}{code}{reset}{end}"