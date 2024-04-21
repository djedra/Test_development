from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

chrome_driver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_driver_path)
browser = Chrome(service=browser_service)


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


def yandex_login(email: str, password: str) -> bool:
    browser.get('https://passport.yandex.ru/auth/')

    try:
        login_form = browser.find_element(By.ID, value='passp-field-login')
        login_form.send_keys(email)
    except NoSuchElementException:
        use_email_button = browser.find_element(By.XPATH,
                                                value='//button[@class="Button2 Button2_size_l Button2_view_clear"]')
        use_email_button.click()

        time.sleep(2)

        login_form = browser.find_element(By.ID, value='passp-field-login')
        login_form.send_keys(email)

    sign_in_button_login = browser.find_element(By.ID, value='passp:sign-in')
    sign_in_button_login.click()

    try:
        password_form = wait_element(browser, by=By.ID, value='passp-field-passwd')
        print(type(password_form))
        password_form.send_keys(password)
    except TimeoutException:
        return False

    time.sleep(1)

    sign_in_button_pass = browser.find_element(By.ID, value='passp:sign-in')
    sign_in_button_pass.click()

    time.sleep(2)

    try:
        phone_code_field = browser.find_element(By.ID, value='passp-field-phoneCode')
        return True
    except NoSuchElementException:
        return False
