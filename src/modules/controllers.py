"""
Модуль controllers отвечает за обработку бизнес-логики приложения менеджера заметок.
"""

from typing import List

from .database import ConnectDb, add_note, get_all_notes, search_notes, delete_note
from .models import Note


def create_note(title: str, content: str) -> None:
    """Создает новую заметку с заданным заголовком и содержанием в базе данных."""
    with ConnectDb() as conn:
        add_note(conn, title, content)


def get_notes_list() -> List[Note]:
    """Возвращает список всех заметок из базы данных."""
    with ConnectDb() as conn:
        notes_data = get_all_notes(conn)
    return [Note(*note_data) for note_data in notes_data]


def search_notes_by_query(query: str) -> List[Note]:
    """Ищет заметки, содержащие заданный поисковый запрос в заголовке или содержании."""
    with ConnectDb() as conn:
        notes_data = search_notes(conn, query)
    return [Note(*note_data) for note_data in notes_data]


def delete_note_by_id(note_id: int) -> None:
    """Удаляет заметку с заданным ID из базы данных."""
    with ConnectDb() as conn:
        delete_note(conn, note_id)
