from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_classs import Base

class Onliner_by(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.onliner.by/"

    """Определяем локаторы на странице"""
    catalog = "//*[@id='container']/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[2]/span"

    """Ищем элемент "Каталог" на странице"""
    def get_catalog(self):
        print("Элемент на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog)))

    """Действия над элементами"""
    def click_catalog(self):
        self.get_catalog().click()
        print("Нажатие на каталог произошло успешно")

    """Методы, который непосредственно запускают последовательность выполнения комманд"""
    def go_to_catalog(self):
        self.driver.get(self.url)
        self.get_catalog()
        self.click_catalog()
