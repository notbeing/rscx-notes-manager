"""
Менеджер заметок на Python.

Это приложение предоставляет пользователям возможность создавать, хранить, 
искать и удалять заметки с использованием базы данных SQLite.

"""

from modules import database, views

if __name__ == "__main__":
    database.initialize_database()
    views.main_menu()
