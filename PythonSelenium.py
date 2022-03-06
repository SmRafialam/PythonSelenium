from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest


driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://demoqa.com/elements')
driver.maximize_window()


#for check box

class LabelTest(unittest.TestCase):
    def test_textfield_one(self):
    check_box=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]")
    print(check_box.is_selected())

    if check_box.is_selected()==False:

    check_box.click()
    Home = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]/span')
    Home.click()
    time.sleep(3)

    plus_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/button[1]')
    plus_button.send_keys(Keys.RETURN)
    time.sleep(3)

    Notes = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]')
    Notes.click()
    time.sleep(3)

    Angular = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]')
    Angular.click()
    time.sleep(10)

    driver.back()
    driver.back()

#for radio_buttons

radio_button=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[3]")
print(radio_button.is_selected())

if(radio_button.is_selected()):
    radio_button.click()
    time.sleep(5)
    driver.back()

#for text_box
text_box = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]")
print(text_box.is_selected())

if text_box.is_selected() == False:
    text_box.click()
    time.sleep(2)
    text_box[0].send_keys('Rafi')
    text_box[1].send_keys('17201053@uap-bd.edu')
    time.sleep(2)
    text_box[2].send_keys('Barisal')

    time.sleep(2)
    text_box[4].send_keys('Barisal')

    time.sleep(2)
    driver.back()
#for buttons
buttons=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[5]")
print(buttons.is_selected())

if buttons.is_selected():
    buttons.click()
    button = driver.find_element_by_id("CLICK ME")
    button.send_keys(Keys.RETURN)
    time.sleep(15)



driver.quit()
