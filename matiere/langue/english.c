#include <stdio.h>
#include <stdlib.h>
#include <cjson/cJSON.h>
#include <string.h>
#include <time.h>
#include "english.h"

int question_english(cJSON *json)
{
	srand(time(NULL));
	int size = cJSON_GetArraySize(json);
	if ( size != 0 ) {
		int random_int = rand() % size;
		cJSON *random_verb = cJSON_GetArrayItem(json, random_int);

		size = cJSON_GetArraySize(random_verb);
		if ( size != 0 ) {
			random_int = rand() % size;
			cJSON *random_temp = cJSON_GetArrayItem(random_verb, random_int);

			size = cJSON_GetArraySize(random_temp);
			if ( size != 0 ) {
				random_int = rand() % size;
				cJSON *random_person = cJSON_GetArrayItem(random_temp, random_int);

				char *correct = random_person -> valuestring;
				char answer[50];
				
				printf("Conjuge \"%s\" au %s\n>> %s ", random_verb -> string, random_temp -> string, random_person -> string);
				scanf(" %[^\n]", answer);

				// 1=correct  0=aide -1=faut
				if (!strcmp(answer, correct)) {
					printf("\033[1;32mreponse correct\033[0m\n\n");
					return 1;
				} else if (!strcmp(answer, "?")) {
					printf("reponse correct: %s\n\n", correct);
					return 0;
				} else if (!strcmp(answer, "Q")) {
					return 2;
				} else if (strcmp(answer, correct)) {
					printf("\033[1;31mreponse correct: %s\033[0m\n\n", correct);
					return -1;
				}

			} else {
				printf("Le verb ne contient aucun temp.\nVeuillez supprimer le fichier ./data/DATA.json puis utiliser le fichier ./MATIERE/ENGLISH/dataC.py pour remplir et recrée le fichier ./MATIERE/ENGLISH/DATA.json facilment.");
				exit(0);
			}
			
		} else {
			printf("Le verb choisi au hasard ne contient aucun temp.\nVeuillez supprimer le fichier ./MATIERE/ENGLISH/DATA.json puis utiliser le fichier ./MATIERE/ENGLISH/dataC.py pour remplir et recrée le fichier ./MATIERE/ENGLISH/DATA.json facilment.");
			exit(0);
		}

	} else {
		printf("Le tableax est vide.\nUtiliser le fichier ./MATIERE/ENGLISH/dataC.py pour remplir le fichier ./MATIERE/ENGLISH/DATA.json facilment.");
		exit(0);
	}
	return 0;
}

int question_voc(cJSON *json, struct Matiere *bouton)
{
	srand(time(NULL));
	int size = cJSON_GetArraySize(json);
	if ( size != 0 ) {
		int random_int = rand() % size;
		cJSON *random_voc = cJSON_GetArrayItem(json, random_int);
		char choix[3][2] = {{'X', 'X'}, {'X', 'X'}, {'X', 'X'}};
		if (bouton -> english.state) {
			choix[0][0] = 'E';
			choix[0][1] = 'N';
		} else if (bouton -> deutsch.state) {
			choix[1][0] = 'D';
			choix[1][1] = 'E';
		} else if (bouton -> francais.state) {
			choix[2][0] = 'F';
			choix[2][1] = 'R';
		}
		int temp_int = rand()%3;
		char final[2] = {choix[temp_int][0], choix[temp_int][1]};
		while (choix[temp_int][0] != 'X' || choix[temp_int][0] != 'X')
		{
			temp_int = rand()%3;
			final[0] = choix[temp_int][0];
			final[1] = choix[temp_int][1];
		}
		char *p = final;
		cJSON *random_lang = cJSON_GetArrayItem(random_voc, *p);
		char *correct = random_lang -> valuestring;
		char answer[50];
				
		printf("Traduit \"%s\" en %s\n>> ", random_voc -> string, random_lang -> string);
		scanf(" %[^\n]", answer);

		// 1=correct  0=aide -1=faut
		if (!strcmp(answer, correct)) {
			printf("\033[1;32mreponse correct\033[0m\n\n");
			return 1;
		} else if (!strcmp(answer, "?")) {
			printf("reponse correct: %s\n\n", correct);
			return 0;
		} else if (!strcmp(answer, "Q")) {
			return 2;
		} else if (strcmp(answer, correct)) {
			printf("\033[1;31mreponse correct: %s\033[0m\n\n", correct);
			return -1;
		}

	} else {
		printf("Le tableax est vide.\nUtiliser le fichier ./MATIERE/ENGLISH/dataVocC.py pour remplir le fichier ./MATIERE/ENGLISH/DATA.json facilment.");
		exit(0);
	}
	return 0;
}
