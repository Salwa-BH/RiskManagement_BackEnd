# Risk Management Backend

This project uses python 3.8.2, so please install at least python 3.8, we recommend installing the latest version of python since the project may use the latest features of python 3.8.

## Requirements

This project requires the following technologies :

- Python 3.8.2 or greater https://www.python.org/downloads/
- PostgreSQL 12 or greater : https://www.postgresql.org/download/ (select PgAdmin in the installation window to get a Comprehensive DB Web Manager)

## Installation

If it is your first time to pull this repository on your local machine, please create a python virtual environment by following the steps below :

1. open your preferred terminal in the root of the project (make sure that you added python to the system path)
2. your terminal should point now to 'backend/', create a virtual environment by typing : `python -m venv venv`
3. now that you created the virtual environment, let's activate it by typing :
   1. For windows : `.\venv\Scripts\activate.bat`
   2. For MacOS / Linux distros : `source ./venv/bin/activate`
4. now that you have activated the virtual environment, let's install the project's required dependencies by typing `pip install -r requirements.txt` into your terminal
5. Now let's create the database, let's assume you have already installed postgres and it is up and running :
   1. First : change the user and password and even the host link if postgresql is installled on a remote machine or a different port in ./riskmanagement/settings.py -> Databases Object
   2. Create a database on on your postgre instance using PgAdmin (or console if you would like to)
   3. Change its name in settings.py
   4. Now, create migrations by typing : `python manage.py makemigrations`
   5. Finally, let us create the db tables by typing : `python manage.py migrate`

## Running the project :

To run the project, open a terminal pointing to the root of the folder and type : `python manage.py runserver` , if the server started correctly, if will show you a link to the deployed project's root, if not please check if :

- If you haven't activated/installed the virtual environment (Refer to [Installation](#Installation))
- If you did not install the required dependencies (Also refer to [Installation](#Installation))

## Reset password for admin :
click on the link http://localhost:8000/reset_password/

## Api of resetting password :
click on the link http://localhost:8000/accounts/password-reset/


## Changing to a custom user model mid-project :

There are two ways to migrate from the default user in django to the custom user in mid-project
* Delete the database:
The easiest way
* Without deleting database:
To integrate and use the custom user in django, follow the steps.
1- Manually delete all default django tables using the script given in pgAdmin4:
---------------------------------
DROP TABLE django_session CASCADE;
DROP TABLE django_migrations CASCADE;
DROP TABLE django_admin_log CASCADE;
DROP TABLE authtoken_token CASCADE;
DROP TABLE auth_user_user_permissions CASCADE;
DROP TABLE auth_user_groups CASCADE;
DROP TABLE auth_user CASCADE;
DROP TABLE auth_group_permissions CASCADE;
DROP TABLE auth_group CASCADE;
DROP TABLE auth_permission CASCADE;
DROP TABLE django_content_type CASCADE;
--------------------------------
2- python makemigrations accounts
3- python manage.py migrate accounts

If you get this error " django.db.utils.ProgrammingError: relation "processes_companysite" already exists " then type the command
$ python manage.py migrate processes --fake
$ python manage.py migrate risks --fake
$ python manage.py migrate accounts

# Links for more information in changing to custom user
https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
https://code.djangoproject.com/ticket/25313

# Add SQL
To add elements directly, there is sql code to populate tables in addSQLmd file, copy the code and execute it. Please remember that you have to create the user manually, then assign to it a profile, and connect to this user so you can see pages and not the unauthorized page.