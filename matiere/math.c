#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void random_value(int *a, int *b, char *op)
{
	int op_temp;
	op_temp = rand()%4;
	if (op_temp == 3) {
		int pro_temp = rand()%2;
		int entier = 20-(rand()%40);
		if (!entier) {entier = 1;}
		int c = 20-(rand()%40);
		if (!pro_temp) {
			*b = entier;
			*a = entier * c;
			*op = '/';
		} else {
			*b = c;
			*a = *b * c;
			*op = '/';
		}
	} else if (op_temp == 2) {
		int pro_temp = rand()%2;
		if (!pro_temp) {
			*a = 20-(rand()%40);
			*b = 20-(rand()%40);
			*op = '*';
		} else {
			int entier = 20-(rand()%40);
			*a = entier;
			*b = entier;
			*op = '*';
		}
	} else if (op_temp) {
		*a = 100-(rand()%200);
		*b = 100-(rand()%200);
		*op = '-';
	} else if (!op_temp) {
		*a = 100-(rand()%200);
		*b = 100-(rand()%200);
		*op = '+';
	}
}

void agrandir_calcul(char calcul[100], int etapes)
{
    // On commence avec un nombre de départ (ex: 7)
    int nombre_depart = 7;
    snprintf(calcul, 100, "%d", nombre_depart);

    char temporaire[100];

    for (int i = 0; i < etapes; i++)
    {
        int op_choix = rand() % 3; // Choix de l'opération pour agrandir

        switch (op_choix)
        {
            case 0:
                // Étape d'addition : "7" devient "(7 + 110)"
                int val_add = rand() % 200;
                snprintf(temporaire, 100, "(%s + %d)", calcul, val_add);
                break;

            case 1:
                // Étape de multiplication : "7" devient "(111 * 7)"
                int val_mult = rand() % 12 + 2;
                snprintf(temporaire, 100, "(%d * %s)", val_mult, calcul);
                break;

            case 2:
                // Étape plus complexe (ex: ajouter une puissance ou fonction)
                // "(expression)" devient "2 * ((expression) + 5)"
                snprintf(temporaire, 100, "2 * (%s + 5)", calcul);
                break;
        }

        // On recopie le résultat agrandi dans notre variable principale
        strncpy(calcul, temporaire, 100);
    }
}

int opperation_basic(int a, int b, char op)
{
	if (op == '+') {
		return a + b;
	} else if (op == '-') {
		return a - b;
	} else if (op == '*') {
		return a * b;
	} else if (op == '/') {
		return a / b;
	} else {
		return 0;
	}
}

int input(char answer[50])
{
    int result = 0;
    int state = 1;

    while (state)
    {
        // 1. Lecture de la ligne complète
        if (scanf("%49s", answer) != 1) return 0;

        int total = 0;
        int valeur_courante = 0;
        char op = '+'; // Par défaut, le premier nombre est ajouté à 0
        
        char *ptr = answer;
        int bytes_read = 0;

        // On va lire la chaîne morceau par morceau : un opérateur puis un nombre
        // Exemple : "-3+6" -> d'abord (pas d'opérateur, signe négatif), puis "+6"
        
        // Si le premier caractère est un nombre ou un signe, on le lit
        if (sscanf(ptr, "%d%n", &valeur_courante, &bytes_read) == 1) {
            total = valeur_courante;
            ptr += bytes_read; // On avance dans la chaîne
        }

        // On parcourt le reste de la chaîne
        while (sscanf(ptr, " %c %d%n", &op, &valeur_courante, &bytes_read) == 2) {
            if (op == '+') {
                total += valeur_courante;
            } else if (op == '-') {
                total -= valeur_courante;
            } else if (op == '*') {
                total *= valeur_courante;
            } else if (op == '/') {
                if (valeur_courante != 0) {
                    total /= valeur_courante;
                }
            }
            ptr += bytes_read; // On avance après le bloc lu
        }

        result = total;
        state = 0; // On a fini d'analyser toute la chaîne saisie

        // On vérifie si l'utilisateur a entré une chaîne vide ou s'il reste des caractères non lus
        // Si ptr n'est pas à la fin de la chaîne '\0', c'est qu'il y a un problème de syntaxe
        if (*ptr != '\0') {
            printf("[Erreur] Expression mal lue. Recommencez :\n>> ");
            state = 1;
        } else if (strchr(answer + 1, '+') != NULL || strchr(answer + 1, '-') != NULL || strchr(answer + 1, '*') != NULL || strchr(answer + 1, '/') != NULL) {
        	state = 1;
        }
    }

    return result;
}

int question_math(int a, int b, char op, int result)
{
	int temp_int = rand()%1;
	if (a == b && op == '*') {
		if (temp_int) {printf("%d² = ", a);}
		else if (!temp_int) {printf("%d %c %d = ", a, op, b);}
	} else if (result == b && op == '/') {
		if (temp_int) {printf("√%d = ", a);}
		else if (!temp_int) {printf("%d %c %d = ", a, op, b);}
	} else {
		printf("%d %c %d = ", a, op, b);
	}
	char answer_char[50];
	int answer = input(answer_char);
	if (answer == result) {
		printf("\033[1;32mBonne reponse\033[0m\n\n");
		return 1;
	} else {
		printf("\033[1;31mMauvaise reponse:\033[0m %d\n\n", result);
		return -1;
	}
}
