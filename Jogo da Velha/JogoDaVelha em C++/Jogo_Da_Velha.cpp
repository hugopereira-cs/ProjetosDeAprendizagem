#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#define N 15

void MostraPlacar(char jog1[N], char jog2[N], int emp, int totX, int totO);
void NovoJogo(int mat[3][3]);
void MostraVelha(int mat[3][3], int l, int c);
int Jogar(char simb, int mat[3][3], int l, int c, int pos, int mudou);
void MudaJogador(char *simb);
int TerminouVelha(int mat[3][3], int *totX, int *totO, int *emp);
void LimpaTela();
char NumpCarac(int num);

int main(void){
    setlocale(LC_ALL,"Portuguese");

    int mat[3][3], mudou=0, l=0, c=0, pos, totX=0, totO=0, emp=0, R=0;
    char simb='X', jog1[N], jog2[N];
    
    printf("Quem vai jogar com X?\n");
    fgets(jog1, N, stdin);
    jog1[strcspn(jog1, "\n")] = '\0';
    fflush(stdin);
    printf("Quem vai jogar com O?\n");
    fgets(jog2, N, stdin);
    jog2[strcspn(jog2, "\n")] = '\0';
    fflush(stdin);
    do
    {
        MostraPlacar(jog1, jog2, emp, totX, totO);
        NovoJogo(mat);
        MostraVelha(mat, l, c); 
        do{
            do
            {
                printf("Vai jogar %c em que posição?", simb);
                scanf("%d", &pos);
                R = Jogar(simb, mat, l, c, pos, mudou);
                if( R == 0 ){
                    printf("JOGADA INVÁLIDA");
                }
            }while (mudou == 1);
            MudaJogador(&simb);
            LimpaTela();
            MostraPlacar(jog1, jog2, emp, totX, totO);
            MostraVelha(mat,l, c);
            printf("\n");
        }while (TerminouVelha(mat, &totX, &totO, &emp) == 1);
        printf("JOGO FINALIZADO!!!\n");
        LimpaTela();           
    } while (totX + totO + emp < 7 );
    if( totX > totO ){
        printf("%s VENCEU!\n",jog1);
    }
    if( totO > totX ){
        printf("%s VENCEU!\n",jog2);
    }
    if( totO == totX ){
        printf("DEU EMPATE!");
    }
    

}

void MostraPlacar(char jog1[N], char jog2[N], int emp, int totX, int totO){
    printf("-------------\n");
    printf("   PLACAR    \n");
    printf("%-4s: %2d\n", jog1, totX);
    printf("%-4s: %2d\n", jog2, totO);
    printf("Velha: %-7d\n", emp);
    printf("-------------\n");
}

void NovoJogo(int mat[3][3]){
    int l, c, cont=1;
    for( l=0; l<3; l++ ){
        for( c=0; c<3; c++){
            mat [l][c] = NumpCarac(cont);
            cont++;
        }
    }
}

char NumpCarac(int num){
    num=0;
    return '0' + num;
}

void MostraVelha(int mat[3][3], int l, int c){
    printf("+---+---+---+\n");
    for( l=0; l<3; l++){
        for(c=0; c<3; c++){
            printf("|  %c", mat[l][c]);
        }
        printf("|\n");
        printf("+---+---+---+\n");
    }
}

int Jogar(char simb, int mat[3][3], int l, int c, int pos, int mudou){
    for( l=0; l<3; l++){
        for( c=0; c<3; c++ ){
            if( mat[l][c] == NumpCarac(pos)){
                mat[l][c] = simb;
                mudou = 1;
            }
        }
    }
    return mudou;
}

 void MudaJogador(char *simb){
    if( *simb == 'X'){
        *simb = 'O';
    }else
        *simb = 'X';    
}

 int TerminouVelha(int mat[3][3], int *totX, int *totO, int *emp){
    int terminou = 0, oc = 0, l, c;
    // jogos em linha
    for( l=0; l<3; l++ ){
        if( mat[l][0] == mat[l][1] && mat[l][1] == mat[l][2] && mat[l][0] == 'X' ){
            (*totX) += 1;
            terminou = 1;
        }
        if( mat[l][0] == mat[l][1] && mat[l][1] == mat[l][2] && mat[l][0] == 'O' ){
            (*totO) += 1;
            terminou = 1;
        }
    }
    // jogos em coluna
    for( c=0; c<3; c++ ){
        if( mat[0][c] == mat[1][c] && mat[1][c] == mat[2][c] && mat[0][c] == 'X' ){
            (*totX) += 1;
            terminou = 1;
        }
        if( mat[0][c] == mat[1][c] && mat[1][c] == mat[2][c] && mat[0][c] == 'O' ){
            (*totO) += 1;
            terminou = 1;
        }
    }
    // jogos em diagonal
    if( mat[0][0] == mat[1][1] && mat[1][1] == mat[2][2] && mat[0][0] == 'X' ){
        (*totX) += 1;
        terminou = 1;
    }
    if( mat[0][0] == mat[1][1] && mat[1][1] == mat[2][2] && mat[0][0] == 'O' ){
        (*totO) += 1;
        terminou = 1;
    }
    if( mat[0][2] == mat[1][1] && mat [1][1] == mat[2][0] && mat[0][2] == 'X' ){
        (*totX) += 1;
        terminou = 1;
    }
    if( mat[0][2] == mat[1][1] && mat [1][1] == mat[2][0] && mat[0][2] == 'O' ){
        (*totO) += 1;
        terminou = 1;
    }
    // velha
    oc = 0;
    for( l=0; l<3; l++ ){
        for( c=0; c<3; c++){
            if( mat[l][c] != 'X' && mat[l][c] != 'O' ){
                oc += 1;
            }
        }
    }
    if( oc == 0 ){
        (*emp) += 1;
        terminou = 1;
    }
    return terminou;
}
void LimpaTela(){
    #if defined(_WIN32) || defined(_WIN64)
        system("cls");
    #else
        system("clear");
    #endif
}   






