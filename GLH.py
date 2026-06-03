import os
from dotenv import load_dotenv

load_dotenv()
base_url_UI = "https://app.todoist.com/"
base_url_API = "https://api.todoist.com/api/v1/"
# Конфиденциальные данные (загружаются из операционной системы / .env)
login = os.getenv("TODOIST_LOGIN")
password = os.getenv("TODOIST_PASSWORD")
token = os.getenv("TODOIST_TOKEN")

if not all([login, password, token]):
    raise ValueError(
        "Ошибка конфигурации: Проверьте, что файл .env создан в корне проекта "
        "и содержит переменные TODOIST_LOGIN, TODOIST_PASSWORD и TODOIST_TOKEN!"
    )
