import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.readconfiguration import read_configuration


def test_login(setup):
    driver = setup
    url = read_configuration("basic info","url")
    login_xpath = read_configuration("xpath",'login_btn')
    driver.implicitly_wait(15)
    driver.get(url)
    #time.sleep(10)
    driver.find_element(By.XPATH,login_xpath).click()
    username_xpath = read_configuration("xpath","username")
    username = read_configuration("login","username")
    pass_xpath = read_configuration("xpath","pass")
    password = read_configuration("login","pass")

    wait = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located((By.XPATH,username_xpath))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.XPATH,pass_xpath))).send_keys(password)
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
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
    driver.save_screenshot(r"C:\Users\ADMIN\PycharmProjects\PythonProject\Screenshot\updated.png")
    wait.until(EC.visibility_of_element_located((By.XPATH,"//textarea[@id='resumeHeadlineTxt']"))).send_keys(".")
    wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Save']"))).click()
    time.sleep(10)



