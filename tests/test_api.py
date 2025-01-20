import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # Example API for testing

# Test GET request
def test_get_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert isinstance(response.json(), list), "Response should be a list"

# Test POST request
def test_create_post():
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    assert response.json()['title'] == payload['title'], "Title mismatch in response"


# Test PUT request
def test_update_post():
    url = f"{BASE_URL}/posts/1"
    payload = {
        "id": 1,
        "title": "foo_updated",
        "body": "bar_updated",
        "userId": 1
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    assert response.json()['title'] == payload['title'], "Title mismatch in response"

# Test DELETE request
def test_delete_post():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

