import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Запускает браузер и закрывает его после всех тестов"""
    with sync_playwright() as p:
        # Запускаем браузер
        browser = p.chromium.launch(headless=False)  # headless=False, чтобы видеть браузер
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Создает новую страницу для каждого теста"""
    # Создаем контекст - это как "окно" браузера
    context = browser.new_context(
        viewport={"width": 1366, "height": 768}  # Задаем размер окна
    )
    # Создаем страницу в этом контексте
    page = context.new_page()
    # Отдаем страницу тесту
    yield page
    # После теста закрываем контекст
    context.close()


