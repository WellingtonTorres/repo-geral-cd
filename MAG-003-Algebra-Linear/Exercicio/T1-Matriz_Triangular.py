# T1- Matriz Triangular
# Faça um programa em Python que:
# Peça ao usuário para digitar todos os elementos uma matriz A45
# * Deve retornar:
#  - Matriz A
#  - Matriz A Superior
#  - Matriz B Inferior
# QUESTIONAR A PROFESSORA SOBRE A45, POIS NAO HA MATRIZ TRIANGULAR REAL SE NAO FOR QUADRATICA

#Digite os elementos da Matriz A45:

#func para maior legibilidade do output
def subscrito(num):
    sequencia = "0123456789"
    sub = "₀₁₂₃₄₅₆₇₈₉"
    return num.translate(str.maketrans(sequencia, sub))

print('Digite os elementos da Matriz Triangular A₄₅:')

nLinhas = 3
nColunas = 3
sExibeElemMatriz = ""
# matriz = [[0] * nColunas] * nLinhas # dessa forma cria referência da lista na mesma lista
matriz = [[0] * nColunas for _ in range(nLinhas)]
lSuperior = True
lInferior = True
elemento = ""


#apenas verifico
print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        sExibeElemMatriz = str(i + 1) + str(j + 1)
        sExibeElemMatriz = subscrito(sExibeElemMatriz)
        matriz[i][j] = int(input(f'A{sExibeElemMatriz}: '))
        if i > j: #avaliando inferior
            if matriz[i][j] > 0:
                lInferior = False
        if i < j: #avaliando superior
            if matriz[i][j] > 0:
                lSuperior = False


if lSuperior and not lInferior:
    print(f'É uma matriz triangular superior!')
elif lInferior and not lSuperior:
    print(f'É uma matriz triangular inferior!')
else:
    print(f'Não é uma matriz triangular!')
    
if lSuperior or lInferior:    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = str(matriz[i][j])
            if i > j: #avaliando inferior
                if matriz[i][j] > 0:
                    if lInferior:
                        print("\033[1;32;40m| " + " ".join(f'{elemento:2}') + " |", end=" " )
                    else:
                        print("| " + " ".join(f'{elemento:2}') + " |", end=" " )
            elif i < j: #avaliando superior
                if lSuperior:
                     print("\033[1;32;40m| " + " ".join(f'{elemento:2}') + " |", end=" " )
                else:
                    print("| " + " ".join(f'{elemento:2}') + " |", end=" " )
            else:
                print("\033[1m| " + " ".join(f'{elemento:2}') + " |", end=" " )
            
            if len(matriz[i]) == (j + 1):
                print('\n')
            
        

#     for j in range(nColunas):


# print("matriz A" + subscrito(45)) 
