import pytest


from rest_framework.test import APIClient


from user.models import User

@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    
    new_user = {
        "username": "tbratik_test",
        "password": "tbratik1234",
        "mail": "t_bratik83@test.com",
        "birth_day": "2003-07-15",
        "phone": "3586018120",
        "name": "Thomas Elser Bratik",
        "role": "customer",
        "document": "44973692"
    }
    
    response = client.post("/users/register/", new_user, format="json")
    print("POST Response:", response.data)
    
    assert response.status_code == 201
    assert "id" in response.data["data"]

@pytest.mark.django_db
def test_user_list():
    client = APIClient()

    
    User.objects.create(
        username="tbratik_test",
        password="tbratik1234",
        mail="t_bratik83@test.com",
        birth_day="2003-07-15",
        phone="3586018120",
        name="Thomas Elser Bratik",
        role="customer",
        document="44973692"
    )

    response = client.get("/users/list/")
    
    print("GET Status:", response.status_code)
    print("GET Data Raw:", response.data)
    
    assert response.status_code == 200
    
    users = response.data.get("data", [])
    
    print("Usuarios listados:", users)
    assert len(users) > 0
