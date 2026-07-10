#include <stdio.h>
#include <stdlib.h>
#include <cjson/cJSON.h>
#include <time.h>
#include <string.h>
#include "json.h"
#if defined(__linux__) || defined(_LINUX) || defined(__linux)
    void recherch(char *path_out, size_t max_len, char file)
    {
        char *home = getenv("HOME");
        if (file == 'D') {
            if (home != NULL) {
                snprintf(path_out, max_len, "%s/CODE/ONE/data/DATA_en.json", home);
            } else {
                strncpy(path_out, "DATA.json", max_len);
            }
        } else if (file == 'P') {
            if (home != NULL) {
                snprintf(path_out, max_len, "%s/CODE/ONE/data/Profil.json", home);
            } else {
                strncpy(path_out, "Profil.json", max_len);
            }
        }
    }
#elif defined(_WIN32) || defined(WIN32)
    void recherch(char *path_out, size_t max_len, char file)
    {
        char home[] = "C:\\user\\rutvam55";
        if (file == 'D') {
            snprintf(path_out, max_len, "%s\\CODE\\ONE\\data\\DATA_en.json", home);
        } else if (file == 'P') {
            snprintf(path_out, max_len, "%s\\CODE\\ONE\\data\\Profil.json", home);
        }
    }
#else
    void recherch(char *path_out, size_t max_len, char file)
    {
        if (file == 'D') {
            snprintf(path_out, max_len, "../data/DATA_en.json");
        } else if (file == 'P') {
Ob            snprintf(path_out, max_len, "../data/Profil.json");
        }
    }
#endif
int ouverture_du_json(char path[128], cJSON **json)
{
	FILE *fichier = fopen(path, "r");
    if (fichier == NULL)
    {
        printf("Erreur: Impossible d'ouvrir le fichier.\n");
    	printf("chemin: \"%s\"\n", path);
        printf("Creation du fichier manquant ...\n");
        fichier = fopen(path, "w");
    }

    fseek(fichier, 0, SEEK_END);
    long taille = ftell(fichier);
    fseek(fichier, 0, SEEK_SET);
    
    char *tampon = malloc(taille + 1);
    if (tampon == NULL) {
        fclose(fichier);
        return 1;
    }
    
    fread(tampon, 1, taille, fichier);
    tampon[taille] = '\0';
    fclose(fichier);

    *json = cJSON_Parse(tampon);
    free(tampon);

    if (*json == NULL)
    {
        printf("Erreur lors du parsing du JSON.\n");
        printf("chemin: \"%s\"\n", path);
        const char *erreur = cJSON_GetErrorPtr();
        if (erreur != NULL)
        {
        	printf("Erreur près de: %s\n", erreur);
        }
        return 1;
    }
    return 0;
}

int sauvegarder_du_json(char path[128], cJSON *json)
{
    FILE *fichier = fopen(path, "w");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture pour sauvegarde: %s\n", path);
        return 1;
    }

    char *rendu = cJSON_Print(json);
    if (rendu == NULL) {
        fclose(fichier);
        return 1;
    }

    fprintf(fichier, "%s", rendu);
    free(rendu);
    fclose(fichier);
    return 0;
}
