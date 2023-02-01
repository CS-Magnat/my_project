import re
import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    """Создание метода для проверки значения сумм на страницах(указаны ниже)"""
    def assert_price(self, word, result):
        value_word = word.text
        """На разных страницах в различных вариациях подтягиваются ценники, где-то есть буквы, где-то нету, по этой причине производим ниже прописанные действия"""
        removing_spaces = value_word.replace(" ", "")  # удаляем пробелы
        delete_unnecessary = re.findall("([0-9]+[,]+[0-9]+)", removing_spaces)  # выводим в Массив только цифры и запятые
        price = "".join(delete_unnecessary)  # преобразуем Список в строку
        print(price)
        print(result)
        assert price == result
        print("Цена на странице верна")

    """Проверка урлов"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        print(get_url)
        print(result)
        assert get_url == result
        print("Url-ы совпали")

        """Создание метода для использования скринов"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\qwerty\\PycharmProjects\\my_project\\screens\\' + name_screenshot)