# Public Health Emotional and Stance Monitor (PHES-Web)
### Master's Software Project — Phase 2 Blueprint Prototype

This repository contains the functional backend architecture and data-routing infrastructure for **PHES-Web**, as outlined in the Phase 2 system development report. 

The prototype establishes a modular RESTful API layer (Flask), a mock relational database simulation layer to aggregate sentiment vectors, and an automated server-side alert threshold verification system.

---

## 📂 Project Architecture

```text
Ghatge-Sakshi_9210062_PHES/
│
├── backend/                  # Application Logic and Core Server Layer
│   ├── app.py                # Main REST API Endpoints & Alert Threshold Engine
│   ├── database.py           # Mock Relational Database Operations & Analytics
│   └── requirements.txt      # System Dependency Manifest
│
└── README.md                 # Deployment & System Documentation