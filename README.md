# PHES-Web — Public Health Emotional and Stance Monitor

A web-based Early Warning System for public health communication teams.
Monitors shifts in public sentiment during health crises through an
interactive dashboard, category filtering, and automated threshold alerts.

**Course:** Project: Software Engineering (DLMCSPSE01)
**Student:** Sakshi Ghatge — Student ID: 9210062
**GitHub:** https://github.com/SakshiGhatge1999/PHES-Web-Monitor

---

## Live Application

> Cloud deployment URL: [add your deployed URL here]

---

## Project Structure

```
PHES-Web/
├── backend/
│   ├── app.py              # Flask API router and alert engine
│   ├── database.py         # Data engine module (mock dataset)
│   ├── requirements.txt    # Python dependencies (version-pinned)
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── components/
│   │       ├── Dashboard.js
│   │       ├── FilterPanel.js
│   │       ├── ChartPanel.js
│   │       └── AlertBanner.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Option 1 — Run with Docker Compose (recommended)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/SakshiGhatge1999/PHES-Web-Monitor.git
cd PHES-Web-Monitor

# 2. Set up environment variables
cp .env.example .env

# 3. Start all services
docker compose up
```

The dashboard is available at **http://localhost:3000**
The API is available at **http://localhost:5000/api/dashboard**

To stop:
```bash
docker compose down
```

---

## Option 2 — Run manually (without Docker)

### Prerequisites
- Python 3.11+
- Node.js 18+

### Backend

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Start the Flask API
python app.py
```

Backend runs at: **http://localhost:5000**

### Frontend

Open a second terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

Frontend runs at: **http://localhost:3000**

---

## API Reference

### GET /api/dashboard

Returns aggregated public health sentiment metrics.

**Optional query parameter:**
- `?emotion=<category>` — filter by emotional category (case-insensitive)

**Available categories:** Anxiety, Confusion, Distrust, Fear, Acceptance

**Example requests:**
```bash
# All categories
curl http://localhost:5000/api/dashboard

# Single category
curl http://localhost:5000/api/dashboard?emotion=Confusion

# Case-insensitive — all three return the same result
curl http://localhost:5000/api/dashboard?emotion=confusion
curl http://localhost:5000/api/dashboard?emotion=CONFUSION
curl http://localhost:5000/api/dashboard?emotion=Confusion
```

**Response schema:**
```json
{
  "status": "success",
  "data": [
    {
      "date": "2026-05-05",
      "category": "Confusion",
      "count": 210,
      "percentage": 52.5
    }
  ],
  "alerts_triggered": [
    {
      "alert_id": "WARN_SPIKE",
      "category": "Confusion",
      "date": "2026-05-05",
      "value": 52.5,
      "message": "Alert: High volume of public Confusion detected on 2026-05-05 (52.5%)."
    }
  ]
}
```

**Alert rule:** Any record with `percentage >= 50.0` triggers an alert.
The threshold is defined as `ALERT_THRESHOLD = 50.0` in `backend/app.py`.

---

## Technology Stack

| Layer | Technology | Version |
|---|---|---|
| Frontend | React.js | 18.2.0 |
| Visualization | Chart.js / react-chartjs-2 | 4.4.0 |
| Backend | Flask | 2.3.2 |
| CORS | Flask-CORS | 4.0.0 |
| Data | pandas | 2.0.3 |
| Deployment | Docker Compose | 3.8 |

---

## Non-Functional Requirements Verification

**NFR1 — Response time under 3 seconds:**
```bash
for i in $(seq 10); do
  curl -o /dev/null -s -w "%{time_total}\n" http://localhost:5000/api/dashboard
done
```

**NFR2 — No data manipulation in app.py:**
```bash
grep -n "pd\." backend/app.py
# Expected output: no results
```

**NFR3 — PEP 8 compliance:**
```bash
pip install flake8
flake8 backend/ --max-line-length=79
# Expected output: no warnings
```
