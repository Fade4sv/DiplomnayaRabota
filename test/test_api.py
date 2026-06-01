from tools.ClassApi import TodoistStore
import allure
api_store = TodoistStore()


@allure.feature("Авторизация")
@allure.title("Проверка успешной авторизации пользователя")
def test_authorization():
    response = api_store.check_authorization(api_store.token)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.feature("Управление задачами")
@allure.title("Получение списка задач на сегодня")
def test_get_today_tasks():
    response = api_store.get_today_tasks()
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.feature("Управление задачами")
@allure.title("Успешное добавление и последующее удаление задачи")
def test_add_task():
    task_name = "Дипломная задача по автоматизации"
    response = api_store.add_task(task_name)
    with allure.step("Проверка успешного создания задачи"):
        assert response.status_code == 200
    created_id = response.json().get("id")
    delete_response = api_store.delete_task(created_id)
    with allure.step("Проверка успешного удаления задачи"):
        assert delete_response.status_code == 204


@allure.feature("Проекты")
@allure.title("Получение списка всех проектов")
def test_get_my_projects():
    response = api_store.get_projects()
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200


@allure.feature("Управление задачами")
@allure.title("Изменение названия существующей задачи")
def test_update_task_name():
    setup_response = api_store.add_task("Старое название")
    task_id = setup_response.json().get("id")
    update_response = api_store.update_task_name(task_id, "Новое название")
    with allure.step("Проверка статус-кода обновления и измененного контента"):
        assert update_response.status_code == 200
        assert update_response.json().get("content") == "Новое название"
    delete_response = api_store.delete_task(task_id)
    with allure.step("Проверка удаления измененной задачи"):
        assert delete_response.status_code == 204
