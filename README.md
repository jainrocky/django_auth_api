# Installation and Usage Guide

## Installation 

* move to assignment directory `cd intellify_assignment`.

* create virtual environment `virtualenv intellify`.

* install all required modules `pip install -r requirements.txt`.

## Usage

* move to project directory `cd Intellify_assignment`.

* command for make migrations `python manage.py makemigrations`.

* command for migrate `python manage.py migrate`.

* now run the server `python manage.py runserver`.

* open the url `http://localhost:8000` for documentation.

* for register new user open the url `http://localhost:8000/api/register` in browser .

* to register new user fill all the fields in the browser or pass this field in body params using postman or anyother similar application.
if everything is correct. it will return success message.

* to login with the resgisterd users. open the url `http://localhost:8000/api/login?user_name=<USER-NAME>&password=<PASSWORD>`.
if user_name and password is correct. it will return success message with user_bio_data.




