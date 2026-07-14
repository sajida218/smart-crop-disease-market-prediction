# Smart Crop Disease Detection API Documentation

## Base URL

http://127.0.0.1:5000

---

## 1. Register User

### Endpoint

POST /register

### Request Body

```json
{
    "name": "Yash",
    "email": "yash@example.com",
    "password": "123456"
}
```

### Response

```json
{
    "success": true,
    "message": "User Registered Successfully"
}
```

---

## 2. Login User

### Endpoint

POST /login

### Request Body

```json
{
    "email": "yash@example.com",
    "password": "123456"
}
```

### Response

```json
{
    "success": true,
    "message": "Login Successful"
}
```

---

## 3. Get Users

### Endpoint

GET /users

### Response

```json
{
    "users": []
}
```

---

## 4. Upload Image

### Endpoint

POST /upload

### Body

form-data

Key: image (File)

### Response

```json
{
    "message": "Image uploaded successfully"
}
```

---

## 5. Predict Disease

### Endpoint

POST /predict

### Body

form-data

Key: image (File)

### Response

```json
{
    "success": true,
    "disease": "Healthy Leaf",
    "confidence": 95.27
}
```

---

## 6. Prediction History

### Endpoint

GET /history

### Response

```json
{
    "history": []
}
```