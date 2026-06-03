import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """Фикстура инициализирует браузер один раз на всю тестовую сессию.

    scope='session' гарантирует, что один и тот же браузер пройдет по всем
    тестам по порядку (включая авторизацию), и закроется только в самом конце.
    """
    browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser_driver.implicitly_wait(10)

    yield browser_driver

    browser_driver.quit()
