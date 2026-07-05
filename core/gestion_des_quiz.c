#include <cjson/cJSON.h>
#include <stdio.h>
#include <stdlib.h>
#include "./gestion_des_quiz.h"
#include "./funktion.h"
#include "../matiere/langue/english.h"
#include "../matiere/math/math.h"

void table_des_matiere(struct Matiere *bouton, struct Mode *mode)
{
	char off[22] = "\033[1;31mOFF\033[0m";
	char on[21] = "\033[1;32mON\033[0m";
	char state[2][22] = {"\033[1;31mOFF\033[0m", "\033[1;32mON\033[0m"};
	char answer_char;

	int condition = 0;
	while (!condition)
	{
		clear();
		switch (bouton -> langue.state)
		{
			case 0:
				printf("[1] %s: %s\n", bouton -> langue.name, off);
				break;
			case 1:
				printf("[1] %s: %s\n", bouton -> langue.name, on);
				printf("\t[a] %s: %s\n", bouton -> english.name, state[ bouton -> english.state ]);
				printf("\t[b] %s: %s\n", bouton -> francais.name, state[ bouton -> francais.state ]);
				printf("\t[c] %s: %s\n", bouton -> deutsch.name, state[ bouton -> deutsch.state ]);
				printf("\t[d] %s: %s\n", bouton -> verb.name, state[ bouton -> verb.state ]);
				printf("\t[e] %s: %s\n", bouton -> voc.name, state[ bouton -> voc.state ]);
				break;
		}

		switch (bouton -> math.state)
		{
			case 0:
				printf("[2] %s: %s\n", bouton -> math.name, off);
				break;
			case 1:
				printf("[2] %s: %s\n", bouton -> math.name, on);
				printf("\t[a] %s: %s\n", bouton -> math_basic.name, state[ bouton -> math_basic.state ]);
				break;
		}
			
		printf("[n] %s: %s\n", mode -> normal.name, state[ mode -> normal.state ]);
		printf("[i] %s: %s\n", mode -> infini.name, state[ mode -> infini.state ]);
		printf("Entrer un de ses caractere (s = suivant; q = quitter):\n>>");
		scanf(" %c", &answer_char);
		char answer_char_2;
		switch (answer_char)
		{
			case 'q':
				exit(0);
			case 'a':
				printf("Entrer le chiffre entre les crochet \"[]\" de la veleur parent:\n>>");
				scanf(" %c", &answer_char_2);
				switch (answer_char_2)
				{
					case '1':
						bouton -> english.state = !bouton -> english.state;
						break;
					case '2':
						bouton -> math_basic.state = !bouton -> math_basic.state;
						break;
				};
				break;
			case 'b':
				printf("Entrer le chiffre entre les crochet \"[]\" de la veleur parent:\n>>");
				scanf(" %c", &answer_char_2);
				switch (answer_char_2)
				{
					case '1':
						bouton -> francais.state = !bouton -> francais.state;
						break;
					case '2':
						break;
				};
				break;
			case 'c':
				printf("Entrer le chiffre entre les crochet \"[]\" de la veleur parent:\n>>");
				scanf(" %c", &answer_char_2);
				switch (answer_char_2)
				{
					case '1':
						bouton -> deutsch.state = !bouton -> deutsch.state;
						break;
					case '2':
						break;
				};
				break;
			case 'd':
				printf("Entrer le chiffre entre les crochet \"[]\" de la veleur parent:\n>>");
				scanf(" %c", &answer_char_2);
				switch (answer_char_2)
				{
					case '1':
						bouton -> verb.state = !bouton -> verb.state;
						break;
					case '2':
						break;
				};
				break;
			case 'e':
				printf("Entrer le chiffre entre les crochet \"[]\" de la veleur parent:\n>>");
				scanf(" %c", &answer_char_2);
				switch (answer_char_2)
				{
					case '1':
						bouton -> voc.state = !bouton -> voc.state;
						break;
					case '2':
						break;
				};
				break;
			case 's':
				if ((bouton -> langue.state && (bouton -> verb.state || bouton -> voc.state) && (bouton -> english.state || bouton -> francais.state || bouton -> deutsch.state)) || (bouton -> math.state && bouton -> math_basic.state)) {
					condition = 1;
				} else {
					printf("Erreur: choisier une matière");
				};
				break;
			case 'i':
			case 'n':
				mode -> infini.state = !mode -> infini.state;
				mode -> normal.state = !mode -> normal.state;
				break;
			case '1':
				bouton -> langue.state = !bouton -> langue.state;
				break;
			case '2':
				bouton -> math.state = !(bouton -> math.state);
				break;
		}
		if (!bouton -> english.state && !bouton -> francais.state && !bouton -> deutsch.state)
		{
			bouton -> english.state = 1;
		}
	}
}

void gamification(struct Player *player, char mode)
{
    float pourcentage = 0;
    if (player -> nombre_de_question > 0) {
	    pourcentage = ((float)(player -> score)/player -> nombre_de_question)*100;
    	printf("\nWow ... Tu as un score de %d en %d question(s)!\nC'est un taux de reussite de %3f%%\n", player -> score, player -> nombre_de_question, pourcentage);
    } else {
    	printf("\nAi ... La prochaine fois cela ira mieux.\nTu peut egalment esseiler le mode normal. même si il y a une mauvaise reponce le quiz continue.\n");
    }
    // --- LOGIQUE DE PROGRESSION & LEVEL UP ---
    int xp_gagne = 0;
    if (mode == 'n') {
	    if(pourcentage >= 75){
        	int bonus = (player -> score) + (player -> level) + 100;
        	xp_gagne = ((player -> score) * player -> nombre_de_question) + bonus;
    	} else if (75 > pourcentage && pourcentage > 50) {
    		int bonus = (player -> score) + (player -> level);
    		xp_gagne = ((player -> score) * player -> nombre_de_question) + bonus;
    	} else if (pourcentage == 50) {
    		xp_gagne = (player -> score) * player -> nombre_de_question;
    	} else {
    	    xp_gagne = (player -> score);
    	}
    } else if (mode == 'i') {
    	(player -> score)++;
		xp_gagne = (player -> score) * player -> nombre_de_question;
		if (player -> score >= 10)
		{
	    	int bonus = (player -> score) + (player -> level);
			xp_gagne += bonus;
		}
	}
    
    (player -> xp) += xp_gagne;
    printf("Vous avez gagné %d XP ! (Total: %d XP)\n", xp_gagne, player -> xp);

    // Boucle tant qu'on a assez d'XP pour monter de niveau
    while (player -> xp >= (player -> level) * 1500) {
        (player -> xp) = (player -> xp) - ((player -> level) * 1500); // Déduction de l'XP consommée pour le passage
        (player -> level)++;
        printf("\033[1;33mUP ! Tu passes au Niveau %d !\033[0m\n", player -> level);
    }

    if(player -> score > player -> score_max){
        player -> score_max = player -> score;
        printf("\033[1;36mNouveau score maximal: %d !\033[0m\n", player -> score_max);
    }
}

void quiz_normal(struct File *file, struct Matiere *bouton, struct Player *player) {
	printf("score: %d\n", player -> score);
    int nombre = 0;
    printf("Combien de question?\n>>");
    while(scanf("%d", &nombre) != 1 || nombre < 1)
    {
        printf("Erreur: entrer un nombre!\n");
        int clean;
        while ((clean = getchar()) != '\n' && clean != EOF);

    	nombre = 0;
    	printf("Combien de question?\n>>");
    }
    player -> nombre_de_question = nombre;
            
    int c;
    while ((c = getchar()) != '\n' && c != EOF); // Nettoyage indispensable

    for(int i = 0; i < nombre; i++)
    {
		int value = -2;
		if ((bouton -> langue.state && (bouton -> verb.state || bouton -> voc.state) && (bouton -> english.state || bouton -> francais.state || bouton -> deutsch.state)) || (bouton -> math.state && bouton -> math_basic.state)) {
			int temp_int = rand()%3;
			if (!temp_int && bouton -> langue.state && bouton -> verb.state) {
				value = question_english(file -> DATA_enVerb.value);
			} else if (temp_int && bouton -> langue.state && bouton -> voc.state) {
				value = question_voc(file -> DATA_Voc.value, bouton);
			} else if (temp_int==2 && bouton -> math.state && bouton -> math_basic.state) {
				int a;
				int b;
				char op;
				int result;
				random_value(&a, &b, &op);
				result = opperation_basic(a, b, op);
				value = question_math(a, b, op, result);
			} else {
				i--;
				value = 0;
			}
		} else {
			printf("ERROR: aucune matiere choisi.");
			exit(0);
		}
	    switch(value)
    	{
    	    case 2:
				cJSON_Delete(file -> DATA_enVerb.value);
				cJSON_Delete(file -> DATA_Voc.value);
				cJSON_Delete(file -> profil_json.value);
				exit(0);
            case 1: 
   	            (player -> score)++;
   	            break;
       	    case 0: 
           	    break;
            case -1:
   	            (player -> score)--;
       	        break;
       	    case -2:
				cJSON_Delete(file -> DATA_enVerb.value);
				cJSON_Delete(file -> DATA_Voc.value);
				cJSON_Delete(file -> profil_json.value);
       	        exit(0);
           	default:
               	break;
        }
    }
}

void quiz_infini(struct File *file, struct Matiere *bouton, struct Player *player)
{
	printf("score: %d\n", player -> score);
    int continu = 1;
    int value = -2;
    while(continu)
    {
		if ((bouton -> langue.state && (bouton -> verb.state || bouton -> voc.state) && (bouton -> english.state || bouton -> francais.state || bouton -> deutsch.state)) || (bouton -> math.state && bouton -> math_basic.state)) {
			int temp_int = rand()%3;
			if (!temp_int && bouton -> english.state && bouton -> verb.state) {
				value = question_english(file -> DATA_enVerb.value);
			} else if (temp_int && bouton -> langue.state && bouton -> voc.state) {
				value = question_voc(file -> DATA_Voc.value, bouton);
			} else if (temp_int==2 && bouton -> math.state && bouton -> math_basic.state) {
				int a;
				int b;
				char op;
				int result;
				random_value(&a, &b, &op);
				result = opperation_basic(a, b, op);
				value = question_math(a, b, op, result);
			} else {
				value = 0;
				player -> nombre_de_question--;
			}
		} else {
			printf("ERROR: aucune matiere choisi.");
			exit(0);
		}
        player -> nombre_de_question++;
	    switch(value)
    	{
        	case 2:
				cJSON_Delete(file -> DATA_Voc.value);
				cJSON_Delete(file -> DATA_enVerb.value);
				cJSON_Delete(file -> profil_json.value);
				exit(0);
            case 1: 
   	            player -> score++;
                break;
       	    case 0: 
           	    break;
            case -1:
   	            continu= 0;
       	        break;
       	    case -2:
				cJSON_Delete(file -> DATA_Voc.value);
				cJSON_Delete(file -> DATA_enVerb.value);
				cJSON_Delete(file -> profil_json.value);
       	        exit(0);
           	default:
        		break;
        }
	}
}

