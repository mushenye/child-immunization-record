# child-immunization-record
Description
A Django-based application designed to provide child immunization alerts via SMS and email. This app keeps track of children, their immunization schedules, and notifies parents when vaccinations are due.

Features
User registration and authentication
CRUD operations for children, vaccines, and immunization schedules
Automated immunization alerts via SMS and email
API endpoints for managing children, vaccines, and schedules
Requirements
Python 3.8+
Django 3.x+
PostgreSQL
Twilio (for SMS alerts)
Django REST Framework
Installation
1. Clone the Repository
bash
Copy code
git clone git@github.com:mushenye/child-immunization-record.git
cd your-repo-name
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies.

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. Install Dependencies
Install required packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Set Up PostgreSQL Database
Ensure PostgreSQL is installed and running. Create a new database and user with appropriate privileges.

5. Configure Environment Variables
Create a .env file in the project root and add your settings:

plaintext
Copy code
SECRET_KEY='your-django-secret-key'
DB_NAME='your-database-name'
DB_USER='your-database-username'
DB_PASSWORD='your-database-password'
DB_HOST='localhost'
DB_PORT='5432'

# Twilio Settings
TWILIO_ACCOUNT_SID='your-twilio-account-sid'
TWILIO_AUTH_TOKEN='your-twilio-auth-token'
TWILIO_PHONE_NUMBER='your-twilio-phone-number'
6. Configure Django Settings
Update settings.py to use these environment variables for DATABASES and TWILIO configuration.

7. Run Migrations
Apply migrations to set up your database schema:

bash
Copy code
python manage.py migrate
8. Create a Superuser
Create an admin account to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
9. Start the Development Server
Run the server to check everything is set up correctly:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/admin to log in to the admin panel with your superuser account.

Usage
Admin Interface: Log in to the Django admin interface to add and manage children, vaccines, and immunization schedules.
API Endpoints: Use API clients like Postman to interact with the following endpoints:
/api/children/: CRUD operations for children.
/api/vaccines/: CRUD operations for vaccines.
/api/immunization-schedules/: CRUD operations for immunization schedules.
Alerts: The application can be configured to send SMS or email alerts automatically (daily) to notify parents of upcoming vaccinations.
Scheduled Tasks
To automatically send SMS alerts daily, use Django-crontab or Celery.

For example, with Django-crontab:

Install Django-crontab:
bash
Copy code
pip install django-crontab
Add the following to your settings:
python
Copy code
INSTALLED_APPS = [
    # other apps
    'django_crontab',
]
CRONJOBS = [
    ('0 9 * * *', 'api.utils.send_immunization_alerts'),  # Runs every day at 9 AM
]
Add the job to the system’s cron:
bash
Copy code
python manage.py crontab add
Testing
To run tests for the application, use:

bash
Copy code
python manage.py test
Contributing
Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature-branch)
Open a Pull Request
License
This project is licensed under the MIT License.