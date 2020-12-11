import pytest
from selenium import webdriver
from POM.Login import loginCredentials
from Utilities.BaseClass import Baseclass
from POM.Categories import Subcategory
import time
import pytest_html


class TestAdmin(Baseclass):

    def test_admin(self,getData):
        login = loginCredentials(self.driver)
        subcate = Subcategory(self.driver)
        login.Username().clear()
        login.Username().send_keys(getData[0])
        login.Password().clear()
        login.Password().send_keys(getData[1])
        login.Login().click()
        time.sleep(2)
        subcate.MainMenu().click()
        time.sleep(3)
        subcate.Submenu().click()
        subcate.Addnew().click()
        time.sleep(3)
        subcate.Swipe().click()
        self.driver.find_element_by_id("Name").send_keys('chelakuty')
        self.driver.find_element_by_name("save").click()

@pytest.fixture(params=[("admin@yourstore.com","admin")])
def getData(request):
    return  request.param


