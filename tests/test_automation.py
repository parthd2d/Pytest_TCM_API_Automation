import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver():
    # Set up Appium driver
    driver = webdriver.Remote()
    
    yield driver
    # Clean up after the test
    driver.quit()

def test_sample(driver):
    # Example: Test if the app is launched correctly
    assert driver.current_activity is not None

def test_example(driver):
        search_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
            )

        search_element.click()
        search_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
            )
        search_input.send_keys("BrowserStack")
        time.sleep(5)
        search_results = driver.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView")
        
        assert len(search_results) > 0
