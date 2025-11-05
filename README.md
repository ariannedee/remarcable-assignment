# Remarcable assignment
Arianne Dee - _November 2025_

Todo: Purpose

## Setting up the project

1. Install Python (I used 3.14 but 3.12+ should work)
2. Create a virtual environment and activate it (optional): `python3.14 -m venv .venv` then `source .venv/bin/activate` (on Unix)
3. Install requirements: `pip install -r requirements.txt`
4. Navigate into the folder that contains `manage.py`: `cd remarcable_project`
5. Initialize and migrate the database: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Load the sample data: `python manage.py loaddata tags categories products`

## Running the code

In your activated virtual environment (optional), 
from the `remarcable_project` directory containing `manage.py`, 
run:

`python manage.py runserver`

The main site will be available at http://127.0.0.1:8000/.

The admin site will be available at http://127.0.0.1:8000/admin.

You can log in to the admin site using your superuser credentials created above.

## Assumptions

- Using a basic virtual environment suffices and knowledge of other tools like `uv` is not being evaluated
- Running on a production environment is not needed
- Using `sqlite` for a database is sufficient
- Using the built-in `User` model is sufficient, along with username sign in instead of email
- Creating multiple apps is overkill for the scope
- I'm not being evaluated too much on the folder structure


## AI Attribution

I used AI to generate believable product names, categories and tags.