# 📝 Blog Website – Django Web Application

A full-featured **Django blog website** that includes user authentication, post management, categories, templates, and a clean architecture following Django best practices.

This project demonstrates skills in **backend development, REST architecture, database modeling, template rendering, authentication, and deployment structure**.

---

## 🚀 Features

- **User Authentication**
  - Register, login, logout
  - Protected routes for creating/editing posts

- **Blog Post Management**
  - Create, update, delete, and publish posts
  - Category-based organization

- **Responsive UI**
  - Clean templates using Django Template Language (DTL)

- **Admin Dashboard**
  - Manage posts, categories, users

- **Database Integration**
  - SQLite (default)
  - Easily switch to PostgreSQL/MySQL

---

## 📁 Repository Structure
Blog-Website/
├── BlogWebsite/                 # Main Django project folder
│   ├── blog/                   # Blog application
│   │   ├── templates/          # HTML templates for the blog
│   │   │   ├── index.html      # Homepage with all posts
│   │   │   ├── post_detail.html # Individual post view
│   │   │   ├── add_post.html   # Create new post form
│   │   │   └── edit_post.html  # Edit existing post form
│   │   │
│   │   ├── migrations/         # Database migration history
│   │   │   ├── 0001_initial.py # Initial database schema
│   │   │   └── __init__.py
│   │   │
│   │   ├── static/             # CSS, images, JS
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   │
│   │   ├── models.py           # Blog models (Post, Category)
│   │   ├── views.py            # Business logic and views
│   │   ├── urls.py             # Local URL routing
│   │   └── forms.py            # Django forms (if used)
│   │
│   ├── BlogWebsite/            # Project-level config
│   │   ├── settings.py         # All project settings
│   │   ├── urls.py             # Main URL routing
│   │   ├── wsgi.py             # WSGI entry point
│   │   └── asgi.py             # ASGI entry point
│   │
│   ├── db.sqlite3              # Default development database
│   └── manage.py               # Django CLI tool
│
└── README.md                   # Project description




## 🧪 How to Run the Project Locally

```bash
# Clone the repository
git clone https://github.com/Athari22/Blog-Website.git

# Navigate to the directory
cd Blog-Website/BlogWebsite

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```


**🛠️ Technologies Used**
  - Python & Django
  - SQLite / PostgreSQL
  - HTML, CSS (Django Templates)
  - Git & GitHub
  - Django Admin
  - 
**🛠️ Technologies Used**
  - Python & Django
  - SQLite / PostgreSQL
  - HTML, CSS (Django Templates)
  - Git & GitHub
  - Django Admin




This project contains three main internal folders, each serving a different layer of the Django application.

