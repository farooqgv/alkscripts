from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import secrets
import os.path

image = "capture.png"
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com/search?q=what+is+my+ip&oq=what+is+my+ip&aqs=chrome..69i57.1737j0j4&sourceid=chrome&ie=UTF-8")
#lucky_button = driver.find_element_by_xpath('//*[@id="section_passwords"]/div[6]/div[2]/div/div[1]/div[4]/button/span/svg')
#lucky_button.click()

#//*[@id="section_passwords"]/div[6]/div[2]/div/div[1]/div[4]/button/span/svg
# capture the screen
def genHash():

    hash = str(secrets.token_urlsafe(16))
    return hash


if os.path.isfile(str(image)):
    driver.get_screenshot_as_file(str(genHash) + ".png")
    print("saved new")
else:
    driver.get_screenshot_as_file(str(image))
    print("created")


#hash = random.getrandbits(128)