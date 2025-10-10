# PQCrypto Web Demo

A web-based demonstration of Post-Quantum Cryptography using Kyber key encapsulation mechanism with AES encryption, built with Flask.

## Project Overview

This project provides a user-friendly web interface to experiment with post-quantum cryptographic operations using the Kyber algorithm, which is part of the NIST Post-Quantum Cryptography standardization process.

## Features

- **Key Generation**: Generate Kyber post-quantum key pairs (public and private keys)
- **Message Encryption**: Encrypt messages using Kyber KEM with AES symmetric encryption
- **Message Decryption**: Decrypt ciphertexts using the corresponding private key
- **Web Interface**: Clean, user-friendly web interface for easy interaction
- **Security**: Enhanced security with Flask-Talisman for HTTPS headers

## Technologies Used

- **Backend**: Flask web framework
- **Cryptography**: pqcrypto_helpers.kyber_aes for post-quantum operations
- **Security**: Flask-Talisman for security headers
- **Frontend**: HTML, CSS with responsive design
- **Environment Management**: python-dotenv

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

git clone <repository-url>
cd <project-directory>

2. Create a virtual environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies

pip install flask flask-talisman python-dotenv pqcrypto_helpers



4. Set up environment variables
Create a .env file in the project root:

SECRET_KEY=secretkey


## Running the Application

### Development Mode

python app.py




The application will be available at http://localhost:5000

### Production Deployment
For production deployment, consider using:
- Gunicorn or uWSGI as WSGI server
- Nginx as reverse proxy
- Proper SSL certificate

Example with Gunicorn:



pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app






## API Endpoints

### POST /generate_keys
Generates a new Kyber key pair.

Response:

{
"status": "success",
"public_key": "base64_encoded_public_key",
"private_key": "base64_encoded_private_key"
}




## Security Notes

- This is a demonstration application and should not be used for production security
- The application uses Kyber-512 by default (via pqcrypto_helpers)
- For production use, consider using the latest standardized versions (ML-KEM)
- Always use HTTPS in production environments
- Keep private keys secure and never expose them unnecessarily

## About Post-Quantum Cryptography

Post-quantum cryptography refers to cryptographic algorithms that are secure against attacks by quantum computers. Kyber is a key encapsulation mechanism (KEM) that has been selected by NIST for standardization.

### Kyber Features:
- **Lattice-based**: Security based on the hardness of lattice problems
- **Efficient**: Relatively fast compared to other post-quantum schemes
- **Standardized**: Part of NIST's Post-Quantum Cryptography standardization

## Troubleshooting

### Common Issues
1. **ModuleNotFoundError: No module named 'pqcrypto_helpers'**





2. **Import errors** - Ensure you're using the correct Python environment and all dependencies are installed

3. **Connection refused** - Check if the port (5000) is available and the Flask app is running

## License

This project is provided for educational and demonstration purposes. Please check the licenses of the underlying cryptographic libraries for production use.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Disclaimer

This software is provided for educational and demonstration purposes only. Use in production environments should be done with careful consideration of security requirements and proper cryptographic implementation practices.





### Step-by-Step Setup
1. Clone the repository
