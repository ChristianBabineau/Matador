import pytest
import yaml
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
with open(os.path.abspath('config.yaml'), 'r') as stream:
    try:
        config = yaml.safe_load(stream)
        print(config)
    except yaml.YAMLError as e:
        print(e)
PACKAGEPATH = config['package-path']
CHROMEDRIVERPATH = config['driver-path']

sys.path.append(PACKAGEPATH)

from pages.homePage import HomePage
from pages.searchResultsPage import SearchResultsPage

service = Service(CHROMEDRIVERPATH)
driver = webdriver.Chrome(service=service)

HomePage = HomePage(driver)
SearchResultsPage = SearchResultsPage(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        screenshot_name = f"screenshot_{item.name}.png"
        driver.get_screenshot_as_file(screenshot_name)

def test_ImageFromSpecificSite():
    performSearch()
    urls = SearchResultsPage.getImageURLs()
    targetURL = 'wallpapercave.com'
    containsTargetUrl = lambda urls, text: any(text in url for url in urls)
    try:
        assert containsTargetUrl(urls, targetURL)
    finally:
        screenshot_name = f"screenshot_{test_ImageFromSpecificSite.__name__}.png"
        driver.get_screenshot_as_file(screenshot_name)


def test_TitleHasWord():
    performSearch()
    titles= SearchResultsPage.getTitles()
    targetText = 'car'
    containsTargetWord = lambda titles: any(targetText in title.lower() for title in titles)
    try:
        assert containsTargetWord(titles)
    finally:
        screenshot_name = f"screenshot_{test_TitleHasWord.__name__}.png"
        driver.get_screenshot_as_file(screenshot_name)

def performSearch():
    driver.get('https://duckduckgo.com/')
    HomePage.enter_search_query("nice cars image")
    HomePage.click_search_button()