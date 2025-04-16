from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
import base64
import json
from datetime import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

router = APIRouter()

PUBLIC_KEY_PATH = "scripts/keys/public_key.pem"


class LicenseCheckRequest(BaseModel):
    license_key: str


@router.post("/validate-license")
async def validate_license(req: LicenseCheckRequest):
    try:
        with open(PUBLIC_KEY_PATH, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        # Decode and parse license key
        raw = base64.b64decode(req.license_key.encode())
        license_package = json.loads(raw)
        payload = license_package["payload"]
        signature = base64.b64decode(license_package["signature"].encode())

        # Verify signature
        message = json.dumps(payload, sort_keys=True).encode()
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        # Check expiry
        if datetime.utcnow() > datetime.fromisoformat(payload["expires"]):
            raise HTTPException(status_code=401, detail="❌ License expired")

        return {
            "valid": True,
            "client_id": payload["client_id"],
            "plan": payload["plan"],
            "expires": payload["expires"]
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"❌ Invalid license: {str(e)}")
