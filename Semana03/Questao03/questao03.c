#include <stdio.h>
#include <stdlib.h>

void torrehanoi(int n, char a, char b, char c)
{
/* mova n discos do pino a para o pino b usando o pino c como intermediario                    */
    if (n == 1)
        printf("mova disco %d de %c para %c\n", n, a, b);
    else
    {
        torrehanoi(n - 1, a, c, b);                            // H1
        printf("mova disco %d de %c para %c\n", n, a, b);
        torrehanoi(n - 1, c, b, a);                            // H2
    }
}

int main(void)
{
    int NumeroDiscos;
    printf("Informe o numero n de discos: ");
    scanf("%d", &NumeroDiscos);
    printf("O numero n de discos informado foi: %d \n", NumeroDiscos);
    printf("A sequencia de comandos a ser executados para resolver a torre de Hanoi e a seguinte: \n\n");
    torrehanoi(NumeroDiscos, 'A', 'B', 'C');
    return 0;
}
