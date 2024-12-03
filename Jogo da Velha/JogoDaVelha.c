#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#define N 50

void MostraPlacar(char p1[N], char p2[N], int e, int tX, int tO);
void NovoJogo(int mat[3][3], int l, int c, int cont);
void MostraVelha(int mat[3][3], int l, int c, int cont);
int Jogar(char s, int mat[3][3], int l, int c, int p, int mudou);
void MudaJogador(char simb);
int TerminouVelha(int mat[3][3], int terminou, int l, int c, int totX, int totO, int oc, int emp);

int main(){
    setlocale(LC_ALL,"Portuguese");

    char mat[3][3],jog1[N], jog2[N], simb='X';
    int l, c, pos, cont=1, totX=0, totO=0, emp=0, i1, i2, R, mud, term, ocor;
    
    

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
        do{
            do
            {
                printf("Vai jogar [%c:1", simb, "] em que posição?");
                scanf("%d", pos);
                R = Jogar(simb, mat[3][3], l, c, pos, mud);
                if( R == 0){
                    printf("JOGADA INVÁLIDA");
                }
            }while (R == 1);
            MudaJogador(simb);

        }while (TerminouVelha(mat[3][3], term, l, c, totX, totO, ocor, emp) == 1);
           
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

void NovoJogo(int mat[3][3], int l, int c, int cont){
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

void MostraVelha(int mat[3][3], int l, int c, int cont){
    printf("+---+---+---+\n");
    for( l=0; l<3; l++){
        for(c=0; c<3; c++){
            printf("|  .1", mat[l,c]);
        }
        printf("|\n");
        printf("+---+---+---+\n");
    }
}

int Jogar(char s, int mat[3][3], int l, int c, int p, int mudou){
    mudou = 0;
    for( l=0; l<3; l++){
        for( c=0; c<3; c++){
            if( mat[l][c] == NumpCarac(p)){
                mat[l][c] = s;
                mudou = 1;
            }
        }
    }
    return mudou;
}

 void MudaJogador(char simb){
    if( simb == 'X'){
        simb = 'O';
    }else
        simb = 'X';    
}

 int TerminouVelha(int mat[3][3], int terminou, int l, int c, int totX, int totO, int oc, int emp){
    terminou = 0;
    // jogos em linha
    for( l=0; l<3; l++ ){
        if( mat[l][1] == mat[l][2] && mat[l][2] == mat[l][3] && mat[l][1] == 'X' ){
            totX += 1;
            terminou = 1;
        }
        if( mat[l][1] == mat[l][2] && mat[l][2] == mat[l][3] && mat[l][1] == 'O' ){
            totO += 1;
            terminou = 1;
        }
    }
    // jogos em coluna
    for( c=0; c<3; c++ ){
        if( mat[1][c] == mat[2][c] && mat[2][c] == mat[3][c] && mat[1][c] == 'X' ){
            totX += 1;
            terminou = 1;
        }
        if( mat[1][c] == mat[2][c] && mat[2][c] == mat[3][c] && mat[1][c] == 'O' ){
            totO += 1;
            terminou = 1;
        }
    }
    // jogos em diagonal
    if( mat[1][1] == mat[2][2] && mat[2][2] == mat[3][3] && mat[1][1] == 'X' ){
        totX += 1;
        terminou = 1;
    }
    if( mat[1][1] == mat[2][2] && mat[2][2] == mat[3][3] && mat[1][1] == 'O' ){
        totO += 1;
        terminou = 1;
    }
    if( mat[1][3] == mat[2][2] && mat [2][2] == mat[3][1] && mat[1][3] == 'X' ){
        totX += 1;
        terminou = 1;
    }
    if( mat[1][3] == mat[2][2] && mat [2][2] == mat[3][1] && mat[1][3] == 'O' ){
        totO += 1;
        terminou = 1;
    }
    // velha
    oc = 0;
    for( l=0; l<3; l++){
        for( c=0; c<3; c++){
            if( mat[l][c] != 'X' && mat[l][c] != 'O' ){
                oc += 1;
            }
        }
    }
    if( oc == 0 ){
        emp += 1;
        terminou = 1;
    }
    return terminou;
}   






