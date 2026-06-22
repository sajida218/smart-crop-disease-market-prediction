from flask import Blueprint, request
from database.database import get_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data:
        return {"error": "No data provided"}, 400

    email = data.get("email")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            "success": True,
            "message": "Login Successful",
            "user_id": user[0],
            "name": user[1],
            "email": user[2]
        }

    return {
        "success": False,
        "message": "Invalid Email or Password"
    }, 401
@auth_bp.route('/users', methods=['GET'])
def get_users():

    conn = sqlite3.connect('database/crop.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id,name,email FROM users")

    users = cursor.fetchall()

    conn.close()

    return {"users": users}