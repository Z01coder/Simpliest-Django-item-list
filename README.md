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




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Simpliest Django Item List</h3>

  <p align="center">
    Простое Django приложение для управления списком фильмов
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

![Превью](2.png)
![Превью](1.png)

Simpliest Django Item List - это простое веб-приложение на Django для управления списком фильмов. Проект демонстрирует базовую функциональность CRUD операций с использованием Django framework.

Основные возможности:
* Просмотр списка фильмов (доступно всем пользователям)
* Добавление новых фильмов (требуется авторизация)
* Система аутентификации пользователей
* Админ-панель для управления данными
* Валидация данных на уровне модели и формы
* Защита от XSS атак и других уязвимостей
* Rate limiting для защиты от злоупотреблений
* Логирование безопасности

Проект включает:
* Django приложение `films` для работы с фильмами
* Модель `Film` с полями: название, описание и отзыв
* HTML страницы: список фильмов и форма добавления
* Базовый шаблон с навигацией и улучшенным дизайном
* Кастомная команда для создания тестового суперпользователя

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Основные технологии и библиотеки, используемые в проекте:

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]

Дополнительные зависимости:
* `python-decouple==3.8` - для управления настройками через переменные окружения
* `django-ratelimit==4.1.0` - для ограничения частоты запросов
* `django-bleach==3.1.0` и `bleach>=5.0.0,<6.0.0` - для санитизации HTML контента

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Инструкции по установке и запуску проекта локально.

### Prerequisites

Для работы с проектом необходимо установить:

* Python 3.x
  ```sh
  # Проверьте версию Python
  python --version
  ```

### Installation

Ниже приведены инструкции по установке и настройке приложения.

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/your_username/repo_name.git
   cd Simpliest-Django-item-list
   ```

2. Создайте виртуальное окружение (рекомендуется)
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Установите зависимости
   ```sh
   pip install -r requirements.txt
   ```

4. Примените миграции
   ```sh
   python manage.py migrate
   ```

5. Создайте тестового суперпользователя
   ```sh
   python manage.py create_test_superuser
   ```
   
   По умолчанию создается пользователь:
   - **Имя:** `admin`
   - **Пароль:** `admin123`
   - **Email:** `admin@example.com`
   
   Для создания пользователя с другими данными:
   ```sh
   python manage.py create_test_superuser --username testuser --password testpass123 --email test@example.com
   ```

6. Запустите сервер разработки
   ```sh
   python manage.py runserver
   ```

7. Откройте в браузере:
   - Главная страница: http://127.0.0.1:8000/films/list/
   - Админ-панель: http://127.0.0.1:8000/admin-panel-secure/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Приложение предоставляет следующие страницы и функциональность:

### Основные страницы:

1. **Список фильмов** (`/films/list/`)
   - Отображает все фильмы из базы данных
   - Доступна всем пользователям без авторизации
   - Показывает название, описание и отзыв для каждого фильма

2. **Добавление фильма** (`/films/add/`)
   - Форма для добавления нового фильма
   - Требуется авторизация
   - Включает валидацию данных
   - Защищена от злоупотреблений (rate limiting: 10 запросов в час)

3. **Вход в систему** (`/films/login/`)
   - Страница авторизации пользователей
   - Защищена от брутфорс атак (rate limiting: 5 попыток в минуту)
   - Логирование всех попыток входа

4. **Админ-панель** (`/admin-panel-secure/`)
   - Стандартная Django админ-панель
   - URL изменен для повышения безопасности
   - Полный доступ к управлению данными

### Безопасность:

- Валидация данных на уровне модели и формы
- Защита от XSS атак через санитизацию HTML
- Rate limiting для критических операций
- Логирование событий безопасности
- Настроенные заголовки безопасности

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
