# T1- Matriz Triangular
# Faça um programa em Python que:
# Peça ao usuário para digitar todos os elementos uma matriz A45
# * Deve retornar:
#  - Matriz A
#  - Matriz A Superior
#  - Matriz B Inferior

#Digite os elementos da Matriz A45:

#func para maior legibilidade do output
def subscrito(num):
    sequencia = "0123456789"
    sub = "₀₁₂₃₄₅₆₇₈₉"
    return num.translate(str.maketrans(sequencia, sub))

def exibir_matriz(nome, mat):
    print(f'\n{nome}:')
    for linha in mat:
        print('| ' + '  '.join(f'{v:3}' for v in linha) + ' |')

print('Digite os elementos da Matriz A₄₅:')

nLinhas = 4
nColunas = 5
matriz = [[0] * nColunas for _ in range(nLinhas)]

for i in range(nLinhas):
    for j in range(nColunas):
        sExibeElemMatriz = subscrito(str(i + 1) + str(j + 1))
        matriz[i][j] = int(input(f'A{sExibeElemMatriz}: '))

# Exibe Matriz A
exibir_matriz('Matriz A', matriz)

# Monta Matriz A Superior (zeros abaixo da diagonal)
matSuperior = [[0] * nColunas for _ in range(nLinhas)]
for i in range(nLinhas):
    for j in range(nColunas):
        if i <= j:
            matSuperior[i][j] = matriz[i][j]

exibir_matriz('Matriz A Superior', matSuperior)

# Monta Matriz B Inferior (zeros acima da diagonal)
matInferior = [[0] * nColunas for _ in range(nLinhas)]
for i in range(nLinhas):
    for j in range(nColunas):
        if i >= j:
            matInferior[i][j] = matriz[i][j]

exibir_matriz('Matriz B Inferior', matInferior)
