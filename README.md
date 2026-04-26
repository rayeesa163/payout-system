# 💰 Payout System (Django + REST API)

A full-stack payout management system built using **Django REST Framework** with a simple frontend UI and deployed on Render.

---

## 🚀 Live Demo

👉 https://payout-system-5.onrender.com/

---

## 📌 Features

* ✅ Create Payout (merchant, amount, bank)
* 🔍 View Payout by ID
* ⚙️ Process Payout (pending → processing → success)
* 📊 Dashboard to view all payouts
* 🔁 Simulated payout lifecycle
* 🌐 Deployed on cloud (Render)

---

## 🧱 Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** HTML, CSS, JavaScript (Fetch API)
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **Deployment:** Render
* **Server:** Gunicorn

---

## ⚙️ API Endpoints

| Method | Endpoint                        | Description      |
| ------ | ------------------------------- | ---------------- |
| POST   | `/api/v1/payouts/`              | Create payout    |
| GET    | `/api/v1/payouts/<id>/`         | View payout      |
| POST   | `/api/v1/payouts/<id>/process/` | Process payout   |
| GET    | `/api/v1/payouts/all/`          | List all payouts |

---

## 🔄 Payout Lifecycle

```text
pending → processing → success
```

---

## 🛠️ Local Setup

### 1. Clone repo

```bash
git clone https://github.com/rayeesa163/payout-system.git
cd payout-system
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Run server

```bash
python manage.py runserver
```

---

## 🌍 Deployment (Render)

* Hosted using Render Web Service
* Gunicorn used as WSGI server
* Environment variable: `PYTHON_VERSION=3.11`

---

## 💡 Future Improvements

* 🔐 Authentication (login/signup)
* 💳 Payment gateway integration
* 📉 Failure & retry logic
* 📊 Advanced dashboard filters
* 🗄️ PostgreSQL database
* 📦 Docker deployment

---

## 👩‍💻 Author

**Rayeesa Tabusum**
🔗 https://github.com/rayeesa163

---

## ⭐ Project Highlights

* Built full-stack system with API + UI
* Implemented real-world payout lifecycle
* Handled CSRF, deployment, and production issues
* Deployed live application

---
