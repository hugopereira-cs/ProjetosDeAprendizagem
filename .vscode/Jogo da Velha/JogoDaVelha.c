#include <stdio.h>
#include <stdlib.h>

void MostraPlacar(char p1, char p2, int e, int tX, int tO);
void NovoJogo(char mat[3][3], int l, int c, int cont);

int main(){
    char mat[3][3],jog1, jog2, simb='X';
    int l, c, pos, cont=1, totX=0, totO=0, emp=0; 

    printf("Quem vai jogar com X?\n");
    scanf(" %c", &jog1);
    printf("Quem vai jogar co O?\n");
    scanf(" %c", &jog2);
    do
    {
        MostraPlacar(jog1, jog2, emp, totX, totO);
        NovoJogo(mat[3][3], l, c, cont);
            
    } while (totX + totO + emp == 7);
    

}

void MostraPlacar(char p1, char p2, int e, int tX, int tO){
    printf("-------------\n");
    printf("   PLACAR    \n");
    printf("%c.10, %d.2\n", p1, tX);
    printf("%c.10, %d.2\n", p2, tO);
    printf("Velha .10 \n", e);
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



