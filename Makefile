# On définit nos variables
CC = gcc
CFLAGS = -Wall -Wextra -O2

# ÉTAPE 1 : On utilise la fonction 'wildcard' pour lister tous les fichiers .c du dossier
SRC = $(wildcard /mnt/c/CODE/ONE/*.c)
SRC_EN = $(wildcard /mnt/c/CODE/ONE/matiere/langue/*.c)
SRC_M = $(wildcard /mnt/c/CODE/ONE/matiere/math/*.c)
SRC_core = $(wildcard /mnt/c/CODE/ONE/core/*.c)

# Etape 2: On defini la variable de fichier executable
EXEC = ../ONE-v1.4.2

# La règle principale : on veut créer le fichier '../ONE'
# Il dépend de tous nos fichiers sources (.c)
$(EXEC): $(SRC) $(SRC_EN) $(SRC_M) $(SRC_core)
	$(CC) $(CFLAGS) $(SRC) $(SRC_EN) $(SRC_M) $(SRC_core) -o $(EXEC) -lcjson

# La règle clean pour nettoyer le dossier parent
clean:
	rm -f $(EXEC)
