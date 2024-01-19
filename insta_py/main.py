from selenium import webdriver
from info import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time


class Instagram:
    driver_path = "C:\Chrome\chromedriver"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.NAME, 'username')
        passwordInput = self.browser.find_element(By.NAME, 'password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)
        self.browser.get("https://www.instagram.com/p/CrxsUQ0Ilg9/")
        time.sleep(3)

        if self.browser.find_element(By.CLASS_NAME, 'xs3hnx8'):
            for i in range(5):
                commentInput = self.browser.find_element(
                    By.CLASS_NAME, '_akhn')
                time.sleep(1)
                commentInput.find_element(By.TAG_NAME, 'textarea').click()
                time.sleep(1)
                userList = ['@burak_kasapoglu', '@esraaduman',
                            '@ahmetanilsanli', '@seliikoo', '@koralpkonurbay', '@gizzsimm']
                ulist = random.choice(userList)
                commentInput.find_element(
                    By.TAG_NAME, 'textarea').send_keys(ulist)
                time.sleep(1)
                commentInput.find_element(
                    By.TAG_NAME, 'textarea').send_keys(Keys.ENTER)
                time.sleep(5)
        time.sleep(1000)


app = Instagram(username, password)
app.signIn()
