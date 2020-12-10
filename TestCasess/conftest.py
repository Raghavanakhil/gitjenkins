import pytest
from selenium import webdriver


@pytest.fixture(scope = "class")
def setUp(request):
    driver = webdriver.Chrome("D://chromedriver_win32 (1)//driver//chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
