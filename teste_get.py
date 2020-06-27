import requests

headers = {'Authorization': 'Token 5ea7f56719d8eb6cffa69d29ceb4a952300badec'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)


# Testando se endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros por página
assert resultado.json()['count'] == 3

# Testando primeiro registro
assert resultado.json()['results'][0]['titulo'] == 'Programação para Web com Django REST Framework'
