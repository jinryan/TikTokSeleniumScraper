import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


# Initialize website and scrapper
website = 'https://www.tiktok.com/'
driver_path = 'ChromeDriver/chromedriver' # Replace this with driver
absolute_driver_path = os.path.abspath(os.path.join(os.getcwd(), driver_path))
print(absolute_driver_path)
service = Service(executable_path=absolute_driver_path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
driver.implicitly_wait(5) # We declare our assumption that max load time for a page is 5s


guest_mode = True

# Step 1: Login
if guest_mode:
    # input("Press enter after login")
    guest_button = driver.find_element(by=By.XPATH, value="//*[@id=\"loginContainer\"]/div/div/div[3]/div/div[2]")
    guest_button.click()
else:
    input("Press enter after login")

# Step 2: Navigate to For You Page
for_you_button = driver.find_element(by=By.CSS_SELECTOR, value="a[data-e2e=\"nav-foryou\"]")
for_you_button.click()

# Step 3: Click on the content to allow scroll
content_page = driver.find_element(by=By.ID, value="main-content-homepage_hot")
content_page.click()

# Step 4: Wait 2 seconds for content to load and scroll through videos
numVidsToScroll = 2
secondsWatchingEachVid = 2
time.sleep(2)
for i in range(numVidsToScroll):
    time.sleep(secondsWatchingEachVid)
    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

# Step 5: Find all video descriptions and print them
vid_descs = driver.find_elements(by=By.CSS_SELECTOR,
                                   value=f"div[data-e2e=\"video-desc\"]")
for vd in vid_descs:
    try:
        desc = vd.find_element(by=By.CLASS_NAME, value="efbd9f0")
        print(desc.get_attribute("innerHTML"))
    except:
        continue

# Step 6: Search

targetUserName = "harrycollinsphotography"
search_bar = driver.find_element(by=By.XPATH, value="//*[@id=\"app-header\"]/div/div[2]/div/form/input")
search_bar.send_keys(targetUserName)
ActionChains(driver).key_down(Keys.ENTER).perform()
# search_bar.click()

# Step 7: Enter channel
if guest_mode:
    input("Press enter after completing captcha") # Have to complete captcha
    china_daily = driver.find_element(by=By.XPATH, value="//*[@id=\"search_user-item-user-link-0\"]")

else:
    china_daily = driver.find_element(by=By.XPATH, value="//*[@id=\"tabs-0-panel-search_top\"]/div/div/div[1]/div[2]")

# Step 8: Spend some time on the page of the channel
secondsStayingOnChannelPage = 4
china_daily.click()
time.sleep(secondsStayingOnChannelPage)

# Step 9: Go Back to Rec Feed
for_you_button = driver.find_element(by=By.CSS_SELECTOR, value="a[data-e2e=\"nav-foryou\"]")
for_you_button.click()

print("\n\n====NEW VID DESCRIPTIONS====")


# Step 10: Scroll Feed
numVidsToScroll = 10
secondsWatchingEachVid = 1
time.sleep(3) # Wait for feed to load
for i in range(numVidsToScroll):
    time.sleep(secondsWatchingEachVid)
    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

# Step 11: Get all video descriptions and print them out
vid_descs = driver.find_elements(by=By.CSS_SELECTOR,
                                   value=f"div[data-e2e=\"video-desc\"]")
for index, vd in enumerate(vid_descs):
    try:
        desc = vd.find_element(by=By.CLASS_NAME, value="efbd9f0")
        val = desc.get_attribute("innerHTML")
        print(f"Video {index}: {val}")
    except:
        continue

input("Press Enter to quit the script and close the browser...")

driver.quit()  # Close the browser when you're done.