import os
from datetime import datetime

def verify_cookies(driver):
    def check_page():
        cookies = driver.get_cookies_dict()
        return "__Secure-ENID" in cookies

    time = 0
    WAIT = 15
    sleep_time = 0.5

    while time < WAIT:
        if check_page():
            print("Cookies successfully accepted")
            return True
        print(f"Waiting for cookies to be accepted... {time}/{WAIT}")
        time += sleep_time
        sleep(sleep_time)

    # Capture d'écran avant de lever une exception
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_filename = f"trace/cookies_error_{timestamp}.png"
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

    print("Unable to consent Cookies")
    raise Exception("Unable to consent Cookies")

def accept_google_cookies(driver):
    try:
        input_el = driver.get_element_or_none_by_selector('[role="combobox"], [role="search"]', 16)
        if input_el is None:
            raise Exception("Unable to load Google")
        else:
            accept_cookies_btn = driver.get_element_or_none_by_selector("button#L2AGLb", 10)
            if accept_cookies_btn is None:
                raise Exception("Unable to find accept cookies button")
            else:
                accept_cookies_btn.click()
                print("Accept cookies button clicked")
                verify_cookies(driver)
    except Exception as e:
        # Capture d'écran en cas d'erreur
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_filename = f"trace/accept_cookies_error_{timestamp}.png"
        driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved as {screenshot_filename}")
        raise e

# Assurez-vous que le dossier trace existe
if not os.path.exists("trace"):
    os.makedirs("trace")