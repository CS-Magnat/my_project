import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_classs import Base
from utilites.logger import Logger


class Catalog_onliner_by_notebook(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Определяем локаторы на странице"""
    schema_filter_checkbox_asus = "//*[@id='schema-filter']/div[5]/div[4]/div[2]/ul/li[2]/label/span[2]"
    schema_filter_checkbox_2022 = "//*[@id='schema-filter']/div[5]/div[9]/div[3]/ul/li[1]/label/span[2]"
    schema_filter_checkbox_intel_core_i9 = "//*[@id='schema-filter']/div[5]/div[11]/div[3]/ul/li[4]/label/span[2]"
    igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W = "//img[@alt='ASUS ROG Strix SCAR 17 G733ZX-KH036W']"
    price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W = "//a[@href='https://catalog.onliner.by/notebook/asus/g733zxkh036w/prices']"


    """Ищем элементы на странице"""
    """Ищем в фильтре Asus"""
    def get_schema_filter_checkbox_asus(self):
        print("Элемент Asus в фильтре на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.schema_filter_checkbox_asus)))

    """Ищем в фильтре 2022 год"""
    def get_schema_filter_checkbox_2022(self):
        print("Элемент 2022 год в фильтре на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.schema_filter_checkbox_2022)))

    """Ищем в фильтре Intel Core i9"""
    def get_schema_filter_checkbox_intel_core_i9(self):
        print("Элемент Intel Core i9 в фильтре на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.schema_filter_checkbox_intel_core_i9)))

    """Ищем в списке Игровой ноутбук ASUS ROG Strix SCAR 17 G733ZX-KH036W"""
    def get_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(self):
        print("Игровой ноутбук ASUS ROG Strix SCAR 17 G733ZX-KH036W на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W)))

    """Ищем цену Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W"""
    def get_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(self):
        print("Цена Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W на странице найдена")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W)))


    """Действия над элементами"""
    """Нажимаем на элемент Asus в фильтре"""
    def click_schema_filter_checkbox_asus(self):
        self.get_schema_filter_checkbox_asus().click()
        print("Нажатие на Asus в фильтре произошло успешно")

    """Нажимаем на элемент 2022 в фильтре"""
    def click_schema_filter_checkbox_2022(self):
        self.get_schema_filter_checkbox_2022().click()
        print("Нажатие на 2022 в фильтре произошло успешно")

    """Нажимаем на элемент Intel Core i9 в фильтре"""
    def click_schema_filter_checkbox_intel_core_i9(self):
        self.get_schema_filter_checkbox_intel_core_i9().click()
        print("Нажатие на элемент Intel Core i9 в фильтре произошло успешно")

    """Нажимаем на Игровой ноутбук ASUS ROG Strix SCAR 17 G733ZX-KH036W"""
    def click_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(self):
        self.get_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W().click()
        print("Нажатие на Игровой ноутбук ASUS ROG Strix SCAR 17 G733ZX-KH036W произошло успешно")


    """Действия на странице"""
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        print("Скролл произведене успешно")

    """Перемещение в самый низ страницы"""
    def PAGE_DOWN(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Страница была спущена в самый низ")

    # хотел дополнительно исgjльзовать возможность перемещения экрана, через автонаведение, но у меня не получилось это сделать
    # не получается праdbильно передавать/обращаться в переменным из функций
    # def hover_over_an_element(self):
    #     action = ActionChains(self.driver)
    #     action.move_to_element(self.get_schema_filter_checkbox_2022).perform()
    #     print("Экран визуально перемещен на фильтре 2022")


    """Методы, который непосредственно запускают последовательность выполнения комманд"""
    def choice_of_laptop(self):
        with allure.step("Сhoice of laptop"):
            Logger.add_start_step(method="choice_of_laptop")
            self.scroll() #не находит элемент, если не сместить страницу, хотя страница сама по себе не подгружается при скролле вниз, фильтр просто скрыт визуально за экраном
            self.get_schema_filter_checkbox_asus()
            self.click_schema_filter_checkbox_asus()

            # self.hover_over_an_element() #попытка автонаведения экрана

            self.get_schema_filter_checkbox_2022()
            self.click_schema_filter_checkbox_2022()

            self.PAGE_DOWN() #скролл после одного использования пересает работать, экран может немног просто дернуться,
            # пришлось юзать вот это, но если заюзать этот же метод в самом начале, перестает искать в фильтре асус)

            self.get_schema_filter_checkbox_intel_core_i9()
            self.click_schema_filter_checkbox_intel_core_i9()

            self.assert_price(self.get_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(), "10740,00") #локатор выводит разные ценники

            self.get_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W()
            self.click_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W()
            Logger.add_end_step(method="choice_of_laptop")






