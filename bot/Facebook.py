from selenium import webdriver
from time import sleep

class Facebook:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://facebook.com')
        sleep(2)

        email_in = self.driver.find_element_by_xpath('// *[ @ id = "email"]')
        email_in.send_keys('skalexsong@gmail.com')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('zura23x@#')

        login_button = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
        login_button.click()
        sleep(2)

        # feedBtn = self.driver.find_element_by_xpath('//*[@id="js_5n"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div')
        # feedBtn.click()

        # statusPost = self.driver.find_element_by_xpath('//*[@id="js_35"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/span/span')
        # statusPost.send_keys('This text was created by fbAutoBot compiled using python by Sami Kalammallah')

        # klik post
        # postBtn = bot.driver.find_element_by_xpath('//*[@id="js_35"]/div[2]/div[3]/div[2]/button')
        # postBtn.click()

    def logout(self):
        option_button = self.driver.find_element_by_xpath('//*[@id="userNavigationLabel"]')
        option_button.click()

        logout_button = self.driver.find_element_by_xpath('//*[@id="js_nx"]/div/div/ul/li[20]')
        logout_button.click()


bot = Facebook()
bot.login()
bot.logout()
