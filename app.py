from flask import Flask

from routes.auth import auth_bp
from routes.upload import upload_bp
from routes.prediction import prediction_bp
from routes.register import register_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(register_bp)

@app.route('/')
def home():
    return {"message": "Smart Crop Backend Running"}


@app.route('/health')
def health():
    return {
        "status": "success",
        "server": "running"
    }


if __name__ == '__main__':
    app.run(debug=True)