import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UIStore:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'https://app.todoist.com/'

    @allure.step("Авторизация пользователя {login} в системе")
    def login(self, login, password):
        self.driver.get(self.base_url + 'auth/login')
        waiter = WebDriverWait(self.driver, 5)
        waiter.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '[id="element-0"]'))
        )
        with allure.step("Ввод логина и пароля"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[id="element-0"]').send_keys(login)
            self.driver.find_element(
                By.CSS_SELECTOR, '[id="element-2"]').send_keys(password)
        with allure.step("Нажатие кнопки 'Войти'"):
            self.driver.find_element(
                By.CSS_SELECTOR, '._7ea1378e._2d084671').click()
        with allure.step("Ожидание перенаправления в личный кабинет"):
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.base_url + 'app/inbox')
            )

    @allure.step("Переход на страницу меток и получение текста при отсутствии меток")
    def check_text_empty_mark(self):
        self.driver.get(self.base_url + 'app/filters-labels')
        empty_mark = self.driver.find_element(
            By.XPATH, '//div[text()="Место для ваших меток."]').text
        return empty_mark

    @allure.step("Получение цвета кнопки 'Добавить задачу' из бокового меню")
    def get_color_button_add_task_from_side_menu(self):
        self.driver.get(self.base_url + 'app/today')
        color = self.driver.find_element(
            By.XPATH, '//span[text()="Добавить задачу"]')
        return color.value_of_css_property('border-bottom-color')

    @allure.step("Проверка цвета активного чекбокса на странице проекта")
    def check_color_checkbox_on_active(self):
        self.driver.get(self.base_url + 'app/projects/active')
        with allure.step("Клик по элементу для активации чекбокса"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[class="bae487be _19abae45 a7c6de33 _194d8611 _8ad6a17c"]').click()
        with allure.step("Ожидание обновления URL"):
            waiter = WebDriverWait(self.driver, 10)
            waiter.until(
                EC.url_to_be(self.base_url + 'app/projects/archived')
            )
        color = self.driver.find_element(
            By.CSS_SELECTOR, '[class="_5af09fb5 _19abae45 d7c72ae2 _7fb159a0 b85e3dfa b834b77e _73d1ede9"]')
        return color.value_of_css_property('background-color')
    
    @allure.step("Получение подсказки (placeholder) при создании новой задачи")
    def check_clue_on_add_task(self):
        with allure.step("Переход на страницу 'Сегодня'"):
            self.driver.get(self.base_url + 'app/today')
        with allure.step("Нажатие на кнопку добавления задачи"):
            self.driver.find_element(
                By.CSS_SELECTOR, '[class="_19abae45 _56a651f6 _3930afa0 _7ea1378e _7246d092"]').click()
        with allure.step("Поиск элемента текстового редактора задачи"):
            clue = self.driver.find_element(
                By.CSS_SELECTOR, 'p[class="is-empty is-editor-empty"]')
        with allure.step("Чтение значения атрибута 'data-placeholder'"):
            return clue.get_attribute('data-placeholder')

    @allure.step("Закрытие сессии браузера")
    def quit(self):
        self.driver.quit()
