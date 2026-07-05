#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "./core/json.h"
#include "./core/funktion.h"
#include "./core/struct.h"
#include "./core/gestion_des_quiz.h"



int main(int argc, char *argv[])
{
	struct Mode mode;
	struct Matiere bouton;
	struct File file;
	struct Player player;
	char path_Profil_json[128];

	char chaine_7[7] = "Normal";
	for (int i = 0; chaine_7[i] != '\0'; i++){mode.normal.name[i] = chaine_7[i];}
	mode.normal.state = 1;

	strcpy(chaine_7, "infini");
	for (int i = 0; chaine_7[i] != '\0'; i++){mode.infini.name[i] = chaine_7[i];}
	mode.infini.state = !mode.normal.state;

	strcpy(chaine_7, "Langue");
	for (int i = 0; chaine_7[i] != '\0'; i++) {bouton.langue.name[i] = chaine_7[i];}
	bouton.langue.state = 0;

	char chaine_5[5] = "Verb";
	for (int i = 0; chaine_5[i] != '\0'; i++) {bouton.verb.name[i] = chaine_5[i];}
	bouton.verb.state = 1;

	char chaine_12[12] = "Vocabulaire";
	for (int i = 0; chaine_12[i] != '\0'; i++) {bouton.voc.name[i] = chaine_12[i];}
	bouton.voc.state = 1;

	char chaine_8[8] = "English";
	for (int i = 0; chaine_8[i] != '\0'; i++) {bouton.english.name[i] = chaine_8[i];}
	bouton.english.state = 1;

	char chaine_9[9] = "Francais";
	for (int i = 0; chaine_9[i] != '\0'; i++) {bouton.francais.name[i] = chaine_9[i];}
	bouton.francais.state = !bouton.english.state;

	strcpy(chaine_8, "Deutsch");
	for (int i = 0; chaine_8[i] != '\0'; i++) {bouton.deutsch.name[i] = chaine_8[i];}
	bouton.deutsch.state = !bouton.english.state;

	strcpy(chaine_5,"Math");
	for (int i = 0; chaine_5[i] != '\0'; i++) {bouton.math.name[i] = chaine_5[i];}
	bouton.math.state = 0;

	char chaine_20[21] = "Math basic (+ - * /)";
	for (int i = 0; chaine_20[i] != '\0'; i++) {bouton.math_basic.name[i] = chaine_20[i];}
	bouton.math_basic.state = 1;

	strcpy(chaine_12, "Profil.json"); 
	for (int i = 0; chaine_12[i] != '\0'; i++) {file.profil_json.data[i] = chaine_12[i];}
	file.profil_json.value = NULL;

	char chaine_14[14] = "DATA_Voc.json";
	for (int i = 0; chaine_14[i] != '\0'; i++) {file.DATA_Voc.data[i] = chaine_14[i];}
	file.DATA_Voc.value = NULL;

	char chaine_17[17] = "DATA_enVerb.json";
	for (int i = 0; chaine_17[i] != '\0'; i++) {file.DATA_enVerb.data[i] = chaine_17[i];}
	file.DATA_enVerb.value = NULL;

	argv_and_argc_search(argc, argv, &bouton, &mode);
	
	printf("Recherche du fichier %s", file.profil_json.data);
	recherch(path_Profil_json, sizeof(path_Profil_json), 'P');
	clear();
	
    srand(time(NULL));
    int temp_int;

    temp_int = ouverture_du_json(path_Profil_json, &file.profil_json.value);
    if (temp_int != 0) {
        cJSON_Delete(file.DATA_enVerb.value);
        cJSON_Delete(file.DATA_Voc.value);
        exit(1);
    }
    printf("Quel est ton nom d'utilisateur [20max]?\n>> ");
    scanf(" %20s", player.username);

    // --- CHARGEMENT DU COMPTE UTILISATEUR ---	

    // Vider le tampon mémoire après scanf pour éviter des conflits avec les prochains menus
    int clean_char;
    while ((clean_char = getchar()) != '\n' && clean_char != EOF);

    // Utilisation de GetObjectItem pour chercher par clé de chaîne
    cJSON *user = cJSON_GetObjectItemCaseSensitive(file.profil_json.value, player.username);



    if (cJSON_IsObject(user)){
        cJSON *cjson_xp = cJSON_GetObjectItemCaseSensitive(user, "xp");
        cJSON *cjson_level = cJSON_GetObjectItemCaseSensitive(user, "level");
        cJSON *cjson_score_max = cJSON_GetObjectItemCaseSensitive(user, "score_max");

        player.xp = 0;
        player.level = 1;
        player.score = 0;
        player.score_max = 0;

        if(cjson_xp) player.xp = cjson_xp->valuedouble;
        if(cjson_level) player.level = cjson_level->valuedouble;
        if(cjson_score_max) player.score_max = cjson_score_max->valuedouble;
        
        printf("Profil chargé!\n| Niveau: %d | XP actuel: %d | Record: %d |\n\n", player.level, player.xp, player.score_max);
    } else {
        // L'utilisateur n'existe pas, on l'ajoute à la structure JSON globale
        printf("Création d'un nouveau profil pour \"%s\"...\n\n", player.username);
        user = cJSON_CreateObject();
        cJSON_AddNumberToObject(user, "level", 1);
        cJSON_AddNumberToObject(user, "xp", 0);
        cJSON_AddNumberToObject(user, "score_max", 0);
        cJSON_AddItemToObject(file.profil_json.value, player.username, user);
    }
    player.nombre_de_question = 0;
    //Choix de la matiere
	table_des_matiere(&bouton, &mode);

	/*========================*/
	/* CHARGEMENT DES FICHIER */
	/*========================*/
	char path_DATA_json[128];

    printf("Recherche du fichier Data_enVerb.json");
    recherch(path_DATA_json, sizeof(path_DATA_json), 'D');
    temp_int = ouverture_du_json(path_DATA_json, &file.DATA_enVerb.value);
    if (temp_int != 0) exit(1);

	printf("Recherche du fichier Data_Voc.json");
	recherch(path_DATA_json, sizeof(path_DATA_json), 'V');
	temp_int = ouverture_du_json(path_DATA_json, &file.DATA_Voc.value);
	if (temp_int != 0) exit(1);
    
    clear();
	
	/*=============*/
	/* PARTIE QUIZ */
	/*=============*/
    clear();
    if(!mode.infini.state && mode.normal.state){
		quiz_normal(&file, &bouton, &player);
    } else if(mode.infini.state && !mode.normal.state){
		quiz_infini(&file, &bouton, &player);
    }

	/*========================================*/
	/* PRESENTATION DE LA FIN AVEC SAUVEGARDE */
	/*========================================*/
	char mode_choix;
	if (mode.infini.state) {mode_choix = 'i';}
	else {mode_choix = 'n';};
	gamification(&player, mode_choix);
    
    // --- MISE À JOUR DANS LA STRUCTURE JSON ET SAUVEGARDE ---
    cJSON_SetNumberValue(cJSON_GetObjectItemCaseSensitive(user, "xp"), player.xp);
    cJSON_SetNumberValue(cJSON_GetObjectItemCaseSensitive(user, "level"), player.level);
    cJSON_SetNumberValue(cJSON_GetObjectItemCaseSensitive(user, "score_max"), player.score_max);

    sauvegarder_du_json(path_Profil_json, file.profil_json.value);
    printf("Données de jeu synchronisées avec succès.\n");

    // Nettoyage complet de la mémoire
    cJSON_Delete(file.DATA_enVerb.value);
    cJSON_Delete(file.DATA_Voc.value);
    cJSON_Delete(file.profil_json.value);
    return 0;
}
