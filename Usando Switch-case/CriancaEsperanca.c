#include <stdio.h>
int main(){

    int numero;
    float valor;

    printf("---------------------------\n");
    printf("     Criança Esperança     \n");
    printf("---------------------------\n");
    printf(" Muito obrigado por ajudar \n");
    printf(" [1] para doar R$10 \n");
    printf(" [2] para doar R$25 \n");
    printf(" [3] para doar R$50 \n");
    printf(" [4] para doar outros valores \n");
    printf(" [5] para cancelar \n");
    scanf("%d", &numero);
    
    switch(numero){
        case 1: {
            valor = 10;
            break;
        }
        case 2: {
            valor = 25;
            break;
        }
        case 3: {
            valor = 50;
            break;
        }
        case 4: {
            printf("Qual o valor da doação?\n");
            scanf("%f", &valor);
            break;    
        }
        case 5: {
            valor = 0;
            break;        
        }
        
    }
    printf("------------------------\n");
    printf(" SUA DOAÇÃO FOI DE R$%.2f.\n", valor);
    printf(" MUITO OBRIGADO!\n");
    printf("------------------------\n");

    return 0;
}