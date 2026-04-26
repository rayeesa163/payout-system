# 📄 Payout System – Explainer

## 🎯 Objective

The goal of this project is to build a simple payout processing system that simulates how payment systems handle transactions and status updates.

---

## 🧱 System Overview

This system allows:

* Creating a payout request
* Fetching payout details
* Processing payouts through lifecycle stages
* Viewing all payouts via a dashboard

---

## ⚙️ Architecture

* **Backend:** Django + Django REST Framework
* **Frontend:** HTML + JavaScript (Fetch API)
* **Database:** SQLite
* **Deployment:** Render (Gunicorn)

---

## 🔄 Payout Lifecycle

Each payout goes through the following states:

```text
pending → processing → success
```

### Flow:

1. User creates payout → status = `pending`
2. User triggers processing → status = `processing`
3. System simulates delay → status = `success`

---

## 📡 API Design

### 1. Create Payout

* `POST /api/v1/payouts/`
* Input: merchant, amount, bank account
* Output: payout ID + status

---

### 2. Get Payout Details

* `GET /api/v1/payouts/<id>/`
* Returns payout information

---

### 3. Process Payout

* `POST /api/v1/payouts/<id>/process/`
* Updates payout status through lifecycle

---

### 4. List All Payouts

* `GET /api/v1/payouts/all/`
* Used for dashboard display

---

## 🖥️ Frontend Logic

* Uses JavaScript `fetch()` to call APIs
* Auto-fills payout ID after creation
* Displays results dynamically
* Includes dashboard table for all payouts

---

## 🚧 Challenges Faced

* CSRF token errors while connecting frontend to backend
* Handling API response parsing issues
* Deployment issues (Gunicorn, Django version compatibility)
* Configuring ALLOWED_HOSTS for production

---

## 🧠 Key Learnings

* How REST APIs work in Django
* Handling real-world deployment issues
* Managing application state transitions
* Debugging frontend-backend integration

---

## 🚀 Future Improvements

* Add authentication system
* Integrate real payment gateway
* Add failure & retry logic
* Use PostgreSQL for production database
* Improve UI/UX with modern frameworks

---

## ✅ Conclusion

This project demonstrates a complete flow from backend API development to frontend integration and deployment, simulating a real-world payout processing system.
