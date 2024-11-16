import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from wallet.models import Wallet, Transaction
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Fixtures
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(email, password):
        user = User.objects.create_user(
            email=email, 
            password=password, 
        )
        Wallet.objects.create(user=user, balance=100.0, is_enabled=True)
        return user
    return _create_user

@pytest.fixture
def authenticated_client(api_client, create_user):
    user = create_user(email="testuser@example.com", password="password123")
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client, user

# Test Signup API
@pytest.mark.django_db
def test_signup(api_client):
    payload = {
        "email": "newuser@example.com",
        "password": "securepassword123",
    }
    url = reverse("signup")
    response = api_client.post(url, payload)
    print(payload)
    print(response)
    assert response.status_code == 201
    assert "refresh" in response.data
    assert "access" in response.data
    assert User.objects.filter(email="newuser@example.com").exists()
    assert Wallet.objects.filter(user__email="newuser@example.com").exists()

# Test Login API
@pytest.mark.django_db
def test_login(api_client, create_user):
    user = create_user(email="testlogin@example.com", password="password123")
    payload = {"email": "testlogin@example.com", "password": "password123"}
    url = reverse("login")
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 200
    assert "refresh" in response.data
    assert "access" in response.data
    assert "user" in response.data
    assert response.data["user"]["email"] == user.email

# Test Wallet Status
@pytest.mark.django_db
def test_wallet_status(authenticated_client):
    api_client, user = authenticated_client
    url = reverse("status")
    response = api_client.get(url)
    assert response.status_code == 200
    wallet = Wallet.objects.get(user=user)
    assert response.data["status"] == wallet.is_enabled

# Test Enable Wallet
@pytest.mark.django_db
def test_enable_wallet(authenticated_client):
    api_client, user = authenticated_client
    wallet = Wallet.objects.get(user=user)
    wallet.is_enabled = False
    wallet.save()
    url=reverse("enable_wallet")
    response = api_client.post(url)
    assert response.status_code == 200
    assert response.data["message"] == "Wallet Enabled Successfully"
    wallet.refresh_from_db()
    assert wallet.is_enabled

# Test Add Money
@pytest.mark.django_db
def test_add_money(authenticated_client):
    api_client, user = authenticated_client
    payload = {"amount": 50.0}
    url=reverse("add_money")
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 200
    wallet = Wallet.objects.get(user=user)
    assert wallet.balance == 150.0  # Initial balance 100 + 50 added

# Test Remove Money
@pytest.mark.django_db
def test_remove_money(authenticated_client):
    api_client, user = authenticated_client
    payload = {"amount": 50.0}
    url=reverse("remove_money")
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 200
    wallet = Wallet.objects.get(user=user)
    assert wallet.balance == 50.0  # Initial balance 100 - 50 removed

# Test Transaction History
@pytest.mark.django_db
def test_transaction_history(authenticated_client):
    api_client, user = authenticated_client
    payload = {"amount": 50.0}
    url=reverse("add_money")
    response = api_client.post(url, payload, format="json")
    url=reverse("transaction_history")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1   
    print(response.data)
    assert response.data[0]["transaction_type"] == "add"
    assert float(response.data[0]["amount"]) == 50.0
    

# Test Wallet Balance
@pytest.mark.django_db
def test_wallet_balance(authenticated_client):
    api_client, user = authenticated_client
    url= reverse("balance")
    response = api_client.get(url)
    assert response.status_code == 200
    wallet = Wallet.objects.get(user=user)
    assert response.data["balance"] == wallet.balance



# Test Add Money
@pytest.mark.django_db
def test_fail_add_money(authenticated_client):
    api_client, user = authenticated_client
    wallet = Wallet.objects.get(user=user)
    wallet.is_enabled = False
    wallet.save()
    payload = {"amount": 50.0}
    url = reverse("add_money")
    response = api_client.post(url, payload, format="json")
    print(response.data)  # Debugging: Print the response data
    
    assert response.status_code == 400  # Expected failure status code
    assert response.data == {'error': "wallet is disabled"}  # Expected error message

   
@pytest.mark.django_db
def test_add_money_unauthenticated(api_client):
 
    url = reverse("add_money")
    payload = {"amount": 50.0}
    response = api_client.post(url, payload, format="json")  # No authentication provided

    assert response.status_code == 401  # Unauthorized
    assert response.data["detail"] == "Authentication credentials were not provided."