"""
Модуль database предоставляет функции для взаимодействия с базой данных SQLite 
для приложения менеджера заметок.

Он включает в себя контекстный менеджер ConnectDb для управления подключением 
к базе данных, а также функции для создания таблиц, добавления, получения, 
поиска и удаления заметок.
"""

import sqlite3
from contextlib import closing
from typing import Any, List, Tuple

DB_NAME = "data/notes.db"


class ConnectDb:
    """Контекстный менеджер для подключения к базе данных SQLite."""

    def __init__(self):
        self.conn = None

    def __enter__(self) -> sqlite3.Connection:
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


def create_tables(conn: sqlite3.Connection) -> None:
    """Создает таблицу 'notes' в базе данных, если она не существует."""
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            """
			CREATE TABLE IF NOT EXISTS notes (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				title TEXT NOT NULL, 
				content TEXT 
			) 
			"""
        )
        conn.commit()


def initialize_database():
    """Инициализирует базу данных, создавая таблицы, если они не существуют."""
    with ConnectDb() as conn:
        create_tables(conn)


def add_note(conn: sqlite3.Connection, title: str, content: str) -> None:
    """Добавляет новую заметку с заданным заголовком и содержанием в базу данных."""
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)", (title, content)
        )
        conn.commit()


def get_all_notes(conn: sqlite3.Connection) -> List[Tuple[Any, ...]]:
    """Получает список всех заметок из базы данных."""
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM notes")
        return cursor.fetchall()


def search_notes(conn: sqlite3.Connection, query: str) -> List[Tuple[Any, ...]]:
    """Ищет заметки, содержащие заданный поисковый запрос в заголовке или содержании."""
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            "SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?",
            ("%" + query + "%", "%" + query + "%"),
        )
        return cursor.fetchall()


def delete_note(conn: sqlite3.Connection, note_id: int) -> None:
    """Удаляет заметку с заданным ID из базы данных."""
    with closing(conn.cursor()) as cursor:
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
