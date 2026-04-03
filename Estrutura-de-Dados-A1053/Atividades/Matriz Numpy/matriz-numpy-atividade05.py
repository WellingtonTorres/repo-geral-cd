import numpy as np

#1º etapa: Criação da matriz
matriz = np.random.randint(0, 100, size=(5, 5))

## 2º etapa: Salvamento em arquivo
np.savetxt('matriz_original.csv', matriz, delimiter=',', fmt='%.0f')
#outra forma
# with open('matriz_original.csv', 'w') as arquivo:
#     for linha in matriz:
#         arquivo.write(','.join(map(str, linha)) + '\n')

## 3º etapa: Leitura do arquivo
with open('matriz_original.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f'Conteúdo do arquivo:\n{conteudo}\n')


print(f'Matriz original:\n{matriz}\n')

## 4º etapa: Manipulação

# Extrair a submatriz central 3x3
submatriz = matriz[1:4, 1:4].copy()
print(f'Submatriz central 3x3:\n{submatriz}\n')

# Achatar e ordenar a submatriz
submatriz_achatada = submatriz.flatten()
submatriz_ordenada = np.sort(submatriz_achatada)
print(f'Submatriz achatada e ordenada: {submatriz_ordenada}\n')

# Reinserir os valores ordenados no centro da matriz
matriz[1:4, 1:4] = submatriz_ordenada.reshape(3, 3)
print(f'Matriz com submatriz ordenada reinserida:\n{matriz}\n')

# Calcular estatísticas da matriz geral e da submatriz central
estatisticas = {
    'Matriz Geral': {
        'Media': np.mean(matriz),
        'Mediana': np.median(matriz),
        'Maximo': np.max(matriz),
        'Minimo': np.min(matriz)
    },
    'Submatriz Central': {
        'Media': np.mean(submatriz),
        'Mediana': np.median(submatriz),
        'Maximo': np.max(submatriz),
        'Minimo': np.min(submatriz)
    }
}

# Salvar estatísticas em arquivo separado
with open('estatisticas.csv', 'w') as arquivo:
    arquivo.write('Origem,Media,Mediana,Maximo,Minimo\n')
    for origem, valores in estatisticas.items():
        arquivo.write(f"{origem},{valores['Media']:.2f},{valores['Mediana']:.2f},{valores['Maximo']},{valores['Minimo']}\n")

print('Estatísticas:')
for origem, valores in estatisticas.items():
    print(f'  {origem}: Média={valores["Media"]:.2f}, Mediana={valores["Mediana"]:.2f}, Máximo={valores["Maximo"]}, Mínimo={valores["Minimo"]}')
print()

# Trocar linhas pares pelas ímpares (índices 0,2,4 <-> 1,3)
matriz_trocada = matriz.copy()
# Troca linha 0 <-> linha 1
matriz_trocada[[0, 1]] = matriz_trocada[[1, 0]]
# Troca linha 2 <-> linha 3
matriz_trocada[[2, 3]] = matriz_trocada[[3, 2]]
# Linha 4 permanece (não tem par para trocar)
print(f'Matriz com linhas pares e ímpares trocadas:\n{matriz_trocada}\n')

# Gerar a transposta
matriz_transposta = matriz_trocada.T
print(f'Matriz transposta:\n{matriz_transposta}\n')

## 5º etapa: Salvamento final
np.savetxt('matriz_final.csv', matriz_transposta, delimiter=',', fmt='%.0f')
print('Matriz final salva em matriz_final.csv')