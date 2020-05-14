from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')\
            .click()

my_bot = InstaBot('ctor.exe@icloud.com', '23568912')