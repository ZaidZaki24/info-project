# PQCrypto Web Demo

A web-based demonstration of Post-Quantum Cryptography using Kyber key encapsulation mechanism with AES encryption, built with Flask.

## 📋 Project Overview

This project provides a user-friendly web interface to experiment with post-quantum cryptographic operations using the Kyber algorithm, which is part of the NIST Post-Quantum Cryptography standardization process.

## ✨ Features

- **Key Generation**: Generate Kyber post-quantum key pairs (public and private keys)
- **Message Encryption**: Encrypt messages using Kyber KEM with AES symmetric encryption
- **Message Decryption**: Decrypt ciphertexts using the corresponding private key
- **Web Interface**: Clean, user-friendly web interface for easy interaction
- **Security**: Enhanced security with Flask-Talisman for HTTPS headers

## 🛠️ Technologies Used

- **Backend**: Flask web framework
- **Cryptography**: `pqcrypto_helpers.kyber_aes` for post-quantum operations
- **Security**: Flask-Talisman for security headers
- **Frontend**: HTML, CSS with responsive design
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Step-by-Step Setup

**Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>

Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install flask flask-talisman python-dotenv pqcrypto_helpers


Set up environment variables

Create a .env file in the project root:
SECRET_KEY=secretkey


Running the Application
Development Mode

python app.py




The application will be available at http://localhost:5000

Production Deployment
For production deployment, consider using:

Gunicorn or uWSGI as WSGI server

Nginx as reverse proxy

Proper SSL certificate


pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app



Project Structure


project/
├── app.py              # Main Flask application
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
├── templates/
│   └── index.html    # Main web interface
└── static/
    └── style.css     # Styling



   
