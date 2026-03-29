# Faca um programa em phyton ou c que:
# - Peca ao usuario para digitar as dimensoes das matrizes A(lin A, col A) e B(lin B, col B)
# - Caso 1: A multiplicacao das matrizes nao seja possível.
# -- Deve retornar ao usuário a informação devidamente justificada.
# - Caso 2: A multiplicacao das matrizes seja possivel.
# -- O usuario devera digitar todos os elementos das matrizes A e B.
# -- O programa deve exibir matriz A, matriz B e a matriz de A*B.

#func para maior legibilidade do output
def subscrito(num):
    sequencia = "0123456789"
    sub = "₀₁₂₃₄₅₆₇₈₉"
    return num.translate(str.maketrans(sequencia, sub))

def ler_matriz(nome, linhas, colunas):
    print(f'\nDigite os elementos da Matriz {nome} ({linhas}x{colunas}):')
    matriz = [[0] * colunas for _ in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            indice = subscrito(str(i + 1) + str(j + 1))
            matriz[i][j] = int(input(f'{nome}{indice}: '))
    return matriz

def exibir_matriz(nome, matriz):
    print(f'\nMatriz {nome}:')
    for i in range(len(matriz)):
        linha = "| "
        for j in range(len(matriz[i])):
            linha += f'{matriz[i][j]:4} '
        linha += "|"
        print(linha)

def multiplicar(A, B):
    linA = len(A)
    colA = len(A[0])
    colB = len(B[0])
    C = [[0] * colB for _ in range(linA)]
    for i in range(linA):
        for j in range(colB):
            for k in range(colA):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Pedir dimensoes das matrizes
linA = int(input('Digite o número de linhas da Matriz A: '))
colA = int(input('Digite o número de colunas da Matriz A: '))
linB = int(input('Digite o número de linhas da Matriz B: '))
colB = int(input('Digite o número de colunas da Matriz B: '))

# Verificar se a multiplicacao e possivel
if colA != linB:
    print(f'\nA multiplicação A({linA}x{colA}) * B({linB}x{colB}) NÃO é possível!')
    print(f'Justificativa: o número de colunas de A ({colA}) deve ser igual ao número de linhas de B ({linB}).')
else:
    # Ler elementos das matrizes
    A = ler_matriz('A', linA, colA)
    B = ler_matriz('B', linB, colB)

    # Calcular A * B
    C = multiplicar(A, B)

    # Exibir resultados
    exibir_matriz('A', A)
    exibir_matriz('B', B)
    exibir_matriz('A*B', C)
