import base64
import json
import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from datetime import datetime, timedelta

# Path to store keys
KEY_DIR = "scripts/keys"
os.makedirs(KEY_DIR, exist_ok=True)

PRIVATE_KEY_FILE = os.path.join(KEY_DIR, "private_key.pem")
PUBLIC_KEY_FILE = os.path.join(KEY_DIR, "public_key.pem")


def generate_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("✅ Key pair generated.")


def create_license(client_id: str, plan: str = "Pro", days_valid: int = 365) -> str:
    with open(PRIVATE_KEY_FILE, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    payload = {
        "client_id": client_id,
        "plan": plan,
        "issued": datetime.utcnow().isoformat(),
        "expires": (datetime.utcnow() + timedelta(days=days_valid)).isoformat()
    }

    # Sign license
    message = json.dumps(payload, sort_keys=True).encode()
    signature = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    # Encode license
    license_package = {
        "payload": payload,
        "signature": base64.b64encode(signature).decode()
    }

    return base64.b64encode(json.dumps(license_package).encode()).decode()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate-key", action="store_true")
    parser.add_argument("--create", metavar="CLIENT_ID", help="Create license for client ID")
    args = parser.parse_args()

    if args.generate_key:
        generate_keypair()
    elif args.create:
        license_key = create_license(args.create)
        print(f"🔑 License Key:\n{license_key}")
