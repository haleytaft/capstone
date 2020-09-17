import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# options = Options()
# options.headless = True
DRIVER_PATH = '/Users/haleytaft/Downloads/chromedriver'


driver = webdriver.Chrome( executable_path=DRIVER_PATH) #options=options,
driver.get("https://www.chewy.com/b/toys-315")
# assert "Dog Supplies: Best Dog & Puppy Products (Free Shipping)" in driver.title

# To first just look at Chew Toys
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

    driver.back() # back to toys
    # driver.back()

    # Looking at Plush Toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    element.click()

    # Looking a the Stuffed toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Stuffed Toys")))
    element.click()
    # To look at the tough chew toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    # To get back to plush toys
    driver.back()

    # Looking a the Unstuffed toys
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Unstuffed Toys")))
    element.click()
    # To look at the tough chew toys -- NEED TO FIGURE OUT HOW TO ACCESS THEM
    check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Plush Toys")))
    # To get back to plush toys
    driver.back()

    # Back to toys
    driver.back()

    # articles = driver.find_elements_by_class_name('product-holder js-tracked-product cw-card cw-card-hover')

    # div = main.find_elements_by_id("tns1")
    # print(div)
    # for a in divs:
    #     header = div.find_element_by_class_name("")


except:
    driver.quit()
    # print(main.text)

    # div_department = main.find_element_by_class_name('department')

    # print(div_department.text)
    # div_container = div_department.find_element_by_class_name('container')
    # print(div_container.text)

    # aside = div_department.find_element_by_class_name('dept-sliders')

    # print("hi")

    # ul = div_department.find_element_by_tag_name('ul')

    # print("hello")

    # lis = ul.find_elements_by_tag_name('li')

    # print(lis[2])
    # li = lis[2]

    # toys = ul.find_elements_by_tag_name("a")
    # print(toys[1])

    # toys_link = driver.find_element_by_link_text("Toys")
    # print(toys_link)
    # toys_link.click()
    # time.sleep(5)

    # for il in
    # toys_link = toys.find_element_by_link_text('/b/toys-315')
    # print(toys_link)

# toys = driv er.find_element_by_tag_name('a')
# toys_link = driver.find_element_by_partial_link_text('/b/toys-315')
# driver.get(toys_link)
# print(driver.title)

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

# assert "No results found." not in driver.page_source
# time.sleep(5)
# driver.close()
