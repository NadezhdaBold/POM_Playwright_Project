import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

#создает экземпляр LoginPage, который может быть использован в тестах
@pytest.fixture
def login_page(page):
    return LoginPage(page)

#создает экземпляр DashboardPage, который может быть использован в тестах
@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)