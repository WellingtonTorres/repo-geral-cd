# Faca um programa em phyton ou c que:
# - Peca ao usuario para digitar as dimensoes das matrizes A(lin A, col A) e B(lin B, col B)
# - Caso 1: A soma das matrizes nao seja possível.
# -- Deve retornar ao usuário a informação devidamente justificada.
# - Caso 2: A soma das matrizes e possivel.
# -- O usuario devera digitar todos os elementos das matrizes A e B.
# -- O programa deve exibir matriz A, matriz B e a matriz de A+B.

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
        linha = "| " + "  ".join(f'{matriz[i][j]:3}' for j in range(len(matriz[i]))) + "  |"
        print(linha)

# Leitura das dimensoes
print('=== Soma de Matrizes ===\n')

linA = int(input('Número de linhas da Matriz A: '))
colA = int(input('Número de colunas da Matriz A: '))
linB = int(input('Número de linhas da Matriz B: '))
colB = int(input('Número de colunas da Matriz B: '))

# Verificacao de compatibilidade
if linA != linB or colA != colB:
    print(f'\nA soma das matrizes A({linA}x{colA}) e B({linB}x{colB}) não é possível!')
    print('Justificativa: Para somar duas matrizes, elas devem ter as mesmas dimensões (mesmo número de linhas e colunas).')
else:
    # Leitura dos elementos
    A = ler_matriz('A', linA, colA)
    B = ler_matriz('B', linB, colB)

    # Calculo da soma A + B
    soma = [[A[i][j] + B[i][j] for j in range(colA)] for i in range(linA)]

    # Exibicao dos resultados
    exibir_matriz('A', A)
    exibir_matriz('B', B)
    exibir_matriz('A+B', soma)
