from selenium import webdriver
from selenium.webdriver.common.by import By
class Subcategory:

    categoryMenu = (By.XPATH, "//ul[@class='sidebar-menu tree']/li[2]")
    categorysubmenu = (By.XPATH, "/html/body/div[3]/div[2]/div/ul/li[2]/ul/li[2]/a/span")
    swipe = (By.XPATH, "//div[@class='onoffswitch']/label")
    addNew = (By.XPATH,"/html/body/div[3]/div[3]/div/div[1]/div/a")

    def __init__(self,driver):

        self.driver = driver

    def MainMenu(self):
        return self.driver.find_element(*Subcategory.categoryMenu)

    def Submenu(self):
        return self.driver.find_element(*Subcategory.categorysubmenu)

    def Swipe(self):
        return self.driver.find_element(*Subcategory.swipe)

    def Addnew(self):
        return self.driver.find_element(*Subcategory.addNew)




