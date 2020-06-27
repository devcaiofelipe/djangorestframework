import requests


class TesteCursos:
    headers = {'Authorization': 'Token 5ea7f56719d8eb6cffa69d29ceb4a952300badec'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_curso(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programacao com Ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo curso de Ruby",
            "url": "http://www.geekuniversity.com.br/ncr"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo(self):
        atualizado = {"titulo": "Novo curso de Ruby 2",
                      "url": "http://www.geekuniversity.com.br/ncr2"}

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']


    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
