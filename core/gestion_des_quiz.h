#include <cjson/cJSON.h>
#include "struct.h"
#ifndef GESTION_DES_QUIZ_H
#define GESTION_DES_QUIZ_H

void table_des_matiere(struct Matiere *bouton, struct Mode *mode);
void gamification(struct Player *player, char mode);
void quiz_normal(struct File *file, struct Matiere *bouton, struct Player *player);
void quiz_infini(struct File *file, struct Matiere *bouton, struct Player *player);

#endif
