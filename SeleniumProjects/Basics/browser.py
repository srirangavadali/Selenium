


def test_eight_components():


    driver.get("https://google.com")

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    print(value)
    assert value == "Selenium"

    #driver.quit()
    driver.get("https://www.facebook.com/")
    fb_email_box = driver.find_element(by=By.NAME, value="email")
    fb_pass_box = driver.find_element(by=By.NAME, value="pass")
    fb_login_button = driver.find_element(by=By.NAME, value="login")

    fb_email_box.send_keys("rangaa1995@yahoo.com")
    fb_pass_box.send_keys("8686258631rfrf")
    fb_login_button.click()

test_eight_components()
