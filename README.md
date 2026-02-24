# Quizz_Project
QuizPro is a Django-based Quiz Web Application featuring user authentication, Google login, subject-wise MCQ quizzes, timer-based tests, performance analytics, and leaderboard ranking system with a premium animated UI.
#Project Structure
quiz_project/
│
├── quiz_project/
│   ├── settings.py
│   ├── urls.py
│
├── quizapp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│
├── db.sqlite3
└── manage.py
quiz_project/
│
├── quiz_project/
│   ├── settings.py
│   ├── urls.py
│
├── quizapp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│
├── db.sqlite3
└── manage.py
#Installation Guide
git clone https://github.com/your-username/quizpro.git
cd quizpro
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install django
pip install django-allauth
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
#Google OAuth Setup (Important)
http://127.0.0.1:8000/accounts/google/login/callback/
