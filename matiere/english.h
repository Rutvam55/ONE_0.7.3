#include <cjson/cJSON.h>
#include "../../core/struct.h"
#ifndef QUIZ_H
#define QUIZ_H

int question_english(cJSON *json);
int question_voc(cJSON *json, struct Matiere *bouton);

#endif
