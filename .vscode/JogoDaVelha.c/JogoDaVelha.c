#include <stdio.h>
#include <stdlib.h>


//variáveis globais

char game[3][3]; //matriz (tabuleiro)

int column, row;

//funções e procedimentos

void init(void);

void show_game();

int win_row(int, char);

int win_rows(char);

int win_column(int, char);

int win_columns(char);

int win_principal_diag(char);

int win_secondary_diag(char);

int valid(int, int);

void read_coordinates(char);

int empty_posit();

void play();


int main ()
{
    int option;

    do
    {
        init();

        play();

        printf("\nDigite 1 para jogar novamente.");

        scanf("%d", &option);

        fflush(stdin);

    }while (option == 1);

    return 0;
}

//função que inicializa todas as posições da matriz

void init(void)
{
    for (row = 0; row < 3; row ++)
    {
        for (column = 0; column <3; column ++)

            game[row][column] = ' ';        
    }
}

//função que mostra o placar



//função que imprime o jogo

void show_game()
{
    printf("\n\n\t\t 0   1   2\n\n");

    for (row = 0; row < 3; row ++)
    {
        for (column = 0; column <3; column ++)
        {
            if (column == 0)
            
                printf("\t\t");

            printf(" %c ", game[row][column]);
            
            if (column < 2)

                printf("|");

            if (column == 2)

                printf("   %d", row);
            
        }
        printf("\n");

        if (row < 2)

            printf("\t\t-----------\n");
    }
}

/*
    função que verifica se houve vitória em uma linha
    1 - houve
    0 - não houve
*/

int win_row(int row, char c)
{
    if (game[row][0] == c && game[row][1] == c && game[row][2] == c)
        return 1;
    else
        return 0;    
}

/*
    função que verifica se houve vitória em linhas
    1 - houve
    0 - não houve
*/

int win_rows(char c)
{
    int win = 0;

    for (row = 0; row < 3; row ++)
    {
       win += win_row(row, c); 
    }
    return win;
}

/*
    função que verifica se houve vitória em uma coluna
    1 - houve
    0 - não houve
*/

int win_column(int column, char c)
{
    if (game[0][column] == c && game[1][column] == c && game[2][column] == c)
        return 1;
    else
        return 0;
}
/*
    função que verifica se houve vitória em colunas
    1 - houve
    0 - não houve
*/

int win_columns(char c)
{
    int win = 0;

    for (column = 0; column <3; column ++)
    {
        win += win_column(column, c);
    }
    return win;
}

/*
    função que verifica se houve vitória na diagonal principal
    1 - houve
    0 - não houve
*/

int win_principal_diag(char c)
{
    if (game[0][0] == c && game[1][1] == c && game[2][2] ==c)
        return 1;
    else
        return 0;
}

/*
    função que verifica se houve vitória na diagonal secundária
    1 - houve
    0 - não houve
*/

int win_secondary_diag(char c)
{
    if (game[0][2] == c && game[1][1] == c && game[2][0])
        return 1;
    else
        return 0;
}

/*
    função que verifica se uma coordenada é válida
    1 - é válida
    0 - não é válida
*/

int valid(int row, int column)
{
    if (row >= 0 && row < 3 && column >= 0 && column < 3 && game[row][column] == ' ')
        return 1;
    else
        return 0;
}

/*
    procedimento que lê as coordenadas do jogador
    r -> variável para coordenada de linha
    col -> variável para coordenada de coluna
*/

void read_coordinates(char p)
{
    int r, col;

    printf("Digite linha e coluna: ");

    scanf("%d%d", &r, &col);

    fflush(stdin);

    while (valid(r, col) == 0)
    {
        printf("Coordenadas iválidas!!! Digite linha e coluna novamente: ");

        scanf("%d%d", &r, &col);

        fflush(stdin);
    }
    game[r][col] = p;

}

//função para retornar quantidade de posções vazias

int empty_posit()
{
    int number_empty_positions = 0;

    for (row = 0; row <3; row ++)
    {
        for (column = 0; column < 3; column ++)
        
            if(game[row][column] == ' ')

                number_empty_positions ++;
            
        
    }
    return number_empty_positions;
}

//procedimento para jogar

void play()
{
    int player = 1, X_win = 0, O_Win = 0;

    char player1 = 'X', player2 = 'O';

    do
    {
        show_game();

        if(player == 1)
        {
            read_coordinates(player1);
            
            player++;
            
            X_win += win_rows(player1);

            X_win += win_columns(player1);

            X_win += win_principal_diag(player1);

            X_win += win_secondary_diag(player1);
        }
        else
        {
            read_coordinates(player2);
            
            player = 1;
            
            O_Win += win_rows(player2);

            O_Win += win_columns(player2);

            O_Win += win_principal_diag(player2);

            O_Win += win_secondary_diag(player2);  
        }
    }while (X_win == 0 && O_Win == 0 && empty_posit() > 0);

    show_game();

    if(O_Win == 1)

        printf("\nParabéns Jogador 2. Você venceu!!!\n");

    else if(X_win == 1)

        printf("\nParabéns Jogador 1. Você venceu!!!\n");  

    else
    
        printf("\nDeu velha!!!\n");
}