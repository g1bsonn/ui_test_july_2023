from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. окрыть главную страницу
# 2. открыть страницу логин
# 3. заполнить поле email
# 4. заполнить поле password
# 5. нажать кнопку start

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def open_page(driver, URL):
    driver.get(URL)

def element_click(xpath, driver):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.click()

def get_element_by_id(xpath, driver):
    element = driver.find_element(By.ID, xpath)
    return element

def element_send_keys(xpath, driver, text):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.clear()
    element.send_keys(text)

def login(login, password):
    element_send_keys(xpath="user-name", driver=driver, text=login)
    element_send_keys(xpath="password", driver=driver, text=password)
    element_click(xpath='login-button', driver=driver)

driver = get_driver()
open_page(driver, URL)
login(login=LOGIN, password=PASSWORD)