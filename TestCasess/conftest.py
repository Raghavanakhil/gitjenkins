import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'],scope = "class")
def setUp(request):
    driver = webdriver.Chrome("D://chromedriver_win32 (1)//driver//chromedriver.exe")
    #driver1 = webdriver.Firefox("D://chromedriver_win32 (1)//geckodriver.exe")
    if request.param == 'chrome':
        drivers = driver
        drivers.get("https://admin-demo.nopcommerce.com/")
        drivers.maximize_window()
        drivers.implicitly_wait(10)
    request.cls.driver = driver
    yield
    request.close()





