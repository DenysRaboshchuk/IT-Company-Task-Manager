# It-Company-Task-Manager

Django project to managing tasks and workers in teams and projects

## Check it out

[It-Company-Task-Manager deployed to render](https://it-company-task-manager-ibdh.onrender.com)

```
Login: testuser
Password: testpassword123
```

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
```
Then you need to create .env file next to .env.sample. You can take .env.sample as example and insert your values!<br>
Finally, we run this commands:

```python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Demo

<img width="1839" alt="main_page" src="https://github.com/DenysRaboshchuk/IT-Company-Task-Manager/assets/120589625/44b7043d-a7a5-4f44-9b1a-ce528029a518">
<img width="1907" alt="tasks_list_page" src="https://github.com/DenysRaboshchuk/IT-Company-Task-Manager/assets/120589625/5a2756b6-263e-453f-afac-50f0f221c08f">
<img width="1907" alt="task_detail_page" src="https://github.com/DenysRaboshchuk/IT-Company-Task-Manager/assets/120589625/d5bd4e0d-30a1-4fd3-9460-e241a28b767b">
