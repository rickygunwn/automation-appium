import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

appium_server = AppiumService()
appium_server.start(args=['-p 4723'])

driver = webdriver.Remote('http://127.0.0.1:4723', options=AppiumOptions().load_capabilities(cap))

driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]').click()

wait = WebDriverWait(driver, 10)
el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
el1.click()

appium_server.stop()
