# adelriorz-Portfolio Developer Portfolio Website

Armando Del Rio porfolio for web based apps, React, Django, Python, Java website built using **Django 4**, **Django REST Framework 3**, **React 18**, and **Material UI 5**.

## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the application](#run-the-application)
- [Adding data to the application](#add-data-to-the-application)
- [Copyright and License](#copyright-and-license)

### Prerequisites

Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
<br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Node.js](https://nodejs.org/en/)
3. [Visual Studio Code](https://code.visualstudio.com/download)


### Installation

#### Backend

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
cd backend
```
```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **backend** directory, run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required backend dependencies

From the **backend** directory, run:

```bash
pip install --cache-dir .pip_cache -r requirements.txt
```

#### 4. Run migrations

From the **backend** directory, run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

#### 5. Create an admin user to access the Django Admin interface

From the **backend** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

#### Frontend

#### 1. Install required frontend dependencies

From the **root** directory, run:

```bash
cd frontend
```
```bash
npm install
```

### Run the application

To run the application, you need to have both the backend and the frontend up and running.

#### 1. Run backend

From the **backend** directory, run:

```bash
python manage.py check --deploy # Check if ready to run
python manage.py collectstatic # Collects static files
python manage.py runserver # Enables app to run on browser
```

#### 2. Run frontend

From the **frontend** directory, run:

```bash
npm start
```

#### 3. View the application

Go to http://localhost:3000/ to view the application.


### Add data to the application

Add data through Django Admin.

Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.
