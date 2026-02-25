import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()



    yield driver

    driver.implicitly_wait(15)
    driver.find_element(By.XPATH,"//img[@class='nI-gNb-icon-img']").click()
    driver.find_element(By.XPATH,"//a[@title='Logout']").click()
    driver.quit()
