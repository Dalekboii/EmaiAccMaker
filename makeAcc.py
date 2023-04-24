from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import time

# Define the username and password for the email accounts
username = "asndowlc"
password = "BusterBoii1031"

# Launch the Tor Browser and configure the Firefox driver
options = Options()
options.binary_location = r"C:\Users\dalek\Desktop\Tor Browser\Browser\firefox.exe" # Replace this with the path to your Tor Browser executable
options.add_argument('--proxy-server=socks5://localhost:9150') # Set the Tor Browser proxy settings
profile = webdriver.FirefoxProfile(r"C:\Users\dalek\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default") # Replace this with the path to your Tor Browser profile
driver = webdriver.Firefox(firefox_profile=profile, options=options)

# Fill in the required fields and click the "Create account" button 365 times
for i in range(133, 366):
    driver.implicitly_wait(20)
    driver.get("https://signup.live.com/signup")
    # Define the email address
    email_address = username + str(i)

    driver.find_element("id", "liveSwitch").click()

    # Fill in the required fields
    driver.find_element("id", "MemberName").send_keys(email_address)

    driver.find_element("id", "iSignupAction").click()

    driver.find_element("id", "PasswordInput").send_keys(password)
    driver.find_element("id", "iSignupAction").click()
    driver.find_element("id", "FirstName").send_keys("John")
    time.sleep(.5)
    driver.find_element("id", "LastName").send_keys("Doe")
    driver.find_element("id", "iSignupAction").click()
    month_dropdown = Select(driver.find_element("id", "BirthMonth"))
    month_dropdown.select_by_value("1")
    day_dropdown = Select(driver.find_element("id", "BirthDay"))
    day_dropdown.select_by_value("1")
    driver.find_element("id", "BirthYear").send_keys("1990")
    driver.find_element("id", "iSignupAction").click()

    input()

print("365 email accounts have been created!")
