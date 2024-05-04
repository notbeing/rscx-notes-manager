"""Модуль views отвечает за представления интерфейса пользователя менеджера заметок."""

import os
from contextlib import contextmanager
from typing import List, Tuple, Callable, Optional

from modules.controllers import (
    get_notes_list,
    create_note,
    search_notes_by_query,
    delete_note_by_id,
)
from modules.models import Note


@contextmanager
def clear_console():
    """Контекстный менеджер для очистки консоли."""

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    clear()
    try:
        yield clear
    finally:
        print()


def display_menu(options: dict[str, Tuple[Callable, str]]) -> Optional[Callable]:
    """Отображает меню и возвращает выбранное действие."""
    print("Менеджер заметок:")
    for choice, (_, description) in options.items():
        print(f"{choice}. {description}")
    choice = input("Выберите действие: ")
    return options.get(choice, (None, None))[0]


def show_all_notes() -> None:
    """Отображает список всех заметок с ID и заголовком, позволяя выбрать заметку для просмотра."""
    notes: List[Note] = get_notes_list()

    while True:
        with clear_console():
            if not notes:
                print("Заметок нет.")
                input("Нажмите Enter, чтобы вернуться в главное меню...")
                return

            for i, note in enumerate(notes):
                print(f"{i+1}. {note}")

            try:
                choice = int(
                    input("Выберите заметку для просмотра (или 0 для возврата): ")
                )
                if 0 <= choice <= len(notes):
                    if choice == 0:
                        return
                    show_note_details(notes[choice - 1])
                    return
                print("Неверный выбор. Пожалуйста, введите номер из списка.")
            except ValueError:
                print("Неверный выбор. Пожалуйста, введите номер заметки.")


def show_note_details(note: Note) -> None:
    """Отображает подробную информацию о выбранной заметке."""
    with clear_console() as clear:
        print(f"ID: {note.id}")
        print(f"Заголовок: {note.title}")
        print(f"Содержание: {note.get_content()}")

    input("Нажмите Enter, чтобы вернуться в главное меню...")
    clear()


def add_note_menu() -> None:
    """Запрашивает у пользователя данные для новой заметки и добавляет ее в базу данных."""

    with clear_console() as clear:
        while True:
            title = input("Введите заголовок заметки: ").strip()
            content = input("Введите содержание заметки: ").strip()

            if not title or not content:
                clear()
                print("Заголовок и содержание заметки не могут быть пустыми.")
                continue

            if any(not c.isprintable() for c in title + content):
                clear()
                print(
                    "Заголовок и содержание заметки не должны содержать управляющих символов."
                )
                continue

            create_note(title, content)
            clear()
            print("Заметка добавлена!")

            user_input = input(
                "Нажмите Enter, чтобы вернуться в главное меню, или 'n' для добавления ещё одной заметки: "
            ).lower()
            clear()
            if user_input != "n":
                break


def search_notes_menu() -> None:
    """
    Запрашивает у пользователя поисковый запрос, отображает результаты поиска,
    и позволяет выбрать заметку для просмотра подробной информации.
    """

    with clear_console() as clear:
        while True:
            query = input("Введите поисковый запрос: ")
            if query.strip():
                break
            clear()
            print(
                "Поисковый запрос не может быть пустым. Пожалуйста, попробуйте ещё раз."
            )

        results = search_notes_by_query(query)

        if not results:
            clear()
            print("Заметок по такому запросу не существует.")
            input("Нажмите Enter, чтобы вернуться в главное меню.")
            return

        for i, note in enumerate(results):
            print(f"{i+1}. ID: {note.id}, Заголовок: {note.title}")

        while True:
            try:
                choice = int(
                    input("Выберите заметку для просмотра (или 0 для возврата): ")
                )
                if 0 <= choice <= len(results):
                    if choice == 0:
                        clear()
                        return
                    show_note_details(results[choice - 1])
                    return
                print("Неверный выбор. Пожалуйста, введите номер из списка.")
            except ValueError:
                clear()
                print("Неверный выбор. Пожалуйста, введите номер заметки.")


def delete_note_menu() -> None:
    """Запрашивает у пользователя ID заметки для удаления и проверяет его наличие."""
    while True:
        with clear_console() as clear:
            note_id_str: str = input("Введите ID заметки для удаления: ")
            try:
                note_id: int = int(note_id_str)
                if note_id <= 0:
                    print("ID заметки должен быть положительным числом.")
                    continue

                notes: List[Note] = get_notes_list()
                if any(note.id == note_id for note in notes):
                    delete_note_by_id(note_id)
                    clear()
                    print("Заметка удалена!")
                    break
            except ValueError:
                print("Неверный ID заметки.")


def main_menu() -> None:
    """Главная функция приложения, отображающая меню и обрабатывающая выбор пользователя."""
    options = {
        "1": (show_all_notes, "Показать все заметки"),
        "2": (add_note_menu, "Добавить заметку"),
        "3": (search_notes_menu, "Найти заметку"),
        "4": (delete_note_menu, "Удалить заметку"),
        "5": (exit, "Выход"),
    }

    while True:
        with clear_console() as clear:
            action = display_menu(options)
            if action:
                clear()
                action()
            else:
                clear()
                print("Неверный выбор.")
