import os
from dotenv import load_dotenv
from pathlib import Path

# Load from .env file if present
load_dotenv(dotenv_path=Path(".env"))

# === Application Config === #
PROJECT_NAME = os.getenv("PROJECT_NAME", "RedCorps Sentinel")
ENV = os.getenv("ENV", "development")
DEBUG = ENV != "production"

# === API Keys === #
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
JWT_SECRET = os.getenv("JWT_SECRET", "supersecuretoken")

# === Ports & URLs === #
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# === Scan Settings === #
DEFAULT_PORTS = os.getenv("DEFAULT_PORTS", "1-1000")
MAX_SCAN_DURATION = int(os.getenv("MAX_SCAN_DURATION", 60))  # in seconds
DEFAULT_FRAMEWORK = os.getenv("DEFAULT_FRAMEWORK", "NIST CSF 2.0")

# === License System === #
LICENSE_VALIDATION_ENABLED = os.getenv("LICENSE_VALIDATION", "true").lower() == "true"
