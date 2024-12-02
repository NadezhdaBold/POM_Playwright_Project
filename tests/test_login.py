import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с недействительными учетными данными')
def test_login_failure(page):
    #создаем объект LoginPage, который представляет страницу входа
    login_page = LoginPage(page)
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    # переход на страницу авторизации
    login_page.navigate()
    # заполнение полей логина и пароля верными учетными данными
    login_page.login('admin', 'admin')
    #проверка, что на странице отображается корректное приветственное сообщение
    dashboard_page.assert_welcome_message("Welcome admin")


@pytest.mark.parametrize('username, password', [
        ('user', 'user'),
        ('admin', 'admin')
    ]) #задали нескольких наборов данных
#тест запускается для каждой пары username и password
def test_login_success(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    # переход на страницу авторизации
    login_page.navigate()
    #подставляет значение параметров username и password
    login_page.login(username, password)
    #проверка, что на странице отображается корректное приветственное сообщение
    dashboard_page.assert_welcome_message(f"Welcome {username}")

def test_login_failure_fixture(login_page):
    login_page.navigate()
    login_page.login('user', 'password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success_fixture(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")