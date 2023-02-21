import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

page_title = "Hitachi Solutions"
search_result_text = "Search results for"
searched_page_title = "Revolutionize your Customer Insights with Microsoft's Connected Ecosystem"


@pytest.fixture()
def search_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://global.hitachi-solutions.com/")
    return driver


def test_successful_navigation_to_site(search_page):
    title = search_page.find_element(By.CLASS_NAME, "homepage-headline").text
    assert title.__contains__(page_title)
    search_page.close()


def test_search_keywords(search_page):
    search_page.find_element(By.ID, "open-global-search").click()
    time.sleep(3)
    search_page.find_element(By.NAME, "s").send_keys("Microsoft")
    search_page.find_element(By.XPATH, '//*[@id="global-site-search"]/form/button').send_keys(Keys.ENTER)
    search_result = search_page.find_element(By.CLASS_NAME, "results").text
    assert search_result.__contains__(search_result_text)
    search_page.close()


def test_search_keywords_with_no_result(search_page):
    search_page.find_element(By.ID, "open-global-search").click()
    time.sleep(3)
    search_page.find_element(By.NAME, "s").send_keys("Rupali")
    search_page.find_element(By.XPATH, '//*[@id="global-site-search"]/form/button').send_keys(Keys.ENTER)
    search_result = search_page.find_element(By.CLASS_NAME, "results").text
    assert not search_result.__contains__(search_result_text)
    search_page.close()


def test_open_search_result(search_page):
    search_page.find_element(By.ID, "open-global-search").click()
    time.sleep(3)
    search_page.find_element(By.NAME, "s").send_keys("Microsoft")
    search_page.find_element(By.XPATH, '//*[@id="global-site-search"]/form/button').send_keys(Keys.ENTER)
    search_page.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/p/a').click()
    current_page_title = search_page.find_element(By.CLASS_NAME, "resource-title").text
    time.sleep(3)
    assert searched_page_title == current_page_title
    search_page.close()
