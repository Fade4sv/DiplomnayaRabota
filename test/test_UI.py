import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tools.ClassUI import UIStore
import allure
from GLH import login, password


@allure.feature("Авторизация")
@allure.title("Успешный вход пользователя в систему")
def test_login(driver, login=login, password=password):
    ui_store = UIStore(driver)
    ui_store.login(login, password)


@allure.feature("Метки")
@allure.title("Проверка текста-подсказки для пустого списка меток")
def test_check_text_empty_mark(driver):
    ui_store = UIStore(driver)
    empty_mark = ui_store.check_text_empty_mark()
    with allure.step("Проверка совпадения текста подсказки"):
        assert empty_mark == "Место для ваших меток."


@allure.feature("Интерфейс и стили")
@allure.title("Проверка цвета кнопки добавления задачи в боковом меню")
def test_color_button_add_task_from_side_menu(driver):
    ui_store = UIStore(driver)
    color = ui_store.get_color_button_add_task_from_side_menu()
    with allure.step("Проверка RGBA-цвета кнопки"):
        assert color == "rgba(211, 51, 34, 1)"


@allure.feature("Интерфейс и стили")
@allure.title("Проверка цвета активного чекбокса")
def test_color_checkbox_on_active(driver):
    ui_store = UIStore(driver)
    color = ui_store.check_color_checkbox_on_active()
    with allure.step("Проверка RGBA-цвета чекбокса"):
        assert color == "rgba(211, 51, 34, 1)"


@allure.feature("Управление задачами")
@allure.title("Проверка наличия подсказки (placeholder) при создании задачи")
def test_clue_on_add_command(driver):
    ui_store = UIStore(driver)
    clue = ui_store.check_clue_on_add_task()
    with allure.step("Проверка, что строка подсказки не пустая"):
        assert len(clue) > 0


@allure.feature("Авторизация")
@allure.title("Выход из учетной записи и закрытие браузера")
def test_quit(driver):
    ui_store = UIStore(driver)
    ui_store.quit()
