from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes import scan, report, user
import uvicorn
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI init
app = FastAPI(
    title="AI Cybersecurity Toolkit API",
    description="""
RedCorps Sentinel is an AI-powered cybersecurity risk auditing toolkit.
Use this API to:
- Submit domains or IPs for automated recon
- Generate PDF audit reports
- Align output with NIST, CIS, PCI, or ISO frameworks
""",
    version="1.0.0",
    contact={
        "name": "RedCorps Security",
        "url": "https://redcorps.io",
        "email": "security@redcorps.io"
    },
    license_info={
        "name": "Commercial License",
        "url": "https://redcorps.io/license"
    }
)

# CORS setup
origins = ["*"]  # In production, restrict to your domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(scan.router, prefix="/api/scan", tags=["Scan"])
app.include_router(report.router, prefix="/api/report", tags=["Report"])
app.include_router(user.router, prefix="/api/user", tags=["User"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to AI Cybersecurity Toolkit Backend"}

# Server startup
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
