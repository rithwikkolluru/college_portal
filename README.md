#  College Portal Web Application

A full-stack web application built using Django for managing college faculty, courses, placements, and student authentication.

---

##  Project Overview

The College Portal is designed to provide:

- Student Registration & Login
- Secure Authentication System
- Admin-controlled Placement Records
- Faculty & Course Information Display
- Professional UI using Bootstrap 5
- Scalable structure for future AI integrations

---

##  Tech Stack

### Backend
- Python 3
- Django
- SQLite3 (Development Database)

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Version Control
- Git
- GitHub

---

##  Project Structure

```
college_portal/
│
├── college_portal/
│   ├── settings.py
│   ├── urls.py
│
├── main/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── faculty.html
│   ├── courses.html
│   ├── placements.html
│   ├── contact.html
│   ├── signup.html
│   ├── login.html
│   └── dashboard.html
│
└── manage.py

```

---

##  Features Implemented (Phase 1)

-  Student Signup
-  Student Login
-  Logout Functionality
-  Protected Dashboard (Login Required)
-  Admin Panel Management
-  Responsive UI

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/college_portal.git
cd college_portal
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

(Mac/Linux)
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Open:
```
http://127.0.0.1:8000/
```

---

##  Future Enhancements (Phase 2 & Beyond)

-  AI-powered Chatbot for Query Resolution
-  Placement Analytics Dashboard
-  Face Recognition Authentication
-  Course Recommendation System
-  Deployment on Cloud Server

---

##  Screenshots

(Add screenshots of your login, dashboard, and admin panel here)

---

##  Author

**Rithwik Kolluru**
- GitHub: https://github.com/rithwikkolluru
- Email: rithwikkolluru7@gmail.com

---

##  License

This project is developed for educational and portfolio purposes.
