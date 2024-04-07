from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    def __init__ (self, driver):
        self.driver = driver

    #XPATHS
    SEARCH_FIELD = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.XPATH,'/html/body/div/main/article/div[1]/div[1]/div[2]/div/header/div/section[2]/form/div/div/button[2]')

    def enter_search_query(self, query):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(query)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
