

# Child Immunization Alert System
<img src="Immunization_schedule_720x480.webp">
 
## Description

This is a Django-based application designed to manage child immunization schedules and provide automatic alerts to parents via SMS and email when a child's immunization is due. The application allows CRUD operations for managing children, vaccines, and immunization schedules, and sends notifications to ensure timely vaccinations.

## Features

- User registration and authentication
- API endpoints for managing children, vaccines, and immunization schedules
- Automated SMS and email alerts for upcoming immunizations
- Admin panel for easy management of records

## Technologies Used

- Python 3.8+
- Django 3.x+
- PostgreSQL
- Twilio (for SMS alerts)
- Django REST Framework

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.8+
- PostgreSQL
- Twilio account for SMS alerts
- A virtual environment setup tool (like `venv`)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mushenye/child-immunization-record
cd child-immunization-record
2. Set Up a Virtual Environment
Create and activate a virtual environment:

# Hto set up virtual enviroment
python -m venv env
source env/bin/activate  # For Windows, use `env\Scripts\activate`
3. Install Dependencies
Install the dependencies listed in requirements.txt:


pip install -r requirements.txt
4. Set Up PostgreSQL Database
Make sure PostgreSQL is installed and running, then create a new database and user with the required privileges.

5. Configure Environment Variables
Create a .env file in the project root with the following environment variables:


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
Make sure settings.py uses the above environment variables for database and Twilio configuration.

7. Run Migrations
Apply database migrations to set up the initial schema:

bash
Copy code
python manage.py migrate
8. Create a Superuser
Create an admin account to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
9. Start the Development Server
Run the development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/admin and log in with your superuser credentials.

Usage
Admin Interface: Use the Django admin interface to add and manage children, vaccines, and immunization schedules.
API Endpoints: You can use tools like Postman to access the API endpoints:
/api/children/: Manage child records.
/api/vaccines/: Manage vaccine records.
/api/immunization-schedules/: Manage immunization schedules.
Alerts: The application automatically sends SMS and email alerts to notify parents about upcoming immunizations.
Scheduled Tasks
To send daily SMS alerts, you can use Django-crontab or Celery. Below is an example setup using Django-crontab:

Install Django-crontab:

bash
Copy code
pip install django-crontab
Add the following to your settings:

###
INSTALLED_APPS = [
    # other installed apps
    'django_crontab',
]

###
CRONJOBS = [
    ('0 9 * * *', 'api.utils.send_immunization_alerts'),  # Runs every day at 9 AM
]
Add the cron job to the system:


python manage.py crontab add
Testing
To run tests for the application:

##
python manage.py test
Contributing
Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature-branch)
Open a Pull Request
License
This project is licensed under the Apache License License.

yaml


---

This README should provide clear instructions on installation, configuration, usage, and contributing, making it easy for others to set up and work with your project.





