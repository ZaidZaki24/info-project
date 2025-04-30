import os
from flask import Flask, render_template, request, jsonify
from flask_talisman import Talisman
from dotenv import load_dotenv

from pqcrypto_helpers.kyber_aes import (
    generate_keypair,
    encrypt_message,
    decrypt_message,
)

# Load .env
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")
Talisman(app, content_security_policy=None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_keys", methods=["POST"])
def generate_keys():
    pub, priv = generate_keypair()
    return jsonify(status="success", public_key=pub, private_key=priv)


@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json(force=True)
    message    = data.get("message", "").encode()
    public_key = data.get("public_key", "")

    if not public_key:
        return jsonify(status="error", error="Missing public key"), 400
    if not message:
        return jsonify(status="error", error="Missing plaintext"), 400

    try:
        ct = encrypt_message(public_key, message)
        return jsonify(status="success", ciphertext=ct)
    except Exception as exc:
        app.logger.exception("Encryption failed")
        return jsonify(status="error", error=str(exc)), 400


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json(force=True)
    ciphertext  = data.get("ciphertext", "")
    private_key = data.get("private_key", "")

    if not ciphertext:
        return jsonify(status="error", error="Missing ciphertext"), 400
    if not private_key:
        return jsonify(status="error", error="Missing private key"), 400

    try:
        pt = decrypt_message(private_key, ciphertext).decode()
        return jsonify(status="success", plaintext=pt)
    except Exception as exc:
        app.logger.exception("Decryption failed")
        return jsonify(status="error", error=str(exc)), 400


if __name__ == "__main__":
    app.run(debug=True)
