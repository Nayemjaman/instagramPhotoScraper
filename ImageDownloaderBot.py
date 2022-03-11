# import all the modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time



driver = webdriver.Chrome(
    'C:/Users/USER/Desktop/insrtagram_pic/chromedriver.exe')
# driver.close()
driver.get('https://www.instagram.com')



# username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
# password
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("python_is_everywhere")

password.clear()
password.send_keys("forgot@password")
time.sleep(2)

# login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()


time.sleep(2)
# Not Now button
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


# the search input field
searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

# searching user
keyword = "Beauties.Bangladesh"
searchbox.send_keys(keyword)

# FIXING DOUBLE ENTER
time.sleep(2)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ARROW_UP)
searchbox.send_keys(Keys.ENTER)


scroll = 4
for x in range(0, scroll):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

images_links = driver.find_elements_by_tag_name('a')
images_links = [a.get_attribute('href') for a in images_links]
#narrow down all links to image links only
images_links = [a for a in images_links if str(a).startswith("https://www.instagram.com/p/")]







time.sleep(60)
driver.close()










