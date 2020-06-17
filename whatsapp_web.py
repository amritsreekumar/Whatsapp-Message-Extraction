from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 
import csv

WAIT_FOR_CHAT_TO_LOAD = 9 # in secs

message_dic = {}
chrome_path = "/chromedriver"
driver = webdriver.Chrome(chrome_path)

def chats():
    name = driver.find_element_by_xpath('//span[@title = "Name"]').text
    m_arg = '//div[@class="_9tCEa"]/div'

    #superclass for message-in and message-out
    for messages in driver.find_elements_by_xpath("//div[contains(@class, '_2hqOq')]"):
        try:
            message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
            message = message_container.find_element_by_xpath(".//span[contains(@class,'selectable-text invisible-space copyable-text')]").text
            print(message)

        except:
            try:
                message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
                emoji = message_container.find_element_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]")
                print(emoji.get_attribute("data-plain-text"))
            except:
                pass


def scrape(prev):
    recentList = driver.find_element_by_xpath('//span[@title = "Name"]')
    #recentList.sort(key=lambda x: int(x.get_attribute('style').split("translateY(")[1].split('px')[0]), reverse=False)

    recentList.click()
    time.sleep(WAIT_FOR_CHAT_TO_LOAD)
    input("click enter to start scan")
    chats()
    return

if __name__ == '__main__':
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window() 
    driver.implicitly_wait(15)
    scrape(None)
