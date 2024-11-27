# API2
The project is going on a git respository so begin by seting one up and cloning it on a folder where you'll create your models.

After cloning, you have to create your virtual environment and start up the django project

The Codes needed are;

This is to set up the virtual environment, then the project

C:\Users\wanin\Desktop\API2\API2> python -m venv .venv

C:\Users\wanin\Desktop\API2\API2> .\.venv\Scripts\Activate.ps1

(.venv) PS C:\Users\wanin\Desktop\API2\API2> pip install django

(.venv) PS C:\Users\wanin\Desktop\API2\API2> django-admin startproject ecommerce

(.venv) PS C:\Users\wanin\Desktop\API2\API2> cd .\ecommerce\

(.venv) PS C:\Users\wanin\Desktop\API2\API2\ecommerce> django-admin startapp Customer

(.venv) PS C:\Users\wanin\Desktop\API2\API2\ecommerce> django-admin startapp Order

(.venv) PS C:\Users\wanin\Desktop\API2\API2\ecommerce> python manage.py runserver

(.venv) PS C:\Users\wanin\Desktop\API2\API2\ecommerce> cd ..




