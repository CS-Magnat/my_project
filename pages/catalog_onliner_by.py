from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_classs import Base

class Catalog_onliner_by(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Определяем локаторы на странице"""
    computers_and_networks = "//*[@id='container']/div/div/div/div/div[1]/ul/li[4]"
    noutbuki_kompyutery_monitory = "//*[@id='container']/div/div/div/div/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/div[1]"
    igrovyye_noutbuki = "//*[@id='container']/div/div/div/div/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/div[2]/div/a[2]"


    """Ищем элементы на странице"""
    """Ищем Компьютеры и сети"""
    def get_computers_and_networks(self):
        print("Элемент Компьютеры и сети на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.computers_and_networks)))

    """Ищем Ноутбуки, компьютеры, мониторы"""
    def get_noutbuki_kompyutery_monitory(self):
        print("Элемент Ноутбуки, компьютеры, мониторы на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.noutbuki_kompyutery_monitory)))

    """Ищем Игровые ноутбуки"""
    def get_igrovyye_noutbuki(self):
        print("Элемент Игровые ноутбуки на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.igrovyye_noutbuki)))


    """Действия над элементами"""
    """Нажимаем на элемент Компьютеры и сети"""
    def click_computers_and_networks(self):
        self.get_computers_and_networks().click()
        print("Нажатие на Компьютеры и сети произошло успешно")

    """Нажимаем на элемент Ноутбуки, компьютеры, мониторы"""
    def click_noutbuki_kompyutery_monitory(self):
        self.get_noutbuki_kompyutery_monitory().click()
        print("Нажатие на Ноутбуки, компьютеры, мониторы произошло успешно")

    """Нажимаем на элемент Игровые ноутбуки"""
    def click_igrovyye_noutbuki(self):
        self.get_igrovyye_noutbuki().click()
        print("Нажатие на элемент Игровые ноутбуки произошло успешно")


    """Методы, который непосредственно запускают последовательность выполнения комманд"""
    def go_to_computers_and_networks(self):
        self.get_computers_and_networks()
        self.click_computers_and_networks()
        self.get_noutbuki_kompyutery_monitory()
        self.click_noutbuki_kompyutery_monitory()
        self.get_igrovyye_noutbuki()
        self.click_igrovyye_noutbuki()


