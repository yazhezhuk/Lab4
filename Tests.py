from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Tests(TestCase):
    def test_search(self):
        search_request = "RTX3090"
        url = 'https://exe.ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element(by=By.ID, value='search_query').send_keys(search_request)
        browser.find_element(by=By.ID, value='search_query').send_keys(Keys.ENTER)

        actual_result = browser.find_element(by=By.CLASS_NAME, value='product').text

        assert actual_result != ""

        browser.close()

    def test_category(self):
        search_text = "Samsung Galaxy"
        expected_category = "Смартфони, Телефони"
        url = 'https://hotline.ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())

        browser.get(url)

        browser.find_element(by=By.XPATH, value='/html/body/div[1]/header/div[2]/div/div/div[2]/form/input').send_keys(
            search_text)
        browser.find_element(by=By.XPATH, value='/html/body/div[1]/header/div[2]/div/div/div[2]/form/input').send_keys(
            Keys.ENTER)

        browser.implicitly_wait(10)

        selector = "#__layout > div > div.search.container > div.flex.top-xs > " \
                   "div.search-sidebar.search__sidebar.hidden-below-xl > div:nth-child(1) > div:nth-child(1) > " \
                   "div.search-sidebar-section__header.flex.middle-xs > div > b "
        actual_category = self.retryingFindClick(selector ,browser)

        assert expected_category == actual_category
        browser.close()

    def retryingFindClick(self, by, driver):
        result = False
        text = ""
        while text == "":
            try:
                text = driver.find_element(By.CSS_SELECTOR,value=by).text
                break
            except():
                continue
        return text
