## Project Setup

### Prerequisites
- **Python 3.x** must be installed.
- **pip** (Python package installer) must be available.

### Steps to Setup the Project Locally
1. **Clone the Repository and setup virtual environment**
   ```bash
   git clone https://github.com/Saifalicoder/PyWallet.git
   cd Pywallet
   python -m venv venv
   venv\Scripts\activate
   ```
2. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup Database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. **IRun the Development Server**
   ```bash
   python manage.py runserver
   ```
4. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
## Backend API Doc

## Signup

|![Static Badge](https://img.shields.io/badge/Method-POST-GREEN)| ```/api/signup/``` |
| :-------- | :------------------------- |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`| `string`  | **Required.** email |
| `password`| `string`  | **Required.** password |


**Example**
```http
{
    "email":"email@email.com",
    "password": "password",
}
```
**Response**
```http
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTY4MTEyNCwiaWF0IjoxNzMxNTk0NzI0LCJqdGkiOiJhYTUzYTIyN2RmOGU0Yzk2YmMxMWUwNzQ2MjVhNWRiZSIsInVzZXJfaWQiOjN9.U_52kcyCXdWnSNFMLnffiFISJBUBNCdiZY65q27McO0",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTk2NTI0LCJpYXQiOjE3MzE1OTQ3MjQsImp0aSI6IjM5ZTk3MjBjNDk4ODRhNmU4MWYyMGI3YTFhZmVjODUxIiwidXNlcl9pZCI6M30.LGCfqmME1e3AXPPO7OeoymkmKgwg0yTl7RQw5IYuf3Q"
}
```

## Login

|![Static Badge](https://img.shields.io/badge/Method-POST-GREEN)| ```/api/token/``` |
| :-------- | :------------------------- |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required.** email |
| `password`| `string`  | **Required.** password |


**Example**
```http
{
    "email": "email",
    "password": "password",
}
```
**Response**
```http
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTc1NjE0OSwiaWF0IjoxNzMxNjY5NzQ5LCJqdGkiOiIxNGEyN2E0MDVjZTE0Zjc0OWEwMDA1YmNkMzIyNzllMCIsInVzZXJfaWQiOjN9.ew2cWp_-1FFWzuTwkCS2pDAtobzDDXtrc1PM3AQX3Fc",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNjcxNTQ5LCJpYXQiOjE3MzE2Njk3NDksImp0aSI6ImZmNDBiZTM2NDAzZjRhYzNhM2MzYzczNmM0MjI3NjAwIiwidXNlcl9pZCI6M30.1qP0WUPOM3e1jHmJI1jdNaOjFgTIo5K1v-KZABWiax0",
    "user": {
        "id": 3,
        "email": "saifali1@gmail.com"
    }
}
```
## Deposit Money

|![Static Badge](https://img.shields.io/badge/Authenticated%20User-blue)|![Static Badge](https://img.shields.io/badge/Method-POST-GREEN)| ```/api/wallet/add/``` |
| :-------- | :-------- | :------------------------- |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `amount` | `decimal` | **Required.** amount |



**Example**
```http
{
    "amount":100
}
```
**Response**
```http
{
    "balance": 100.0
}

```

## Withdraw Money

|![Static Badge](https://img.shields.io/badge/Authenticated%20User-blue)|![Static Badge](https://img.shields.io/badge/Method-POST-GREEN)| ```/api/wallet/remove/``` |
| :-------- | :-------- | :------------------------- |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `amount` | `decimal` | **Required.** amount |



**Example**
```http
{
    "amount":100
}
```
**Response**
```http
{
    "balance": 0.0
}

```

## Get Transactions

|![Static Badge](https://img.shields.io/badge/Authenticated%20User-blue)|![Static Badge](https://img.shields.io/badge/Method-GET-blue)| ```/api/wallet/transactions/``` |
| :-------- | :-------- | :------------------------- |

**Response**
```http
[
 {
        "user": {
            "id": 3,
            "email": "saifali1@gmail.com"
        },
        "amount": "100.00",
        "transaction_type": "remove",
        "date": "2024-11-14T16:26:58.167318Z"
    },
    {
        "user": {
            "id": 3,
            "email": "saifali1@gmail.com"
        },
        "amount": "100.00",
        "transaction_type": "add",
        "date": "2024-11-14T16:24:35.047131Z"
    }
]
```


## Enable Wallet

|![Static Badge](https://img.shields.io/badge/Authenticated%20User-blue)|![Static Badge](https://img.shields.io/badge/Method-POST-GREEN)| ```/api/wallet/enable/``` |
| :-------- | :-------- | :------------------------- |

**Response**
```http
{
    "message": "Wallet Enabled Successfully"
}
```



## Check Balance

|![Static Badge](https://img.shields.io/badge/Authenticated%20User-blue)|![Static Badge](https://img.shields.io/badge/Method-GET-blue)| ```/api/wallet/balance/``` |
| :-------- | :-------- | :------------------------- |

**Response**
```http
{
    "balance": 0.0
}

```


![image](https://github.com/user-attachments/assets/d617ad2f-af58-499d-a55e-0f8f2ea7cdb2)

![image](https://github.com/user-attachments/assets/4e64667f-56da-48db-bad5-25b220df8c98)

![image](https://github.com/user-attachments/assets/605a2c68-787f-4817-9be7-2a93e2c0944c)
![image](https://github.com/user-attachments/assets/5be5b8af-36e5-44f0-9cb7-5fb8093e550e)
![image](https://github.com/user-attachments/assets/40180666-1194-4e15-9a71-e6eb46749d68)



