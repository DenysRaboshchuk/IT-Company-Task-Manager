# It-Company-Task-Manager

Django project to managing tasks and workers in teams and projects

## Features
Authentication functionality for Worker/User
Managing teams & tasks & project directly from website
Powerful admin panel for advanced managing
Worker can create tasks.
Worker can change position
Tasks can change deadline & completed & priority


## Installation

Python3 and Django must be already installed

```python
git clone https://github.com/DenysRaboshchuk/IT-Company-Task-Manager.git
cd IT_Company_Task_Manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## How it looks

![main_page.png](..%2Fscreens%2Fmain_page.png)
![tasks_list_page.png](..%2Fscreens%2Ftasks_list_page.png)
![task_detail_page.png](..%2Fscreens%2Ftask_detail_page.png)