# **Atividade para entrega**

A NASA disponibiliza a API **Near Earth Object Web Service** (NEO), que fornece dados sobre objetos espaciais (asteroides e cometas) que passam próximos à Terra.
Sua tarefa é desenvolver um script em Python que:

1. Pergunte ao usuário uma **data inicial**. O formato que a API aceita é **YYYY-MM-DD**.
2. Pergunte ao usuário uma **data final**.
   - **Dica:** caso o usuário **não** informe a data final, considere como padrão **7 dias após a data inicial** (dica: use a biblioteca `datetime` para calcular isso).
3. Acesse a API da NASA para obter os **objetos próximos à Terra** no período especificado.
4. Organize os dados em um dicionário e exiba para cada objeto:
   - **Nome do objeto espacial**
   - **Diâmetro máximo em metros**
   - **Distância mínima da Terra (em km)**
   - **Se é potencialmente perigoso** (Sim - True ou Não - False)
   - **Corpo celeste que orbita** (exemplo: 'Earth')



---
