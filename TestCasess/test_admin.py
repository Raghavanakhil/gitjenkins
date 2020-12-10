import pytest
from selenium import webdriver
from POM.Login import loginCredentials
from Utilities.BaseClass import Baseclass
import time


class TestAdmin(Baseclass):

    def test_admin(self,getData):
        login = loginCredentials(self.driver)
        login.Username().clear()
        login.Username().send_keys(getData[0])
        login.Password().clear()
        login.Password().send_keys(getData[1])
        login.Login().click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//ul[@class='sidebar-menu tree']/li[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[2]/ul/li[2]/a/span").click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[1]/div/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='onoffswitch']/label").click()

        self.driver.find_element_by_id("Name").send_keys('chelakuty')
        self.driver.find_element_by_name("save").click()

@pytest.fixture(params=[("admin@yourstore.com","admin")])
def getData(request):
    return  request.param