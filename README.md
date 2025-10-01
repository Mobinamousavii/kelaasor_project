# 📚 Kelaasor Backend Project

A **full-featured backend system** built with Django & Django REST Framework for managing bootcamps, advanced courses, tickets, and payments.  
This project was developed as part of the **Kelaasor Backend Bootcamp**.  

---

## 🚀 Features

### 🔑 Accounts
- **Custom User Model** with extended fields  
- Role-based access using a custom `Role` model instead of Django’s default groups  
- Roles: `student`, `support`, `teacher`, `financial`, `admin`  
- Authentication via **JWT** and **OTP**  

### 🎓 Bootcamps & Advanced Courses
- Designed with an **Abstract Base Model** to avoid code duplication  
- User registration requests with **approval workflow**  
- Capacity & status management (`registration_open`, `in_progress`, `completed`, etc.)  
- API for listing **My Bootcamps / My Courses**  
- Filtering, searching, and pagination for courses  

### 🎟️ Tickets
- Support system for users  
- Tickets can be **general** or linked to a bootcamp/advanced course  
- Each ticket supports multiple messages (conversation style) and file attachments  
- Support role can reply or close tickets  
- Email notification sent to support team when a new ticket is created  

### 💳 Payments
- **Invoice** model + **Payment** model  
- Partial payments supported (multiple payments for one invoice)  
- Offline payments (bank transfer with receipt & tracking code)  
- Online payments (future integration with payment gateway)  
- Payment approval workflow by **financial role**  

---

## 🛠️ Tech Stack
- **Python 3.11+**  
- **Django 5 + Django REST Framework**  
- **PostgreSQL**  
- **Celery + Redis** for async tasks (emails, SMS)  
- **JWT Authentication**  
- **Docker (optional)** for deployment  

---

## 📂 Project Structure

```bash
kelaasor_project/
│
├── accounts/         # User & role management
├── bootcamps/        # Bootcamps
├── advcourses/       # Advanced courses (abstract base model)
├── tickets/          # Ticketing system
├── payments/         # Invoices and payments
└── core/             # Core settings & configuration
```

---

## 📌 Design Highlights
- **Abstract Base Models** used to keep Bootcamp and Advanced Courses DRY.  
- **Nested Serializers** for returning related objects (e.g., user profile inside user, messages inside ticket).  
- Custom permission system via `HasRole` for role-based access control.  
- Clean architecture with separated apps for scalability.  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mobinamousavii/kelaasor_project.git
   ```
