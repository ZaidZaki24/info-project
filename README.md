# Post-Quantum Cryptography Flask Demo

A tiny web app that illustrates **Kyber-512 key encapsulation** (post-quantum secure) combined with **AES-256-GCM** for symmetric encryption.

---

## 1. Quick-start (local)

```bash
git clone https://github.com/YOUR-ORG/pqc-flask-demo.git
cd pqc-flask-demo

python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env                 # and put a strong SECRET_KEY

python app.py                        # visit http://127.0.0.1:5000
