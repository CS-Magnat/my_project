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

        # отел сделать одну итоговую проверку в cart_online_order.py, но у меня не получилось передать туда переменные с суммами
        # def assert_price(self, word_1, wornd_2, word_3, result):
        #     value_word_1 = word_1.text
        #     value_word_2 = word_2.text
        #     value_word_3 = word_3.text
        #
        #     """На разных страницах в различных вариациях подтягиваются ценники, где-то есть буквы, где-то нету, по этой причине производим ниже прописанные действия"""
        #     removing_spaces_1 = value_word_1.replace(" ", "")  # удаляем пробелы
        #     removing_spaces_2 = value_word_2.replace(" ", "")  # удаляем пробелы
        #     removing_spaces_3 = value_word_3.replace(" ", "")  # удаляем пробелы
        #
        #     delete_unnecessary_1 = re.findall("([0-9]+[,]+[0-9]+)", removing_spaces_1)  # выводим в Массив только цифры и запятые
        #     delete_unnecessary_2 = re.findall("([0-9]+[,]+[0-9]+)", removing_spaces_2)  # выводим в Массив только цифры и запятые
        #     delete_unnecessary_3 = re.findall("([0-9]+[,]+[0-9]+)", removing_spaces_3)  # выводим в Массив только цифры и запятые
        #
        #     price_1 = "".join(delete_unnecessary_1)  # преобразуем Список в строку
        #     price_2 = "".join(delete_unnecessary_2)  # преобразуем Список в строку
        #     price_3 = "".join(delete_unnecessary_3)  # преобразуем Список в строку
        #
        #     assert price_1 == price_2 == price_3 == result
        #     print("Цена на страницах верна")




