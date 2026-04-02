Atividade para entrega
A NASA disponibiliza a API Near Earth Object Web Service (NEO), que fornece dados sobre objetos espaciais (asteroides e cometas) que passam próximos à Terra.
Sua tarefa é desenvolver um script em Python que:
Pergunte ao usuário uma data inicial. O formato que a API aceita é YYYY-MM-DD.
Pergunte ao usuário uma data final.
Dica: caso o usuário não informe a data final, considere como padrão 7 dias após a data inicial (dica: use a biblioteca datetime para calcular isso).
Acesse a API da NASA para obter os objetos próximos à Terra no período especificado.
Organize os dados em um dicionário e exiba para cada objeto:
Nome do objeto espacial
Diâmetro máximo em metros
Distância mínima da Terra (em km)
Se é potencialmente perigoso (Sim - True ou Não - False)
Corpo celeste que orbita (exemplo: 'Earth')
Exemplo da string da API: https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-02-23&end_date=2025-02-28&api_key=DEMO_KEY
 
Entrega:
Pode ser feito em até trios.
Enviar o link para um notebook no Google Colab (verifique se está aberto para acesso!), com o nome dos integrantes e códigos.
Enviar um link em um arquivo .txt para o e-mail humberto.zanetti@fatec.sp.gov.br e humberto.zanetti@cps.sp.gov.br com o assunto "Atividade 3 - ED".
 