from time import sleep
from .wait import Wait

def verify_cookies(driver):
    def check_page():
        return "__Secure-ENID" in driver.get_cookies_dict()

    time = 0
    WAIT = 8
    sleep_time = 0.1

    while time < WAIT:
        if check_page():
            return True
        time += sleep_time
        sleep(sleep_time)

    raise Exception("Unable to consent Cookies")

def accept_google_cookies(driver):
    input_el = driver.get_element_or_none_by_selector('[role="combobox"], [role="search"]', 16)
    if input_el is None:
        raise Exception("Unable to load Google")
    else:
        accept_cookies_btn = driver.get_element_or_none_by_selector("button#L2AGLb", Wait.SHORT)
        if accept_cookies_btn is None:
            raise Exception("Unable to find accept cookies button")
        else:
            accept_cookies_btn.click()
            verify_cookies(driver)