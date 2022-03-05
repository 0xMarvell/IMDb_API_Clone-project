# IMDB API Clone With DRF
A simple API clone project inspired by IMDb's API

## Project Setup
 - Clone Project or download as zip file.
 ```bash
 git clone https://github.com/Marvellous-Chimaraoke/IMDb_API_Clone-project.git
 ```
 - Create virtual environment.
 ```bash
 pip3 install virtualenv
 virtualenv env
 ```
- Activate virtual environment (MacOS/Linux).
```bash
source env/bin/activate
``` 
- Activate virtual environment (Windows).
```bash
env/scripts/activate.bat
```   
 - Install all requirements from requirements.txt file.
 ```bash
 pip install -r requirements.txt
 ```
 - Run migrations to create database tables.
 ```bash
 python manage.py makemigrations
 python manage.py migrate
 ```
 - Run Project Server.
 ```bash
 python manage.py runserver
 ```
