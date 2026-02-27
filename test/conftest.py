import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.readconfiguration import read_configuration


@pytest.fixture()
def setup():
    browser = read_configuration("basic info",'browser')
    opt = Options()
    pref = {
        "credentials_enable_service":False,
        "profile.password_manager_service":False,
        "profile.password_manager_leak_detection":False
    }
    opt.add_experimental_option("prefs",pref)
    url = read_configuration("basic info","url")
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\PythonProject\screenshots\url_load.png")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='login_Layer']"))).click()
        #driver.find_element(By.XPATH,login_xpath).click()
        username_xpath = read_configuration("xpath","username")
        username = read_configuration("login","username")
        pass_xpath = read_configuration("xpath","pass")
        password = read_configuration("login","pass")


        wait.until(EC.visibility_of_element_located((By.XPATH,username_xpath))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.XPATH,pass_xpath))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Login']"))).click()

    yield driver

    driver.implicitly_wait(15)
    driver.find_element(By.XPATH,"//img[@class='nI-gNb-icon-img']").click()
    driver.find_element(By.XPATH,"//a[@title='Logout']").click()
    time.sleep(10)
    driver.quit()
