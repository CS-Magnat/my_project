import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_classs import Base
from utilites.logger import Logger


class Cart_onliner_by_order(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Определяем локаторы на странице"""
    naselennyy_punkt = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/input"
    ulica = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div/div/div/div/div/input"
    dom = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[3]/div[2]/div/input"
    korpus = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[4]/div[2]/div/input"
    podyezd = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[6]/div[2]/div/input"
    etazh = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[7]/div[2]/div/input"
    kvartira = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[4]/div[8]/div[2]/div/input"
    kommentariy_k_adresu = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[2]/div/textarea"
    imya = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[9]/div[1]/div[2]/div/input"
    familiya = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[9]/div[2]/div[2]/div/input"
    e_mail = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[10]/div[1]/div[2]/div/input"
    telefon = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[10]/div[2]/div[3]/div[1]/div/div[1]/input"
    podtverdit_nomer = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[10]/div[2]/div[3]/div[1]/div/button"
    pereyti_k_sposobu_oplaty = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[5]/button"
    total_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W = "//*[@id='container']/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/span"


    """Ищем элементы на странице"""
    """Ищем элемент Населенный пункт"""
    def get_naselennyy_punkt(self):
        print("Элемент Населенный пункт на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.naselennyy_punkt)))
    """Ищем элемент Улица"""
    def get_ulica(self):
        print("Элемент Улица на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.ulica)))
    """Ищем элемент Дом"""
    def get_dom(self):
        print("Элемент Дом на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.dom)))
    """Ищем элемент Корп."""
    def get_korpus(self):
        print("Элемент Корп. на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.korpus)))
    """Ищем элемент Под."""
    def get_podyezd(self):
        print("Элемент Под. на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.podyezd)))
    """Ищем элемент Этаж"""
    def get_etazh(self):
        print("Элемент Этаж на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.etazh)))
    """Ищем элемент Квартира"""
    def get_kvartira(self):
        print("Элемент Квартира на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.kvartira)))
    """Ищем элемент Комментарий к адресу"""
    def get_kommentariy_k_adresu(self):
        print("Элемент Комментарий к адресу на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.kommentariy_k_adresu)))
    """Ищем элемент Имя"""
    def get_imya(self):
        print("Элемент Имя на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.imya)))
    """Ищем элемент Фамилия"""
    def get_familiya(self):
        print("Элемент Фамилия на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.familiya)))
    """Ищем элемент E-mail"""
    def get_e_mail(self):
        print("Элемент E-mail на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.e_mail)))
    """Ищем элемент Телефон"""
    def get_telefon(self):
        print("Элемент Телефон на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.telefon)))

    """Ищем элемент Подтвердить номер"""
    def get_podtverdit_nomer(self):
        print("Элемент Подтвердить номер на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.podtverdit_nomer)))
    """Ищем элемент Перейти к способу оплаты"""
    def get_pereyti_k_sposobu_oplaty(self):
        print("Элемент Перейти к способу оплаты на странице найден")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.pereyti_k_sposobu_oplaty)))

    """Ищем итоговую цену Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W"""
    def get_total_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(self):
        print("Итоговая цена Игрового ноутбука ASUS ROG Strix SCAR 17 G733ZX-KH036W на странице найдена")
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.total_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W)))


    """Действия над элементами"""
    """Отправить текст в поле Населенный пункт"""
    def send_naselennyy_punkt(self):
        self.get_naselennyy_punkt().send_keys("")
        print("Текст в поле Населенный пункт отправлен успешно")
    """Отправить текст в поле Улица"""
    def send_ulica(self):
        self.get_ulica().send_keys("Независимости")
        print("Текст в поле Улица отправлен успешно")
    """Отправить текст в поле Дом"""
    def send_dom(self):
        self.get_dom().send_keys("10")
        print("Текст в поле Дом отправлен успешно")
    """Отправить текст в поле Корп."""
    def send_korpus(self):
        self.get_korpus().send_keys("10")
        print("Текст в поле Корп. отправлен успешно")
    """Отправить текст в поле Под."""
    def send_podyezd(self):
        self.get_podyezd().send_keys("2")
        print("Текст в поле Под. отправлен успешно")
    """Отправить текст в поле Этаж"""
    def send_etazh(self):
        self.get_etazh().send_keys("2")
        print("Текст в поле Этаж отправлен успешно")
    """Отправить текст в поле Квартира"""
    def send_kvartira(self):
        self.get_kvartira().send_keys("7")
        print("Текст в поле Квартира отправлен успешно")
    """Отправить текст в поле Комментарий к адресу"""
    def send_kommentariy_k_adresu(self):
        self.get_kommentariy_k_adresu().send_keys("EEEEEE BoooooY")
        print("Текст в поле Комментарий к адресу отправлен успешно")
    """Отправить текст в поле Имя"""
    def send_imya(self):
        self.get_imya().send_keys("Johnny")
        print("Текст в поле Имя отправлен успешно")
    """Отправить текст в поле Фамилия"""
    def send_familiya(self):
        self.get_familiya().send_keys("Cage")
        print("Текст в поле Фамилия отправлен успешно")
    """Отправить текст в поле E-mail"""
    def send_e_mail(self):
        self.get_e_mail().send_keys("test@yandex.ru")
        print("Текст в поле E-mail отправлен успешно")
    """Отправить текст в поле Телефон"""
    def send_telefon(self):
        self.get_telefon().send_keys("000000000")
        print("Текст в поле Телефон отправлен успешно")

    """Нажатия"""
    """Нажимаем Подтвердить номер"""
    def click_podtverdit_nomer(self):
        self.get_podtverdit_nomer().click()
        print("Нажатие на Подтвердить номер произошло успешно")


    """Методы, который непосредственно запускают последовательность выполнения комманд"""
    def oformleniye_zakaza(self):
        with allure.step("Oformleniye zakaza"):
            Logger.add_start_step(method="oformleniye_zakaza")

            self.assert_price(self.get_total_price_igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(), "10740,00")
            self.assert_url("https://cart.onliner.by/order") #если указать данную проверку перед проверкой цены, селениум подтягивает url предыдущей страницы,
            #возможно перед тем, как распознавать url на странице, надо что-нибудь на ней сделать

            self.get_naselennyy_punkt()
            self.send_naselennyy_punkt()
            self.get_ulica()
            self.send_ulica()
            self.get_dom()
            self.send_dom()
            self.get_korpus()
            self.send_korpus()
            self.get_podyezd()
            self.send_podyezd()
            self.get_etazh()
            self.send_etazh()
            self.get_kvartira()
            self.send_kvartira()
            self.get_kommentariy_k_adresu()
            self.send_kommentariy_k_adresu()
            self.get_imya()
            self.send_imya()
            self.get_familiya()
            self.send_familiya()
            self.get_e_mail()
            self.send_e_mail()
            self.get_telefon()
            self.send_telefon()

            self.get_podtverdit_nomer()
            self.click_podtverdit_nomer()
            self.get_screenshot()
            Logger.add_end_step(method="oformleniye_zakaza")


