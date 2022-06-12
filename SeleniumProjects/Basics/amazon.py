# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def amazon_test():
    driver.get("https://www.amazon.in/")
    title = driver.title
    print(title)

    amazon_search_box = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    amazon_search_box.send_keys("gluegun")


    driver.implicitly_wait(5)

    amazon_search_button = driver.find_element(by=By.ID, value="nav-search-submit-button")
    amazon_search_button.click()

    driver.back()
    driver.forward()
    driver.refresh()

    driver.quit()
amazon_test()

product_name = []
product_asin = []
product_price = []
product_ratings = []
product_ratings_num = []
product_link = []