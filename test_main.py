from fastapi.testclient import TestClient
from main import app

clinet = TestClient(app)


def test_get_all_posts():
    response = clinet.get("/blog/all")
    assert response.status_code == 200


def test_auth_error():
    response = clinet.post(
        "/token",
        data={
            "username": "",
            "password": ""
        }
    )
    access_token = response.json().get('access_token')
    assert access_token is None

    message = response.json().get('detail')[0].get('msg')
    # assert message == ""
    assert message == "field required"


def test_auth_success():
    response = clinet.post(
        "/token",
        data={
            "username": "lixiong",
            "password": "123",
        }
    )
    access_token = response.json().get('access_token')
    assert access_token


def test_post_article():
    response = clinet.post(
        "/token",
        data={
            "username": "lixiong",
            "password": "123",
        }
    )
    access_token = response.json().get('access_token')

    assert access_token

    response = clinet.post(
        "/article/",
        json={
            "title": "test article",
            "content": "test_content",
            "published": True,
            "creator_id": 3,
        },
        headers={
            "Authorization": f"bearer{access_token}"
        }
    )
    assert response.status_code == 200
    assert response.json().get("title") == "test article"
