# ⚽ Spartacus Bubble Soccer: AI Automation Ecosystem

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=openai&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white)

> **Architected by Sujon Ahmed (Backend Engineer)**  
> A high-performance, automated operational brain built to manage 238+ locations across the UK.

---

## 🎯 Project Overview
This project transforms a traditional booking process into a fully autonomous **AI-Driven Ecosystem**. It orchestrates seamless communication between web inquiries, phone calls, real-time inventory systems, and operational dashboards.

### 🏗️ The Core Architecture
The system is divided into three specialized engines:
1.  **Booking Engine (`bookinge`)**: Handles slots, inventory, and venue coordination.
2.  **Support Intelligence (`support`)**: Processes customer interactions via OpenAI.
3.  **Analytics Hub (`Dashboards`)**: Real-time business intelligence and data sync.

---

## 🚀 Key Intelligent Features

### 🧠 1. Smart Inventory Engine (Rezgo Integration)
*   **Fuzzy Location Mapping:** Developed a custom matching algorithm to map 238+ city names to unique Rezgo UIDs instantly.
*   **Real-time Availability:** Checks live slots and creates bookings via XML Commit API.
*   **Intelligent Alternatives:** If a requested time is full, the system automatically suggests the next available unique slots for that specific location.

### 📞 2. Autonomous Voice Assistant (Vapi + Twilio)
*   **Hands-free Booking:** A dedicated bridge allowing the Voice AI to talk to our Django backend. 
*   **Instant Confirmation:** AI can check availability and block inventory during a phone call without human intervention.

### ✉️ 3. AI Email Support (GPT-4 + SendGrid)
*   **Context-Aware Support:** Integrated OpenAI GPT-4 to read incoming customer replies.
*   **Dynamic Knowledge Base:** The AI answers based on real-time database FAQ rules, ensuring 100% accuracy.
*   **SMTP Failover:** Branded email delivery via SendGrid API and high-availability SMTP.

### 📊 4. Operational Command Center (Airtable Sync)
*   **Relational Multi-Table Sync:** Automatically synchronizes data across 5 inter-linked Airtable tables:
    *   `Leads`: Captures initial inquiries.
    *   `Bookings`: Final confirmed reservations.
    *   `Venues`: Directory of field owners.
    *   `Venue Requests`: Automated outreach logs.
    *   `Shifts`: Operational staff scheduling.

---

## 🛠️ Technical Stack
*   **Backend:** Python 3.12, Django 5.x, Django Rest Framework (DRF)
*   **AI Logic:** OpenAI GPT-4, Function Calling, Prompt Engineering
*   **Voice/Tel:** Twilio, Vapi (Voice-to-JSON Bridge)
*   **Database:** PostgreSQL (Core), Airtable (Client Interface)
*   **Integration:** SendGrid API, Rezgo XML/JSON API, Ngrok

---

## 📡 API Documentation (Swagger)
The entire system is documented using OpenAPI standards. 
- **Interactive Docs:** `http://127.0.0.1:8000/api/docs/`
- **Stats Overview:** `GET /api/dashboards/stats/` - Real-time business health check.

---

## ⚙️ Installation & Live Setup

### 1. Environment Configuration
Create a `.env` file in the root directory:
```env
# Credentials
REZGO_CID=36413
REZGO_API_KEY=your_key
REZGO_DOMAIN=spartacusbubble
AIRTABLE_API_KEY=your_token
AIRTABLE_BASE_ID=your_base_id
OPENAI_API_KEY=your_gpt_key
SENDGRID_API_KEY=your_key
EMAIL_HOST_PASSWORD=your_smtp_app_password



# Clone and install
git clone https://github.com/yourusername/Josph.git
pip install -r requirements.txt

# Run Database Migrations
python manage.py migrate

# Synchronize Inventory from Rezgo
python manage.py shell
>>> from bookinge.utils import auto_sync_all_rezgo_locations
>>> auto_sync_all_rezgo_locations()

# Launch System
python manage.py runserver




📜 Summary of Logic Workflows
Scenario	Action Taken by System
User sends Inquiry	Checks Rezgo -> Logs to Airtable Leads -> Sends Email Link.
Requested Slot is Full	System finds all other available times -> Emails a list of alternatives.
Voice Call Received	AI understands intent -> Blocks slot in Rezgo -> Confirms via Email.
Customer Replies Email	OpenAI parses question -> Searches DB context -> Replies intelligently.
