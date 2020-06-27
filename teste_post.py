import requests

headers = {'Authorization': 'Token 5ea7f56719d8eb6cffa69d29ceb4a952300badec'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência agil de Projeto com Scrum 2",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

resultado = requests.post(url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status http 201
assert resultado.status_code == 201

# Testando se o titulo do curso criado ou retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']