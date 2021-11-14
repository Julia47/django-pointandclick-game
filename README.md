# Django Game

Small point-and-click browser-based game, wroted in Django framework. Project writed as collage diploma, and not mean seriosly game project. 

## Installation 
- Python dependency
  ```python
  pip3 install -U Django django-crispy-forms jinja2 
  ```
- SQLite
  ```sh
  # arch
  sudo pacman -S sqlite3
  # debian
  sudo apt install sqlite3
  # fedora
  sudo dnf install sqlite
  ```
  

## Run project
To build this game
1. run commands
   ```sh
   # for preparing and making migration to SQLite
   python manage.py makemigrations
   python manage.py migrate
   # special step for generating game assets, and swap it to DB
   python manage.py build_data
   # running debug python server
   python manage.py runserver
   ```
2. create user with path  ->   http://127.0.0.1:8000/catalog/register/
3. or login with (`julka`, `zibert230`)   http://127.0.0.1:8000/catalog/login
4. main url -> http://127.0.0.1:8000/catalog/house/
