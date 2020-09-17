import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

DRIVER_PATH = '/Users/haleytaft/Downloads/chromedriver'


driver = webdriver.Chrome( executable_path=DRIVER_PATH) #options=options,
driver.get("https://www.chewy.com/b/toys-315")

# To first just look at CHEW TOYS
chew_toys_link = driver.find_element_by_link_text('Chew Toys')
chew_toys_link.click()

try:
    # To get to moderate chew toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Moderate")))
    element.click()
    # To look at the moderate chew toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Chew Toys")))
    articles = driver.find_elements_by_class_name('product-holder js-tracked-product cw-card cw-card-hover')
    # To get back to Chew Toys
    driver.back()

    # To get to tough chew toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Tough")))
    element.click()
    # To look at the tough chew toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Chew Toys")))
    # To get back to Chew Toys
    driver.back()

    # To get to Extreme chew toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Extreme")))
    element.click()
    # To look at the extreme chew toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Chew Toys")))
    driver.back() # back to chew toys
    # DONE WITH CHEW TOYS

    # back to toys
    driver.back()
    # driver.back()

    # Looking at PLUSH TOYS
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    element.click()

    # Looking a the Stuffed toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Stuffed Toys")))
    element.click()
    # To look at the stuffed plush toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    # To get back to plush toys
    driver.back()

    # Looking a the Unstuffed toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Unstuffed Toys")))
    element.click()
    # To look at the unstuffed plush toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    # To get back to plush toys
    driver.back()
    # DONE WITH PLUSH TOYS

    # Back to toys
    driver.back()

    # Now Looking at FETCH TOYS
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Fetch Toys")))
    element.click()

    # Looking a the Balls toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Balls")))
    element.click()
    # To look at the ball fetch toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Fetch Toys")))
    # To get back to fetch toys
    driver.back()

    # Looking a the Discs toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Discs")))
    element.click()
    # To look at the disc fetch toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Fetch Toys")))
    # To get back to fetch toys
    driver.back()

    # Looking a the Launcher toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Launchers")))
    element.click()
    # To look at the launcher fetch toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Fetch Toys")))
    # To get back to fetch toys
    driver.back()

    # Looking a the Stick toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sticks")))
    element.click()
    # To look at the stick fetch toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Fetch Toys")))
    # To get back to fetch toys
    driver.back()
    # DONE WITH FETCH TOYS

except:
    driver.quit()
