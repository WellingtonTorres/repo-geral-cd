import requests
from datetime import datetime, timedelta


def calcular_data_final(data_inicial: str) -> str:
    """Calcula 7 dias após a data inicial"""
    data_obj = datetime.strptime(data_inicial, '%Y-%m-%d')
    return (data_obj + timedelta(days=7)).strftime('%Y-%m-%d')


def buscar_objetos_proximos(data_inicial: str, data_final: str) -> dict:
    """Faz a requisição à API NEO da NASA e retorna os dados"""
    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={data_inicial}&end_date={data_final}&api_key=DEMO_KEY'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {'Erro': f'Falha na requisição. Status: {resposta.status_code}'}


def extrair_dados_objeto(obj: dict) -> dict:
    """Extrai e organiza os dados de um objeto espacial em um dicionário"""
    nome = obj['name']
    diametro_max = obj['estimated_diameter']['meters']['estimated_diameter_max']
    distancia_min = obj['close_approach_data'][0]['miss_distance']['kilometers']
    perigoso = obj['is_potentially_hazardous_asteroid']
    corpo_orbital = obj['close_approach_data'][0]['orbiting_body']

    return {
        'Nome': nome,
        'Diâmetro máximo (m)': round(diametro_max, 2),
        'Distância mínima da Terra (km)': round(float(distancia_min), 2),
        'Potencialmente perigoso': 'Sim' if perigoso else 'Não',
        'Corpo que orbita': corpo_orbital
    }


def exibir_objeto(asteroide: dict) -> None:
    """Exibe os dados de um objeto espacial"""
    for chave, valor in asteroide.items():
        print(f'  {chave}: {valor}')
    print()


# Solicita a data inicial ao usuário
data_inicial = input('Digite a data inicial (YYYY-MM-DD): ')

# Solicita a data final (opcional)
data_final = input('Digite a data final (YYYY-MM-DD) ou pressione Enter para 7 dias após a inicial: ')

# Se o usuário não informar a data final, calcula 7 dias após a inicial
if data_final == '':
    data_final = calcular_data_final(data_inicial)
    print(f'Data final definida automaticamente: {data_final}')

# Busca os dados na API da NASA
dados = buscar_objetos_proximos(data_inicial, data_final)

# Verifica se houve erro na requisição
if isinstance(dados, dict) and 'Erro' in dados:
    print(dados['Erro'])
else:
    # Extrai os objetos de cada data usando list comprehension
    todos_objetos = [
        extrair_dados_objeto(obj)
        for objetos in dados['near_earth_objects'].values()
        for obj in objetos
    ]

    print(f'\nTotal de objetos encontrados: {len(todos_objetos)}')

    # Exibe os objetos organizados por data
    for data, objetos in dados['near_earth_objects'].items():
        print(f'\n--- Data: {data} ({len(objetos)} objetos) ---\n')

        for obj in objetos:
            asteroide = extrair_dados_objeto(obj)
            exibir_objeto(asteroide)

    # Lista apenas os objetos potencialmente perigosos
    perigosos = [obj for obj in todos_objetos if obj['Potencialmente perigoso'] == 'Sim']

    if perigosos:
        print(f'\n*** OBJETOS POTENCIALMENTE PERIGOSOS: {len(perigosos)} ***\n')
        for asteroide in perigosos:
            exibir_objeto(asteroide)
    else:
        print('\nNenhum objeto potencialmente perigoso encontrado no período.')
