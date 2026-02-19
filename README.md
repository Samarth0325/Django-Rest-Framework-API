# Django-Rest-Framework-API
"Beginner Django REST Framework API project"

#Django REST Framework – API Project

This is a beginner-friendly Django REST Framework (DRF) project that demonstrates how to build RESTful APIs using DefaultRouter and ViewSets.

The project exposes APIs for managing Users and Groups and includes Django Admin for backend management.

🚀 Features

1.Django REST Framework integration
2.DefaultRouter with API Root
3.User & Group APIs
4.Browsable REST API
5.JSON & HTML renderers
6.Django Admin Panel
7.Clean project structure

🛠 Tech Stack

1.Python 3.11
2.Django
3.Django REST Framework
4.SQLite (default database)

📂 Project Structure
Django-RestFramework/
│
├── tutorial/        # Main project settings
├── quickstart/      # API app (ViewSets, Serializers)
├── manage.py
└── requirements.txt

🔗 API Endpoints
Endpoint	Description
/	API Root
/users/	List & create users
/users/<id>/	Retrieve, update, delete user
/groups/	List & create groups
/groups/<id>/	Retrieve, update, delete group
/admin/	Django Admin Panel

▶️ How to Run the Project

1.Clone the repository:-

git clone https://github.com/your-username/your-repo-name.git

2.Create virtual environment

python -m venv env
env\Scripts\activate

3.Install dependencies

pip install -r requirements.txt

4.Run migrations

python manage.py migrate

5.Create superuser

python manage.py createsuperuser

6.Start server

python manage.py runserver

7.Open in browser:

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin/

📸 API Root Output
{
  "name": "Api Root",
  "description": "The default basic root view for DefaultRouter"
}

📌 Learning Outcome

#Understood Django REST Framework basics
#Implemented ViewSets and Routers
#Built RESTful APIs
#Worked with Django Admin
#Learned API Root & Browsable API

👨‍💻 Author

Samarth Deshmukhe
B.Tech in Artificial Intelligence & Machine Learning

⭐ Future Enhancements

JWT Authentication
Permissions & Roles
Custom User Model
PostgreSQL integration
API documentation using Swagger

