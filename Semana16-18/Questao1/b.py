elementos = 20

def sequencia_b(saida):
    sequencia = []
    i = 1
    j = 0
    while i <= saida:
        j = j + i
        sequencia.append(j)
        i +=1
    return sequencia

print('Saidas:')
sequencia_b(elementos)