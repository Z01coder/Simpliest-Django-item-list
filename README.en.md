<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- LANGUAGE SWITCHER -->
<div align="right">
  <strong>Language:</strong> <a href="README.en.md">English</a> | <a href="README.md">Русский</a>
</div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Django Film Manager</h3>

  <p align="center">
    A simple Django application for managing a film list
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Preview](static/images/3g.webp)

Django Film Manager is a simple Django web application for managing a film list. The project demonstrates basic CRUD functionality using the Django framework.

<details>
  <summary><strong>Project Goals and Objectives</strong></summary>

**Goals:**
* Create a simple and functional web application for managing a film list
* Demonstrate basic Django framework capabilities
* Implement user authentication and authorization system
* Ensure application security at all levels

**Key Objectives:**
* Develop a data model for storing film information
* Create a user interface for viewing and adding films
* Implement user login and logout system
* Configure admin panel for data management
* Implement data validation at model and form levels
* Ensure protection against XSS attacks and other vulnerabilities
* Implement rate limiting to protect against abuse
* Configure security event logging
* Create a custom command for quick test user creation

</details>

<details>
  <summary><strong>Results</strong></summary>

**Implemented Functionality:**
* View film list (available to all users)
* Add new films (requires authorization)
* User authentication system
* Admin panel for data management
* Data validation at model and form levels
* Protection against XSS attacks and other vulnerabilities
* Rate limiting to protect against abuse
* Security logging

**Created Components:**
* Django application `films` for working with films
* `Film` model with fields: title, description, and review
* HTML pages: film list and add form
* Base template with navigation and improved design
* Custom command for creating test superuser

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Main technologies and libraries used in the project:

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]

Additional dependencies:
* `python-decouple==3.8` - for managing settings through environment variables
* `django-ratelimit==4.1.0` - for request rate limiting
* `django-bleach==3.1.0` and `bleach>=5.0.0,<6.0.0` - for HTML content sanitization

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
<details>
  <summary><strong>Getting Started</strong></summary>

Instructions for installing and running the project locally.

### Prerequisites

To work with the project, you need to install:

* Python 3.x
  ```sh
  # Check Python version
  python --version
  ```

### Installation

Below are instructions for installing and configuring the application.

1. Clone the repository
   ```sh
   git clone https://github.com/your_username/repo_name.git
   cd Simpliest-Django-item-list
   ```

2. Create a virtual environment (recommended)
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```sh
   python manage.py migrate
   ```

5. Create a test superuser
   ```sh
   python manage.py create_test_superuser
   ```
   
   By default, a user is created with:
   - **Username:** `admin`
   - **Password:** `admin123`
   - **Email:** `admin@example.com`
   
   To create a user with different data:
   ```sh
   python manage.py create_test_superuser --username testuser --password testpass123 --email test@example.com
   ```

6. Run the development server
   ```sh
   python manage.py runserver
   ```

7. Open in browser:
   - Main page: http://127.0.0.1:8000/films/list/
   - Admin panel: http://127.0.0.1:8000/admin-panel-secure/

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<details>
  <summary><strong>Usage</strong></summary>

The application provides the following pages and functionality:

### Main Pages:

1. **Film List** (`/films/list/`)
   - Displays all films from the database
   - Available to all users without authorization
   - Shows title, description, and review for each film

2. **Add Film** (`/films/add/`)
   - Form for adding a new film
   - Requires authorization
   - Includes data validation
   - Protected against abuse (rate limiting: 10 requests per hour)

3. **Login** (`/films/login/`)
   - User authentication page
   - Protected against brute force attacks (rate limiting: 5 attempts per minute)
   - Logging of all login attempts

4. **Admin Panel** (`/admin-panel-secure/`)
   - Standard Django admin panel
   - URL changed for enhanced security
   - Full access to data management

### Security:

- Data validation at model and form levels
- Protection against XSS attacks through HTML sanitization
- Rate limiting for critical operations
- Security event logging
- Configured security headers

</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<details>
  <summary><strong>Show completed development stages</strong></summary>

### Completed Stages:

- [x] **Stage 1: Basic Project Structure**
  - [x] Create Django project `movie_project`
  - [x] Create application `films`
  - [x] Configure basic URL structure and routing

- [x] **Stage 2: Data Model**
  - [x] Develop `Film` model with fields: title, description, review
  - [x] Create and apply database migrations
  - [x] Add `created_at` and `updated_at` fields for time tracking

- [x] **Stage 3: Basic Views and Templates**
  - [x] Implement view for displaying film list
  - [x] Create HTML templates for film list
  - [x] Configure base template with navigation

- [x] **Stage 4: Authentication System**
  - [x] Implement user login page
  - [x] Implement logout functionality
  - [x] Configure decorators for protecting pages requiring authorization
  - [x] Configure redirects after login/logout

- [x] **Stage 5: Add Film Functionality**
  - [x] Create `FilmForm` form for adding films
  - [x] Implement view for form processing
  - [x] Create HTML template for add form

- [x] **Stage 6: Data Validation**
  - [x] Implement validation at model level (method `clean()`)
  - [x] Implement validation at form level (methods `clean_*()`)
  - [x] Check minimum and maximum field lengths
  - [x] Basic protection against dangerous characters

- [x] **Stage 7: XSS Attack Protection**
  - [x] Integrate `django-bleach` and `bleach` libraries
  - [x] Sanitize HTML content in forms
  - [x] Remove HTML tags via `strip_tags()`
  - [x] Check for dangerous patterns (script, javascript:, onerror, onload)

- [x] **Stage 8: Rate Limiting (Request Rate Limiting)**
  - [x] Integrate `django-ratelimit` library
  - [x] Limit login attempts (5 attempts per minute)
  - [x] Limit film additions (10 requests per hour)
  - [x] Handle limit exceedances with informative messages

- [x] **Stage 9: Security Logging**
  - [x] Configure logging system in `settings.py`
  - [x] Create separate logger for security events
  - [x] Log successful and failed login attempts
  - [x] Log limit exceedances and validation errors
  - [x] Configure log files (`django.log`, `security.log`)

- [x] **Stage 10: Security Settings**
  - [x] Configure security headers (XSS Protection, Content Type Nosniff, Frame Options)
  - [x] Configure session security (HttpOnly, Secure, SameSite)
  - [x] Configure CSRF protection
  - [x] Configure HSTS for production
  - [x] Basic Content Security Policy configuration

- [x] **Stage 11: Managing Settings via Environment Variables**
  - [x] Integrate `python-decouple` library
  - [x] Move secret keys to environment variables
  - [x] Configure `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` via `.env`

- [x] **Stage 12: User Interface Improvements**
  - [x] Integrate Bootstrap 5.3 for modern design
  - [x] Create responsive navigation bar
  - [x] Improve forms with Bootstrap CSS classes
  - [x] Display user status in navigation

- [x] **Stage 13: Admin Panel**
  - [x] Configure Django admin panel for Film model
  - [x] Add filters and search in admin panel
  - [x] Change standard admin panel URL to `/admin-panel-secure/`
  - [x] Configure admin panel headers

- [x] **Stage 14: Custom Management Commands**
  - [x] Create `create_test_superuser` command for quick test user creation
  - [x] Implement command line argument support
  - [x] Add user existence check

- [x] **Stage 15: Localization**
  - [x] Configure Russian language interface
  - [x] Translate model field names to Russian
  - [x] Russian validation error messages

- [x] **Stage 16: Documentation**
  - [x] Create detailed README.md with project description
  - [x] Add installation and configuration instructions
  - [x] Describe functionality and application pages
  - [x] Document security settings
  - [x] Describe used technologies and dependencies

</details>

### Planned Improvements:

- [ ] Add film editing functionality
- [ ] Add film deletion functionality
- [ ] Implement film category system
- [ ] Add ability to upload images for films
- [ ] Implement film rating system
- [ ] Add pagination for film list
- [ ] Implement full-text search
- [ ] Add API endpoints (REST API)
- [ ] Write unit tests
- [ ] Configure CI/CD pipeline

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion to improve this, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [![GitHub][GitHub-badge]][GitHub-url]
* [![Gmail][Gmail-badge]][Gmail-url]
* [![Telegram][Telegram-badge]][Telegram-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I express my sincere gratitude to [Zerocoder University](https://zerocoder.ru/) and its entire team for creating an inspiring and professional educational environment. For preparing "IT-astronauts" at the Zerocoder "cosmodrome".

Special thanks to:

[Kirill Pshinnik](https://kpshinnik.ru/), director of the university, for inspiring achievements;

Teachers [Nina Stefantsova](https://neural-courses.ru/teacher/nina-stefancova/), [Maxim Vershinin](https://neural-courses.ru/teacher/maksim-vershinin/), and [Darya Bobrovskaya](https://neural-courses.ru/teacher/darya-bobrovskaya/) — for deep knowledge, patience, and readiness to always help;

Nikita Murkin, course curator, for clear organization and mentorship;

Elizaveta, manager, for care, responsiveness, and unwavering kindness.

Thanks to you, this project became possible!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[GitHub-badge]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/Z01coder
[Gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Gmail-url]: mailto:zolotuxin.alexey@gmail.com
[Telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://t.me/AZVXAN

