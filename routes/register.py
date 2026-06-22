from flask import Blueprint, request
import sqlite3

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    conn = sqlite3.connect('database/crop.db')
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,(name,email,password))

        conn.commit()

        return {"message":"User Registered Successfully"}

    except:
        return {"error":"Email already exists"}

    finally:
        conn.close()