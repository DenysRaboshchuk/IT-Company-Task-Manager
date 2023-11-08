It-Company-Task-Manager
​
Django project to managing tasks and workers in teams and projects

Features
Authentication functionality for Worker/User
Managing teams & tasks & project directly from website
Powerful admin panel for advanced managing
Worker can create tasks.
Worker can change position
Tasks can change deadline & completed & priority
​
​
Installation
​
Python3 and Django must be already installed
​
git clone https://github.com/DenysRaboshchuk/IT-Company-Task-Manager.git
cd it-company-task-manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
