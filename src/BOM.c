#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define ASIZE 256
#define WORD_SIZE 32
#define EOS '\0'
#define FALSE 0
#define TRUE 1
#define UNDEFINED -1

struct _cell{
   int element; 
  struct _cell *next;
};
 
typedef struct _cell *List;

void error(char *name){
    fprintf(stderr,"ERROR: The program failed at %s.",name);
    exit(-1);
}

long readfile(char *filename, char *text[])
{
	FILE *fin;
	long len;
	int i = 0;
	char c;
	
	if (!(fin = fopen(filename, "r"))) {
		fprintf (stderr, "I can't open the file: %s\n", filename);
		exit(1);
	}
	// llegim el nombre de caracters que hi ha al fitxer
	fseek(fin, 0, SEEK_END);
	len = ftell(fin);
	fseek(fin, 0, SEEK_SET);
	// demanem memoria per la variable text
	*text = malloc(len + 1);
        // bucle per llegir el fitxer
	while ((c = (fgetc(fin))) != EOF) {
	  if ((c=='a')||(c=='c')||(c=='g')||(c=='t')||(c=='A')||(c=='C')||(c=='G')||(c=='T')){
	    (*text)[i] = c;
	    //printf("text[%d] = %c\n", i, (*text)[i]);
	    i++;
	  }
	}
	fclose(fin);
	return i;
}

int getTransition(char *x, int p, List L[], char c) {
   List cell;

   if (p > 0 && x[p - 1] == c)
      return(p - 1);
   else {
      cell = L[p];
      while (cell != NULL)
         if (x[cell->element] == c)
            return(cell->element);
         else
            cell = cell->next;
      return(UNDEFINED);
   }
}


void setTransition(int p, int q, List L[]) {
   List cell;

   cell = (List)malloc(sizeof(struct _cell));
   if (cell == NULL)
      error("BOM/setTransition");
   cell->element = q;
   cell->next = L[p];
   L[p] = cell;
}


void oracle(char *x, int m, char T[], List L[]) {
   int i, p, q;
   int S[m + 1];
   char c;

   S[m] = m + 1;
   for (i = m; i > 0; --i) {
      c = x[i - 1];
      p = S[i];
      while (p <= m &&
             (q = getTransition(x, p, L, c)) ==
             UNDEFINED) {
         setTransition(p, i - 1, L);
         p = S[p];
      }
      S[i - 1] = (p == m + 1 ? m : q);
   }
   p = 0;
   while (p <= m) {
      T[p] = TRUE;
      p = S[p];
   }
}


void BOM(char *x, int m, char *y, int n) {
  char T[m + 1];
  List L[m + 1];
  int i, j, p, period, q, shift;
  long int found = 0;

  /* Preprocessing */
  memset(L, NULL, (m + 1)*sizeof(List));
  memset(T, FALSE, (m + 1)*sizeof(char));
  oracle(x, m, T, L);

  /* Searching */
  j = 0;
  while (j <= n - m) {
    i = m - 1;
    p = m;
    shift = m;
    while (i + j >= 0 &&
            (q = getTransition(x, p, L, y[i + j])) !=
            UNDEFINED) {
        p = q;
        if (T[p] == TRUE) {
          period = shift;
          shift = i;
        }
        --i;
    }
    if (i < 0) {
        found++;
        shift = period;
    }
    j += shift;
  }
  printf("Found: %ld\n",found);
}

  int main(int argc, char *argv[])
{
  char pattern[256];
	char filename[256];
	char *text;
	int  n;
	clock_t initemps;

	sprintf(pattern,"%s",argv[2]);
	sprintf(filename,"%s",argv[1]);
	printf("pattern: %s \n",pattern);
	
	n = readfile(filename, &text);
	// printf("text: %s \n",text);
	// printf("n=%d\n",n);
	initemps=clock();
	BOM(pattern,strlen(pattern),text,n);
	printf( "Time: %f s\n", (clock()-initemps)/(double)CLOCKS_PER_SEC );
	free(text);
  return 0;
}

