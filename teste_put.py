import requests

headers = {'Authorization': 'Token 5ea7f56719d8eb6cffa69d29ceb4a952300badec'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

resultado = requests.put(f'{url_base_cursos}2/', headers=headers, data=curso_atualizado)
print(resultado.json())

# Testando o codigo de status HTTP
assert resultado.status_code == 200

# Testando se o titulo foi alterado
assert resultado.json()['titulo'] == curso_atualizado['titulo']