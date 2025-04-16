# 🔐 RedCorps Sentinel

**AI-Powered Offline Cybersecurity Toolkit**

Turn your laptop into a full-stack vulnerability scanner, GPT-powered risk assessor, and compliance report engine — all offline, self-hosted, and monetized with license control.

---

## 🚀 Features

- ✅ **FastAPI-based API engine**
- ✅ **Next.js dashboard UI (Dockerized)**
- ✅ **OpenAI GPT risk analysis (NIST, CIS, PCI, ISO)**
- ✅ **Recon: Nmap + DNS + Tech stack fingerprints**
- ✅ **AI-powered PDF report generator**
- ✅ **Offline CLI tool with license key activation**
- ✅ **Self-hosted MongoDB (optional log store)**
- ✅ **License system: RSA-signed, CLI-validatable**

---

## 📦 Installation (Docker Compose)

### 1. Clone This Repo
```bash
git clone https://github.com/your-org/ai-cybersecurity-toolkit.git
cd ai-cybersecurity-toolkit
```

### 2. Set Up Environment
```bash
cp .env.template .env
# Edit .env with your own OPENAI_API_KEY and JWT_SECRET
```

### 3. Build and Launch
```bash
docker-compose build
docker-compose up -d
```

### 4. Access the Toolkit
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/docs

---

## 🧠 Usage (Web Interface)

1. Visit `/scan` in your browser
2. Enter domain or IP
3. Choose compliance framework (NIST, PCI, CIS, ISO)
4. Get AI-driven risk score, PDF report, and mapped controls
5. View or download past reports via `/reports`

---

## 💻 Usage (Offline CLI)

### 1. Activate License
```bash
python scripts/license_generator.py --create acme-123 > key.lic
cp key.lic ~/.ai-sec-cli/license.lic
```

### 2. Run Scan from CLI
```bash
python cli/cli.py --scan example.com
```

> ✅ CLI works fully offline — AI prompts, scan logic, and PDF all local.

---

## 🔑 Licensing System

- Licenses are RSA signed via `scripts/license_generator.py`
- CLI and API verify offline
- You can embed this into Gumroad, SaaS subscriptions, or reseller tiers

---

## 🧾 Report Output

- Stored at: `backend/reports/output/`
- Formats: PDF + HTML
- Includes: Target, GPT risk score, mapped controls, compliance footer

---

## 📁 Folder Structure
```
ai-cybersecurity-toolkit/
├── backend/ (FastAPI + AI Engine)
├── frontend/ (Next.js UI)
├── cli/ (Offline client)
├── reports/ (PDF Templates)
├── docker/ (Dockerfiles)
├── scripts/ (License generator)
├── .env.template
├── docker-compose.yml
```

---

## 💸 Use Cases

- ✅ Law firms without IT staff
- ✅ Freelancers offering security audits
- ✅ Startups needing baseline NIST/CIS compliance
- ✅ IT pros who want local-first security tooling

---

## 📃 License

MIT (for internal use). Contact [you@yourdomain.com] for commercial licensing.

---

## 🤝 Support / Contribute

PRs welcome. For commercial inquiries, demos, or deployment:
📧 you@yourdomain.com

---

Built with ❤️ by RedCorps Inc.
