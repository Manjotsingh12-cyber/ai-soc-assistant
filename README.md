# AI SOC Assistant – SOC Automation Project

🔗 **YouTube Demo:** https://youtu.be/S5H78cE_JT0?si=Rf1qEO3FGMXTEN56

This project demonstrates an end-to-end SOC automation workflow using Splunk alerts, Python processing, and MITRE ATT&CK mapping.

It is designed to simulate a brute-force attack scenario in a lab environment and automatically analyze alerts.

---

## 📌 Architecture

- Splunk forwards detection alerts to the webhook
- Python app consumes alerts
- Alert is analyzed for severity
- Attack is mapped to MITRE ATT&CK technique
- Incident report is generated automatically

---

## 📌 Features

✔ Detect brute-force pattern  
✔ Automated webhook processing  
✔ Simple AI analysis logic  
✔ MITRE ATT&CK mapping  
✔ JSON incident report generator  
✔ Ready for extension with real AI API

---

## 📌 Tech Stack

- Splunk
- Python (Flask)
- MITRE ATT&CK
- JSON report format

---

## 📌 How to Run

1. Install required packages:
   ```bash
   pip install -r requirements.txt
