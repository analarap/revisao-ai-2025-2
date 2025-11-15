from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_deve_retornar_200_quando_cartao_valido():
    response = client.get("/cartao/BIBLIOTECA-ALUNO-001")  # rota da api
    assert response.status_code == 200  # retorno de codigo
    assert response.json() == {"card": "BIBLIOTECA-ALUNO-001", "valid": True} # é o conteudo esperado pela api


def test_deve_retornar_400_quando_cartao_invalido():
    response = client.get("/cartao/INVALIDO")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cartão inválido"}


def test_deve_retornar_404_quando_cartao_vazio():
    response = client.get("/cartao/")
    assert response.status_code == 404
    assert response.json()
