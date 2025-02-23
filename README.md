# Django Social Media Application

This is a basic social media web application built with Django. The application allows users to:
- Register and log in
- Create, edit, and delete posts
- View all posts on the homepage
- View and manage only their own posts on the profile page

---

## Features

- **User Registration and Authentication**: Secure login and registration system.
- **Post Management**: Users can create, edit, and delete their own posts.
- **User Profile**: Each user can view and manage their posts on their profile page.
- **Responsive UI**: Clean and intuitive interface using HTML, CSS, and basic JavaScript.

---

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.12.x or higher
- Django 5.x
- Virtualenv (optional but recommended)

---

## Installation

1. **Clone the Repository**

```bash
git clone <your-repository-url>
cd socialmedia
```

2. **Create a Virtual Environment**

```bash
python3 -m venv env
source env/bin/activate  # On macOS or Linux
env\Scripts\activate     # On Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply Migrations**

```bash
python3 manage.py migrate
```

5. **Create Superuser (Admin)**

```bash
python3 manage.py createsuperuser
```

6. **Run the Development Server**

```bash
python3 manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`

---

## Usage

- Visit the homepage to view all posts.
- Register for a new account or log in with an existing account.
- Create new posts, edit or delete them from your profile page.
- Log out using the "Logout" link in the navigation bar.

---

## Folder Structure

```
socialmedia/
├── socialmedia/            # Main project settings
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL configurations
│   └── wsgi.py
│
├── posts/                  # Posts application
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py           # Post model
│   ├── views.py            # View functions
│   ├── urls.py             # App-specific URLs
│   └── templates/
│       └── posts/          # HTML templates for posts
│           ├── base.html
│           ├── homepage.html
│           ├── profile.html
│           ├── create_post.html
│           ├── edit_post.html
│           └── login.html
│
└── manage.py               # Django management script
```

---

## Technologies Used

- **Backend**: Django 5.x (Python 3.12.x)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)
- **Authentication**: Django's built-in authentication system

---

## Future Enhancements

- Add user profile pictures
- Implement like and comment functionality on posts
- Add follow/unfollow feature
- Enhance UI with modern CSS frameworks (e.g., Tailwind CSS or Bootstrap)

---