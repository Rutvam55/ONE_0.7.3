#include <cjson/cJSON.h>
#ifndef STRUCT_H
#define STRUCT_H

struct Player
{
	char username[21];
    int xp;
    int level;
    int score_max;
    int score;
    int nombre_de_question;
};

struct Bouton
{
	char name[50];
	int state;
};

struct Mode
{
	struct Bouton normal;
	struct Bouton infini;
};

struct Matiere
{
	struct Bouton langue;
	struct Bouton verb;
	struct Bouton voc;
	struct Bouton english;
	struct Bouton francais;
	struct Bouton deutsch;
	struct Bouton math;
	struct Bouton math_basic;
};

struct Json
{
	char data[50];
	cJSON *value;
};

struct File
{
	struct Json profil_json;
	struct Json DATA_enVerb;
	struct Json DATA_Voc;
};

#endif
