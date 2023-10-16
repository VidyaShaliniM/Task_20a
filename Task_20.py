from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Co_win:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_faq(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
            home_window = self.driver.window_handles[0]
            # Open FAQ tab
            self.driver.find_element(by=By.CSS_SELECTOR, value='a.dropdwnbtn.accessibility-plugin-ac.newMenu[href="/faq"]').click()
            sleep(4)
            # get the window handle of faq tab
            faq_window = self.driver.window_handles[1]
            # Open Partners tab
            self.driver.find_element(by=By.XPATH, value='/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
            sleep(4)
            # Get the window handle of Partners tab
            partner_window = self.driver.window_handles[2]
            # Get all the Window handles
            a = self.driver.window_handles
            # Loop through the window handles and close the faq and partners window
            for i in a:
                if i != home_window:
                    self.driver.switch_to.window(i)
                    self.driver.close()
            # Switch to the Home window
            self.driver.switch_to.window(home_window)
            sleep(4)
            # Get the Window /Frame ID of FAQ and partner windows
            print(faq_window,partner_window)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()


url = "https://www.cowin.gov.in/"

co = Co_win(url)

co.open_faq()

