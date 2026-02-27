import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.readconfiguration import read_configuration


def test_login(setup):
    driver = setup

    login_xpath = read_configuration("xpath",'login_btn')
    driver.implicitly_wait(15)
    wait = WebDriverWait(driver,10)

    time.sleep(10)

    #driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(10)

    title = driver.find_element(By.XPATH,"//div[@class='info__heading']").text
    print(title)


    #if title.__eq__("NIKHIL GANESH PATIL"):

    wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='view-profile-wrapper']//child::a"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Resume headline']//following-sibling::span"))).click()

    driver.find_element(By.XPATH,"//textarea[@id='resumeHeadlineTxt']").click()

    actions = ActionChains(driver)
    actions.key_down(Keys.END).perform()
    actions.key_down(Keys.BACKSPACE).perform()
    driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\PythonProject\screenshots\updated.png")
    #driver.save_screenshot()
    wait.until(EC.visibility_of_element_located((By.XPATH,"//textarea[@id='resumeHeadlineTxt']"))).send_keys(".")
    wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Save']"))).click()
    time.sleep(10)
    driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\PythonProject\screenshots\profile_updated.png")
    driver.find_element(By.XPATH,"//div[contains(@class,'profileUpdatedProLayer')]//child::span[normalize-space()='CrossLayer']").click()

    time.sleep(10)

def test_share_interest(setup):
    driver = setup
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH,"//a[starts-with(@class,'spc__view')]").click()
    driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\PythonProject\screenshots\share_interest.png")
    time.sleep(2)
    wait = WebDriverWait(driver,15)
    time.sleep(15)
    share_interest = driver.find_elements(By.XPATH,"//button[normalize-space()='Share interest']")

    print(len(share_interest))
    #wait.until(EC.visibility_of_element_located((By.XPATH,"Share interest")))
    count = 0
    for i in range(len(share_interest)):
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Share interest']"))).click()
        driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\PythonProject\screenshots\shared_clicked.png")
        time.sleep(2)
        driver.back()
        time.sleep(2)

        count+=1
        if count ==5:
            break


    time.sleep(15)
