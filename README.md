# Flipr Full Stack Django Project 🚀

This is a full-stack web application built using Django, developed as part of the Flipr Placement Task. It features a responsive landing page and a complete admin panel to manage projects, clients, contact entries, and newsletter subscribers.

---

## 🔥 Features

### 🌐 Landing Page
- ✅ List of completed **Projects**
- ✅ Display of **Happy Clients**
- ✅ Responsive **Contact Us** form
- ✅ Email-based **Newsletter** subscription

### 🔐 Admin Panel
- Add/edit/delete **Projects** and **Clients**
- View **Contact** submissions and **Newsletter** subscribers

---

## ⚙️ Tech Stack

| Layer        | Technology          |
|--------------|---------------------|
| Frontend     | HTML, CSS, Bootstrap |
| Backend      | Python, Django       |
| Database     | SQLite               |
| Image Crop   | Pillow               |

---

## 🚀 How to Run Locally

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flipr-django.git
cd flipr-django

### 2. Create and Activate a Virtual Environment

python -m venv venv
venv\Scripts\activate         # On Windows
# or
source venv/bin/activate      # On Mac/Linux

### 3. Install Dependencies

pip install -r requirements.txt
If you don't have a requirements.txt file, create one using:
pip freeze > requirements.txt

### 4. Run Database Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser (for Admin Access)

python manage.py createsuperuser
Enter username, email, password

### 6. Start the Server
python manage.py runserver
Open your browser and visit:
👉 http://127.0.0.1:8000

To access the admin panel:
👉 http://127.0.0.1:8000/admin
