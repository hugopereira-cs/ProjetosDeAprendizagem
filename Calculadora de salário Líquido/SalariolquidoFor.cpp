#include <stdio.h>
#include <stdlib.h>
int main()
{
    int cont;
    float sBrut, sLiq, imp, totBrut=0, totLiq=0, totImp=0;

    for(cont = 1; cont <= 15; cont++)
    {
        printf("Digite o salário bruto do funcionário: \n");
        scanf("%f", &sBrut);
        if( sBrut >= 0 && sBrut <= 999 )
        imp = sBrut *0.10;
        else
            if( sBrut <=1999 )
            imp = sBrut *0.15;
            else
                if( sBrut <=9999 )
                imp = sBrut *0.20;
                else
                    if( sBrut <=99999 )
                    imp = sBrut *0.25;
                    else
                    imp = sBrut *0.30;
                    sLiq = sBrut - imp;
        printf("O salário líquido deste funcionário é %.2f \n", sLiq);
        totBrut = totBrut + sBrut;
        totLiq = totLiq + sLiq;
        totImp = totImp + imp;
        cont++;           
    } 
    printf("Total de salário bruto: %.2f \n", totBrut);
    printf("Total de salário líquido: %.2f \n", totLiq);
    printf("Total de imposto: %.2f\n", totImp);
    return 0;
}