import time
import allure
from selenium import webdriver

from pages.cart_onliner_by_order import Cart_onliner_by_order
from pages.catalog_onliner_by import Catalog_onliner_by
from pages.catalog_onliner_by_notebook import Catalog_onliner_by_notebook
from pages.catalog_onliner_by_notebook_asus_g733zxkh036w import Igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W
from pages.onliner_by import Onliner_by


"""End to End test"""
@allure.description("Test dymovoye testirovaniye dlya oformleniya zakaza")
def test_dymovoye_testirovaniye_dlya_oformleniya_zakaza(set_up, set_group):
    driver = webdriver.Chrome(executable_path="C:\\Users\\qwerty\\PycharmProjects\\resource\\chromedriver.exe")
    driver.maximize_window()

    check_catalog = Onliner_by(driver)
    check_catalog.go_to_catalog()

    transition_computers_and_networks = Catalog_onliner_by(driver)
    transition_computers_and_networks.go_to_computers_and_networks()

    transition_choice_of_laptop = Catalog_onliner_by_notebook(driver)
    transition_choice_of_laptop.choice_of_laptop()

    transition_buy_product = Igrovoy_noutbuk_ASUS_ROG_Strix_SCAR_17_G733ZX_KH036W(driver)
    transition_buy_product.buy_product()

    entering_personal_data = Cart_onliner_by_order(driver)
    entering_personal_data.oformleniye_zakaza()

    time.sleep(5)









