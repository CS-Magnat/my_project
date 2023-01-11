import allure

from base.base_classs import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilites.logger import Logger


class Igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Определяем локаторы на странице"""
    price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W = "//*[@id='container']/div/div/div/div/div[2]/div[1]/main/div/div/div[1]/div[2]/div[5]/div[1]/div/a"
    kupit_seychas = "//*[@id='container']/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[3]/div[1]/div[1]/div[3]/a[1]"


    """Ищем элементы на странице"""
    """Ищем элемент Купить сейчас"""
    def get_buy_it_now(self):
        print("Элемент Купить сейчас на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.kupit_seychas)))

    """Ищем цену Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W"""
    def get_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(self):
        print("Цена Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W на странице найдена")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W)))


    """Действия над элементами"""
    """Нажимаем на Купить сейчас"""
    def click_buy_it_now(self):
        self.get_buy_it_now().click()
        print("Нажатие на Купить сейчас произошло успешно")


    """Методы, который непосредственно запускают последовательность выполнения комманд"""
    def buy_product(self):
        with allure.step("Buy product"):
            Logger.add_start_step(method="buy_product")
            self.assert_price(self.get_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(), "11350,00")
            self.get_buy_it_now()
            self.click_buy_it_now()
            Logger.add_end_step(method="buy_product")

