from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# webdriver will be the thing that helps us automate tasks in the browser

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The driver is sending the required headers that a website would want
driver = webdriver.Chrome(options=chrome_options)

# Grab the website we want to scrape
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timer = time.time() + 60*5


while True:
    time.sleep(.05)
    driver.find_element(By.ID, value="cookie").click()
    cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
    grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
    factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
    mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
    shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
    alchemy = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
    portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
    time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
    total_money = driver.find_element(By.ID, value="money")
    value = int(total_money.text)

    if value >= int(time_machine.text.split(" ")[3].replace(',', '')):
        time_machine.click()
    elif value >= int(portal.text.split(" ")[2].replace(',', '')):
        portal.click()
    elif value >= int(alchemy.text.split(" ")[3].replace(',', '')):
        alchemy.click()
    elif value >= int(shipment.text.split(" ")[2].replace(',', '')):
        shipment.click()
    elif value >= int(mine.text.split(" ")[2].replace(',', '')):
        mine.click()
    elif value >= int(factory.text.split(" ")[2]):
        factory.click()
    elif value >= int(grandma.text.split(" ")[2]):
        grandma.click()
    elif value >= int(cursor.text.split(" ")[2]):
        cursor.click()

    if time.time() > timer:
        break

print("cookies/second", driver.find_element(By.ID, value="cps").text)

