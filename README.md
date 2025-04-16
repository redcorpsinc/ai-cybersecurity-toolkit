# 🔐 RedCorps Sentinel  
**AI-Powered Offline Cybersecurity Toolkit**

Turn your laptop into a full-stack vulnerability scanner, GPT-powered risk assessor, and compliance reporting engine — all offline, self-hosted, and monetized with license control.

---

## 🚀 Features

- ✅ FastAPI-based backend API engine  
- ✅ Next.js frontend dashboard (Dockerized)  
- ✅ GPT-driven risk analysis (Supports NIST, CIS, PCI, ISO)  
- ✅ Recon engine: Nmap + DNS scan + Tech stack fingerprinting  
- ✅ AI-powered PDF + HTML report generator  
- ✅ Fully offline CLI tool with license key validation  
- ✅ Self-hosted MongoDB support for report storage  
- ✅ RSA-based license activation and verification system  

---

## 📦 Installation (Docker Compose)

```bash
# 1. Clone the repository
git clone https://github.com/your-org/ai-cybersecurity-toolkit.git
cd ai-cybersecurity-toolkit

# 2. Create and configure environment file
cp .env.template .env
# Edit .env to add your OPENAI_API_KEY and JWT_SECRET

# 3. Build and launch containers
docker-compose build
docker-compose up -d
```

### 🔗 Access the Toolkit
- **Frontend UI:** `http://localhost:3000`  
- **Backend API Docs:** `http://localhost:8000/docs`  

---

## 🧠 Usage (Web Interface)

1. Go to `/scan` on the dashboard  
2. Enter a domain or IP address  
3. Select compliance framework (NIST, PCI, CIS, ISO)  
4. View:
   - GPT-generated risk score  
   - AI summary report (PDF/HTML)  
   - Mapped security controls  
5. Check `/reports` to view/download archived results  

---

## 💻 Usage (Offline CLI)

```bash
# 1. Generate & install a license key
python scripts/license_generator.py --create acme-123 > key.lic
cp key.lic ~/.ai-sec-cli/license.lic

# 2. Run an offline scan
python cli/cli.py --scan example.com
```

✅ CLI runs **fully offline** – includes local GPT prompts, scan engine, and report generation.

---

## 🔑 Licensing System

- Licenses are RSA-signed using `scripts/license_generator.py`  
- CLI and backend validate keys offline  
- Ready for monetization via:
  - SaaS subscriptions  
  - Gumroad/gated downloads  
  - Reseller partner tiers  

---

## 🧾 Report Output

- **Storage:** `backend/reports/output/`  
- **Formats:** PDF & HTML  
- **Details Included:**
  - Target Info
  - GPT Risk Score
  - Framework-mapped security controls
  - Compliance footer

---

## 📁 Folder Structure

```
ai-cybersecurity-toolkit/
├── backend/        # FastAPI + GPT analysis engine
├── frontend/       # Next.js dashboard UI
├── cli/            # Offline CLI client
├── reports/        # PDF & HTML templates
├── docker/         # Dockerfiles for services
├── scripts/        # License generation tools
├── .env.template   # Environment variables template
├── docker-compose.yml
```

---

## 💸 Use Cases

- ✅ Law firms without in-house IT  
- ✅ Freelancers delivering cybersecurity audits  
- ✅ Startups needing lightweight NIST/CIS compliance  
- ✅ IT professionals preferring **local-first** tooling  

---

## 📃 License

**MIT License** (for internal use)  
🔒 For **commercial use**, contact: [you@yourdomain.com](mailto:you@yourdomain.com)

---

## 🤝 Support / Contribute

We welcome your pull requests, ideas, and contributions.  
📧 **Business, demo, or deployment inquiries:** [you@yourdomain.com](mailto:you@yourdomain.com)

---

Built with ❤️ by **RedCorps Inc.**
