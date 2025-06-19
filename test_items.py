from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(30)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")