import pandas as pd
import matplotlib.pyplot as plt

## 1º etapa: Leitura do arquivo CSV
df = pd.read_csv('despesas.csv')

## 2º etapa: Exibir as 5 primeiras linhas
print('5 primeiras linhas do DataFrame:')
print(df.head())
print()

## 3º etapa: Informações sobre os tipos
print('Informações do DataFrame:')
df.info()
print()

## 4º etapa: Converter a coluna mes para categórica (ordem janeiro a junho)
ordem_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
df['mes'] = pd.Categorical(df['mes'], categories=ordem_meses, ordered=True)
print('Tipos após conversão da coluna "mes" para categórica:')
print(df.dtypes)
print()

## 5º etapa: Total de despesas por mês
total_por_mes = df.groupby('mes', observed=True)['valor_despesa'].sum()
print('Total de despesas por mês:')
print(total_por_mes)
print()

## 6º etapa: Total de despesas por tipo de despesa
total_por_categoria = df.groupby('despesa', observed=True)['valor_despesa'].sum()
print('Total de despesas por categoria:')
print(total_por_categoria)
print()

## 7º etapa: Gráfico de barras - total de despesas por mês
plt.figure(figsize=(8, 5))
plt.bar(total_por_mes.index.astype(str), total_por_mes.values, color='steelblue')
plt.title('Total de Despesas por Mês (2024)')
plt.xlabel('Mês')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=30)
for i, v in enumerate(total_por_mes.values):
    plt.text(i, v + 2, f'R$ {v:.2f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('grafico_despesas_por_mes.png')
plt.show()

## 8º etapa: Gráfico de barras - total de despesas por categoria
plt.figure(figsize=(6, 5))
plt.bar(total_por_categoria.index, total_por_categoria.values, color=['orange', 'green'])
plt.title('Total de Despesas por Categoria (2024)')
plt.xlabel('Categoria de Despesa')
plt.ylabel('Valor Total (R$)')
for i, v in enumerate(total_por_categoria.values):
    plt.text(i, v + 5, f'R$ {v:.2f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('grafico_despesas_por_categoria.png')
plt.show()