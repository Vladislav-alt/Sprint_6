import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from utils.urls import Urls

@pytest.fixture(scope="function")
def driver():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(Urls.MAIN_PAGE)
    
    yield driver
    
    if hasattr(pytest, "test_failed") and pytest.test_failed:
        driver.save_screenshot("failure.png")
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    
    if result.when == "call" and result.failed:
        pytest.test_failed = True
    else:
        pytest.test_failed = False