# Django-Rest-Framework-API
"Beginner Django REST Framework API project"
<br>

#Django REST Framework – API Project
<br>

This is a beginner-friendly Django REST Framework (DRF) project that demonstrates how to build RESTful APIs using DefaultRouter and ViewSets.
<br>

The project exposes APIs for managing Users and Groups and includes Django Admin for backend management.
<br>

🚀 Features
<br>
1.Django REST Framework integration<br>
2.DefaultRouter with API Root <br>
3.User & Group APIs <br>
4.Browsable REST API <br>
5.JSON & HTML renderers <br>
6.Django Admin Panel <br>
7.Clean project structure
<br>

🛠 Tech Stack
<br>
1.Python 3.11<br>
2.Django<br>
3.Django REST Framework<br>
4.SQLite (default database)
<br>

📂 Project Structure
<br>
Django-RestFramework/
│<br>
├── tutorial/ <br>      
├── quickstart/ <br> 
├── manage.py <br>
└── requirements.txt<br>

🔗 API Endpoints<br>

Endpoint	Description <br>

/	API Root<br>
/users/	List & create users<br>
/users/<id>/	Retrieve, update, delete user<br>
/groups/	List & create groups<br>
/groups/<id>/	Retrieve, update, delete group<br>
/admin/	Django Admin Panel<br>

▶️ How to Run the Project<br>

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

📸 API Root Output<br>
{<br>
  "name": "Api Root",<br>
  "description": "The default basic root view for DefaultRouter"<br>
}
<br>

📌 Learning Outcome
<br>
#Understood Django REST Framework basics <br>
#Implemented ViewSets and Routers <br>
#Built RESTful APIs <br>
#Worked with Django Admin <br>
#Learned API Root & Browsable API <br>

👨‍💻 Author
<br>
Samarth Deshmukhe <br>
B.Tech in Artificial Intelligence & Machine Learning

⭐ Future Enhancements <br>

JWT Authentication <br>
Permissions & Roles <br>
Custom User Model <br>
PostgreSQL integration <br>
API documentation using Swagger

