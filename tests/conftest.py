from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(params=['chrome','edge'])
def set_up(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path=r"../driver/chromedriver.exe")
    elif request.param == 'edge':
        driver = webdriver.Edge(executable_path=r"../driver/msedgedriver.exe")
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.set_page_load_timeout(20)
    driver.implicitly_wait(20)
    return driver

