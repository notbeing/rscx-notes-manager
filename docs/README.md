# Менеджер заметок на Python:
## Краткая информация:
*Данное приложение представляет собой консольный менеджер заметок, разработанный на языке Python. Он позволяет пользователю создавать, хранить, искать и удалять заметки, используя встроенную базу данных SQLite для хранения информации.*

## Функциональность:
Приложение предоставляет следующие возможности:

- **Добавление новой заметки**: Пользователь может ввести заголовок и содержание заметки, которые будут сохранены в базе данных.
    
- **Просмотр списка всех заметок**: Приложение отображает список всех заметок с их заголовками. Пользователь может выбрать заметку из списка для просмотра подробной информации.
    
- **Поиск заметки**: Пользователь может ввести ключевое слово или фразу для поиска заметок, содержащих данное слово или фразу в заголовке или содержании.
    
- **Удаление заметки**: Пользователь может выбрать заметку из списка и удалить ее из базы данных.

## Структура проекта:
Проект разделен на несколько модулей:

- **app.py**: Главный модуль приложения, запускающий инициализацию базы данных и основное меню.
    
- **controllers.py**: Модуль, содержащий функции для обработки бизнес-логики, такой как добавление, получение, поиск и удаление заметок.
    
- **database.py**: Модуль, предоставляющий функции для взаимодействия с базой данных SQLite.
    
- **models.py**: Модуль, определяющий структуру данных Note, которая представляет собой заметку.
    
- **views.py**: Модуль, отвечающий за отображение интерфейса пользователя.

## Технологии:
- **Python**: Язык программирования, на котором написан наш менеджер заметок.
    
- **SQLite**: База данных для хранения заметок.

### Использование

1. **Убедитесь, что Python 3 установлен.** Откройте командную строку и введите: *python --version*.  Если Python не установлен, скачайте его с [https://www.python.org/downloads/](https://www.python.org/downloads/).
    
2. **Создайте папку notes_manager и поместите в неё файлы проекта.**
    
3. **Откройте командную строку в этой папке.**
    
    - **Windows:** Откройте папку в проводнике, нажмите правой кнопкой мыши на пустом месте, удерживая Shift, и выберите "Открыть окно PowerShell здесь".
        
    - **macOS:** Откройте папку в Finder, нажмите правой кнопкой мыши на пустом месте и выберите "Новая терминальная вкладка".
        

4. **Запустите приложение:** Введите *py app.py* и нажмите Enter.


	**Следуйте инструкциям на экране, чтобы добавлять, просматривать, искать и удалять заметки.
   	Для выхода из приложения выберите опцию "Выход" в главном меню.**
