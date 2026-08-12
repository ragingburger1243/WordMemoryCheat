import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/verbal-memory")
word_set = set()

input("Start test, And press enter here")
previous_word = ""
while True:
    try:
        # Get the current word
        word_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".word"))
        )

        word = word_element.text.strip()

        if word in word_set:
            seen_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='SEEN']"))
            )
            seen_button.click()

        else:
            new_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='NEW']"))
            )
            new_button.click()
            word_set.add(word)



        time.sleep(0.05)

    except (StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
        continue