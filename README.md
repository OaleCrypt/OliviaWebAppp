README Summary for Django Portfolio Website

Project Overview
Welcome to my Django Portfolio Website! This project is a personal portfolio showcasing various projects, including a sophisticated Security Operations Center (SOC) Incident Management system, a Password Manager, and other demos. Built with the Django framework and PostgreSQL as the database backend, this website highlights my skills in web development and cybersecurity.

Current versions:
(python 3.10)
(django 5.0.6)

Key Features
Portfolio:

A collection of projects displayed in an organized and visually appealing manner.
Each project entry includes a title, a brief description, and links to further details or external resources.
Projects are categorized and can be filtered for easy navigation.
SOC Incident Management:

This app simulates a SOC dashboard allowing users to manage security incidents.
Features include creating incidents, listing incidents with expandable details, and editing incident severity.
The app integrates with a live attack map showing real-time security events.
Alert System:

Users can view and create alerts with dynamic priority settings.
The alert list supports expanding details and prioritizing alerts similar to the incident management system.
Password Manager:

A secure password management tool allowing users to store and manage passwords efficiently.
Features encryption and secure storage for user credentials.
Technologies Used
Django: The main framework used for building the backend and managing the server-side logic.
PostgreSQL: A robust relational database system used to manage and store application data.
HTML/CSS/JavaScript: For structuring, styling, and adding interactivity to the web pages.
Flatpickr: A lightweight JavaScript library used for date and time pickers in forms.
Bootstrap: A CSS framework for responsive design and UI components.

Getting Started
To run this project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code below
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the project root with the following content:

env
Copy code below
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=your-db-name
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=your-db-host
DATABASE_PORT=your-db-port

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
Apply Migrations:

bash
Copy code below
python manage.py migrate
Create a Superuser:

bash
Copy code below
python manage.py createsuperuser
Run the Development Server:

bash
Copy code below
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to see the application in action.

Deployment
To deploy this project to a live server, ensure the following:

Configure Production Settings:

Set DEBUG=False in your .env file.
Add your domain to the ALLOWED_HOSTS list in settings.py.
Securely manage and set environment variables on your server.
Collect Static Files:

bash
Copy code below
python manage.py collectstatic
Set Up a Production Database:

Ensure your PostgreSQL database is configured for production use.
Update the .env file with the production database credentials.
Deploy Using Your Preferred Platform:

Follow the deployment steps for your hosting platform (e.g., Heroku, AWS, Azure).

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, please contact me at hello@olivia-le.com.