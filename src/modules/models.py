"""
Модуль models определяет структуры данных, используемые в приложении 
менеджера заметок.
"""


class Note:
    """Модель данных для заметки с атрибутами id, title и content."""

    def __init__(self, note_id: int, title: str, content: str):
        self.id: int = note_id
        self.title: str = title
        self.content: str = content

    def __str__(self) -> str:
        """Возвращает строковое представление заметки."""
        return f"Заметка {self.id}: {self.title}"

    def get_content(self) -> str:
        """Возвращает содержание заметки."""
        return self.content
