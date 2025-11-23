"""
Management команда для создания тестового суперпользователя.
Использование: python manage.py create_test_superuser
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Создает тестового суперпользователя для демонстрации проекта'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Имя пользователя (по умолчанию: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Email (по умолчанию: admin@example.com)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Пароль (по умолчанию: admin123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Пользователь "{username}" уже существует!')
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Суперпользователь "{username}" успешно создан!\n'
                f'  Email: {email}\n'
                f'  Пароль: {password}\n'
                f'  Админка: http://127.0.0.1:8000/admin-panel-secure/'
            )
        )

