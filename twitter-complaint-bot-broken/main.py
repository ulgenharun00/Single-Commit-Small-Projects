from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 75
PROMISED_UP = 8
EMAIL = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 7
        self.down = 54
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)

    # def get_internet_speed(self):
    #     self.driver.get("https://www.speedtest.net/")
    #     time.sleep(5)
    #     go_button = self.driver.find_element(By.CSS_SELECTOR, "a[role='button'].js-start-test.test-mode-multi")
    #     go_button.click()
    #     time.sleep(60)
    #     self.up = 50
    #     self.down = 7

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://x.com/home")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div"))
        ).click()

        time.sleep(3)

        email = self.driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='identifier']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email'][name='identifier']"))
        )
        email.send_keys(EMAIL)

        time.sleep(3)

        next_button = self.driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")
        next_button.click()

bot = InternetSpeedTwitterBot()
bot.tweet_at_provider()




