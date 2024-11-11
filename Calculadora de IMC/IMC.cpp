#include <stdio.h>
int main(){
    float imc, altura, peso;

    printf("Digite seu peso: \n") ;
    scanf("%f", &peso);
    printf("Digite sua altura: \n");
    scanf("%f", &altura);
    
    imc = peso / (altura * altura);
    printf("%.2f Kg. ", imc);

    if( imc > 0){
        if( imc < 17 ){
            printf("Cuidado! Você está muito abaixo do seu peso ideal.\n");
        } else{
            if( imc >= 17 && imc < 18.5 ){
                printf("Vovê está abaixo do seu peso ideal.\n");
            }else{
                if( imc >= 18.5 && imc < 25 ){
                    printf("Parabéns! Você está no seu peso ideal.\n");
                }else{
                    if( imc >= 25 && imc < 30 ){
                        printf("Você esta acima do seu peso ideal.\n");
                    }else{
                        if( imc >= 30 && imc < 35 ){
                            printf("Você está na faixa da obesidade.\n");
                        }else{
                            if( imc >= 35 && imc < 40 ){
                                printf("Você está na faixa de obesidade severa.\n");
                            }else if ( imc >= 40 ){
                              printf("Tenha muita atenção! Você está na faixa de obesidade mórbida.\n"); 
                            }                        
                        }
                    }
                }
            }
        }


    }



}