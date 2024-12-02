from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        # сохраняет ссылку на объект страницы для использования в методах класса
        self.page = page
        # инициализируют локаторы для элементов страницы
        self.profile = page.locator('#usernameDisplay')
        self.logout = page.locator('#logout')

    def assert_welcome_message(self, message):
        #проверяет текст приветственного сообщения на панели управления
        expect(self.profile).to_have_text(message)