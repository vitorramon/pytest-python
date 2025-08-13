# import requests

# def get_post(post_id):
#     """Função real que faz uma chamada para uma API."""
#     response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
#     return response

# def test_api_with_mocked_response(requests_mock):
#     """Usa requests-mock para simular a resposta da API."""
#     # Define o endpoint e a resposta simulada
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     mocked_json = {"userId": 1, "id": 1, "title": "mocked title", "body": "mocked body"}
#     requests_mock.get(url, json=mocked_json, status_code=200)

#     response = get_post(1)
#     assert response.status_code == 200
#     assert ai-response.json() == mocked_json

# def test_api_with_real_response():
#     """Opcional: teste real sem mock, acessando a API pública de verdade."""
#     response = get_post(1)
#     assert response.status_code == 200
#     data = ai-response.json()
#     assert "userId" in data
#     assert data["id"] == 1
