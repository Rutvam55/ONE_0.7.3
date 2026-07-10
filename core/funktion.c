#include <stdio.h>
#include <string.h>
#include "struct.h"

void clear()
{
    printf("\033[H\033[2J");
    fflush(stdout);
}

void argv_and_argc_search(int argc, char *argv[], struct Matiere *bouton, struct Mode *mode)
{
    char on[20] = "\033[1;32mON\033[0m";
    char off[21] = "\033[1;31mOFF\033[0m";
    if (argc == 1) {
        printf("Basic Mode: %s\n", on);
        printf("Personal Mode: %s\n", off);
    } else {
        printf("Basic Mode: %s\n", off);
        printf("Personal Mode: %s\n", on);
        for(int i = 1; i < argc; i++)
        {
			int j = i + 1;
            if (!strcmp(argv[i], bouton->langue.name)) {
                bouton->langue.state = 1;
                printf("%s: %s\n", bouton->langue.name, on);
                if (j < argc && !strcmp(argv[j], bouton->verb.name)) {
                	bouton->verb.state = 1;
                	printf("\t%s: %s\n", bouton->verb.name, on);
                	i++;
                } else if (j < argc && !strcmp(argv[j], bouton->voc.name)) {
                    bouton->voc.state = 1;
                   	printf("\t%s: %s\n", bouton->voc.name, on);
       	            i++;
                } else if (j < argc && !strcmp(argv[j], bouton->english.name)) {
                    bouton->english.state = 1;
                   	printf("\t%s: %s\n", bouton->english.name, on);
       	            i++;
                } else if (j < argc && !strcmp(argv[j], bouton->francais.name)) {
                    bouton->francais.state = 1;
                   	printf("\t%s: %s\n", bouton->francais.name, on);
       	            i++;
                } else if (j < argc && !strcmp(argv[j], bouton->deutsch.name)) {
                    bouton->deutsch.state = 1;
                   	printf("\t%s: %s\n", bouton->deutsch.name, on);
       	            i++;
                }
            } else if (!strcmp(argv[i], bouton->math.name)) {
                bouton->math.state = 1;
                printf("%s: %s\n", bouton->math.name, on);
                if (j < argc && !strcmp(argv[j], bouton->math_basic.name)) {
                    bouton->math_basic.state = 1;
                	printf("\t%s: %s\n", bouton->math.name, on);
                }
            } else if (!strcmp(argv[i], "infini")) {
                mode->infini.state = 1;
                mode->normal.state = 0;
                printf("Mode Infini: %s\n", on);
                printf("Mode Normal: %s\n", off);
            } else if (!strcmp(argv[i], "normal")) {
                mode->infini.state = 0;
                mode->normal.state = 1;
                printf("Mode Normal: %s\n", on);
                printf("Mode Infini: %s\n", off);
            } else {
                printf("Warning: The argument \"%s\" is not recognized.\n", argv[i]);
            }
        }
    }
}
