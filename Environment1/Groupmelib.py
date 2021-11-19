# Other Imports
import time
from dataclasses import dataclass

# selenium imports
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

def select_element(method, flag):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((method, flag)))


# Use Chrome Browser
driver = webdriver.Chrome()
class Groupme:
    def Login(self, phone_number, password, chat):
        driver.get('https://groupme.com/en-US/')
        login_button1 = select_element(By.CSS_SELECTOR, "a[class = 'login button gray']")
        login_button1.click()
        # Enter the credentials
        gm_username = select_element(By.CSS_SELECTOR, "input[id = 'signinUserNameInput']")
        gm_password = select_element(By.CSS_SELECTOR, "input[id = 'signinPasswordInput']")
        gm_username.clear()
        gm_password.clear()
        gm_username.send_keys(phone_number)
        gm_password.send_keys(password)
        gm_login_button = select_element(By.XPATH, '//*[@id="signin"]/div/form/button')
        gm_login_button.click()
        time.sleep(2)
        chat_room = select_element(By.CSS_SELECTOR, "button[aria-label = 'Chat Snug Harbor Jewelry Inc. 1 And 2']")
        chat_room.click()
        input('Complete the Two-Factor Authentication, then press any key to continue')



