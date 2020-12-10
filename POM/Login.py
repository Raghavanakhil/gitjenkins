from selenium import webdriver
from selenium.webdriver.common.by import By


class loginCredentials:
    username = (By.XPATH, "//input[@type='email']")
    password = (By.ID, "Password")
    submit = (By.XPATH, "//input[@type='submit']")
    Checkboxs = (By.XPATH,"//input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def Username(self):
        return self.driver.find_element(*loginCredentials.username)

    def Password(self):
        return self.driver.find_element(*loginCredentials.password)

    def Login(self):
        return self.driver.find_element(*loginCredentials.submit)

    def Checkbox(self):
        return self.driver.find_element(*loginCredentials.Checkboxs)



