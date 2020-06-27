import requests

headers = {'Authorization': 'Token 5ea7f56719d8eb6cffa69d29ceb4a952300badec'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}2/', headers=headers)
print(resultado)

# Testando o codigo HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho
assert len(resultado.text) == 0