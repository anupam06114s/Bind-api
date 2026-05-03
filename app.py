# app.py
# Simple Bind Info API (Flask)
# Install: pip install flask requests gunicorn

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Bind Info API Running"
    })

@app.route("/bindinfo", methods=["GET"])
def bindinfo():
    access_token = request.args.get("token")

    if not access_token:
        return jsonify({
            "status": False,
            "error": "token parameter required"
        }), 400

    url = "https://100067.connect.garena.com/game/account_security/bind:get_bind_info"

    params = {
        "app_id": "100067",
        "access_token": access_token
    }

    headers = {
        "User-Agent": "GarenaMSDK/4.0.30",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        data = response.json()

        return jsonify({
            "status": True,
            "garena_response": data
        })

    except Exception as e:
        return jsonify({
            "status": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)