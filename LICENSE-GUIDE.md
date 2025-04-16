# 🛡️ License Activation & Selling Guide

This document explains how to distribute, activate, and enforce licenses for RedCorps Sentinel — the AI-powered cybersecurity toolkit.

---

## 🔐 1. How Licensing Works

RedCorps Sentinel uses RSA-signed offline licenses. These are validated by:
- ✅ CLI tool (`cli.py`)
- ✅ Backend API (`/api/user/validate-license`)

Each license contains:
- `client_id`
- `plan` (Basic, Pro, Enterprise)
- `issued` + `expires`
- Digital signature

---

## 🧰 2. Generate a License

Use the built-in license generator:

```bash
python3 scripts/license_generator.py --generate-key           # Once (private/public)
python3 scripts/license_generator.py --create acme-123 > acme.lic
```

Store or send `acme.lic` to the client.

---

## 💻 3. Activate License (Client-Side)

### CLI Activation:
```bash
cp acme.lic ~/.ai-sec-cli/license.lic
python cli/cli.py --scan example.com
```

### API Validation:
The backend checks the license via public key before running any scan/report endpoint.

---

## 🛒 4. Selling Licenses (Gumroad / Reseller / SaaS)

### ✅ Option 1: Sell Pre-Generated Licenses
- Use Gumroad or LemonSqueezy
- Upload each `.lic` file as a digital product
- Send buyer instructions to place it in `~/.ai-sec-cli/license.lic`

### ✅ Option 2: Generate on Purchase (Zapier API)
- Auto-trigger `scripts/license_generator.py --create` with unique ID
- Email the `.lic` to client

### ✅ Option 3: Enterprise B2B
- Generate licenses manually per customer
- Track license IDs with expiry in spreadsheet or CRM

---

## 🧾 5. License Plans (Example)

| Plan       | Expiry    | Features Included           |
|------------|-----------|-----------------------------|
| Free       | 14 days   | Limited scan, PDF           |
| Pro        | 1 year    | Full report, offline CLI    |
| Enterprise | Custom    | Full access + support       |

---

## 🔒 6. Prevent Sharing / Abuse

- Licenses expire via internal timestamp
- Signature prevents tampering
- Offline-only = no callback, but CLI/API both enforce locally
- Optional: add client domain/IP in payload

---

## 📤 7. Distribute

Send `.lic` file by:
- Email
- Download link (private Gumroad product)
- CLI auto-installer script

---

## 📬 Need Help?
Contact licensing@redcorps.io for volume sales, OEM bundling, or private label deals.
