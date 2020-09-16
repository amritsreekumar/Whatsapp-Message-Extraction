from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

WAIT_FOR_CHAT_TO_LOAD = 9 # in secs


message_dic = {}
#place the chromedriver in the same path as your google chrome
chrome_path = "path_to/chromedriver"
driver = webdriver.Chrome(chrome_path)

def chats():
    name = driver.find_element_by_xpath('//span[@title = "Name"]').text
    m_arg = '//div[@class="_9tCEa"]/div'
    list_messages = []
    #superclass for message-in and message-out
    for messages in driver.find_elements_by_xpath("//div[contains(@class, '_2hqOq')]"):
        try:
            #print(messages)
            message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
            message = message_container.find_element_by_xpath(".//span[contains(@class,'selectable-text invisible-space copyable-text')]").text
            list_messages.append(message)

        except:
            try:
                message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
                emoji = message_container.find_element_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]")
                list_messages.append(emoji.get_attribute("data-plain-text"))
            except:
                pass
    return list_messages


def scrape(prev):
    recentList = driver.find_element_by_xpath('//span[@title = "Name"]')
    #recentList.sort(key=lambda x: int(x.get_attribute('style').split("translateY(")[1].split('px')[0]), reverse=False)
    recentList.click()
    time.sleep(WAIT_FOR_CHAT_TO_LOAD)
    #input("click enter to start scan")
    messages = chats()
    return messages


driver.get("https://web.whatsapp.com/")
driver.maximize_window() 
driver.implicitly_wait(20)
