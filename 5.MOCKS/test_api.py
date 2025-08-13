#import requests

# def test_api_call_real_1():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#     assert response.status_code == 200
#     data = ai-response.json()
#     assert "userId" in data
#     assert "title" in data

# def test_api_call_real_2():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
#     assert response.status_code == 200
#     data = ai-response.json()
#     assert isinstance(data["id"], int)
#     assert data["id"] == 2

# def test_api_call_real_3():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/3")
#     assert response.status_code == 200
#     data = ai-response.json()
#     assert "body" in data
#     assert isinstance(data["body"], str)