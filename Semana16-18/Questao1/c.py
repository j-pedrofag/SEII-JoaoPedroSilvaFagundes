elementos = 20

def sequencia_c(saida):
    sequencia = []
    i = 1
    while i <= saida:
        j = i*i
        sequencia.append(j)
        i +=1
    return sequencia 

print('Saidas:')
sequencia_c(elementos)