#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#define N 50

void MostraPlacar(char p1[N], char p2[N], int e, int tX, int tO);
void NovoJogo(char mat[3][3], int l, int c, int cont);
void MostraVelha(char mat[3][3], int l, int c, int cont);

int main(){
    setlocale(LC_ALL,"Portuguese");

    char mat[3][3],jog1[N], jog2[N], simb='X';
    int l, c, pos, cont=1, totX=0, totO=0, emp=0, i1, i2; 

    printf("Quem vai jogar com X?\n");
    gets(jog1);
    i1 = strlen(jog1);
    fflush(stdin);
    printf("Quem vai jogar com O?\n");
    gets(jog2);
    i2 = strlen(jog2);
    fflush(stdin);
    do
    {
        MostraPlacar(jog1[N], jog2[N], emp, totX, totO);
        NovoJogo(mat[3][3], l, c, cont);
        MostraVelha(mat[3][3],l, c, cont); 
           
    } while (totX + totO + emp < 7);
    

}

void MostraPlacar(char p1[N], char p2[N], int e, int tX, int tO){
    printf("-------------\n");
    printf("   PLACAR    \n");
    printf("%c.10, %d.2\n", p1, tX);
    printf("%c.10, %d.2\n", p2, tO);
    printf("Velha: %d.10\n", e);
    printf("-------------/n");
    return (p1, p2, e, tX, tO);
}

void NovoJogo(char mat[3][3], int l, int c, int cont){
    cont=1;
    for( l=0; l<3; l++){
        for( c=0; c<3; c++){
            mat [l][c] = NumpCarac(cont);
            cont++;
        }
    }
}

char NumpCarac(int num){
    return 0 + num;
}

void MostraVelha(char mat[3][3], int l, int c, int cont){
    printf("+---+---+---+\n");
    for(l=0; l<3; l++){
        for(c=0; c<3; c++){
            printf("|  .1", mat[l,c]);
        }
        printf("|\n");
        printf("+---+---+---+\n");
    }
}





