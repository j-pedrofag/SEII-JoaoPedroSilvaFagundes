elementos = 20

def sequencia_a(saida):
    sequencia = []
    i = 1
    j = 1 
    while i <= saida:
        sequencia.append(j)
        j += 2
        i += 1
    return sequencia

print('Saidas:')
sequencia_a(elementos)