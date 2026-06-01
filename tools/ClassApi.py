import requests
import allure
from GLH import base_api, token


class TodoistStore:

    def __init__(self, base_api=base_api, token=token):
        self.base_api = base_api
        self.token = token

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    @allure.step("Проверка авторизации с токеном: {api_token}")
    def check_authorization(self, api_token):
        url = self.base_api + "projects"
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.get(url, headers=headers)
        self.token = api_token
        return response

    @allure.step("Получение задач на сегодня")
    def get_today_tasks(self):
        url = self.base_api + "tasks"
        params = {"filter": "today"}
        return requests.get(url, headers=self._get_headers(), params=params)

    @allure.step("Добавление новой задачи: '{task_name}'")
    def add_task(self, task_name):
        url = self.base_api + "tasks"
        payload = {"content": task_name}
        return requests.post(url, headers=self._get_headers(), json=payload)

    @allure.step("Получение списка проектов")
    def get_projects(self):
        url = self.base_api + "projects"
        return requests.get(url, headers=self._get_headers())

    @allure.step("Обновление имени задачи (ID: {task_id}) на '{new_name}'")
    def update_task_name(self, task_id, new_name):
        url = f"{self.base_api}tasks/{task_id}"
        payload = {"content": new_name}
        return requests.post(url, headers=self._get_headers(), json=payload)

    @allure.step("Удаление задачи (ID: {task_id})")
    def delete_task(self, task_id):
        url = f"{self.base_api}tasks/{task_id}"
        return requests.delete(url, headers=self._get_headers())
