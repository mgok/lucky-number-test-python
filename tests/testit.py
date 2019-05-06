from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        # Edit driver location with yours
        driverLocation = "/Users/mehmetgok/Documents/drivers/chromedriver_mac64"
        os.environ["webdriver.chrome.driver"] = driverLocation

        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)

        # Open the provided URL
        driver.get("http://localhost:8000/lucky/number")
        driver.implicitly_wait(10)

        # id next
        whatsNext = driver.find_element(By.ID, "num")
        print(whatsNext.text)
        assert 0 <= int(whatsNext.text) <= 100


ff = RunChromeTests()
ff.test()
