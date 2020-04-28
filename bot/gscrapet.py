from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas


# time.sleep(5) # Let the user actually see something!
# driver.quit()


class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = []
        time.sleep(2)

    def browse(self):
        self.driver.get('https://google.com')
        click = self.driver.find_element_by_name('q')
        click.send_keys('allinurl:  site:.go.id')
        click.submit()
        time.sleep(2)

    def collect(self):
        content = self.driver.page_source
        get_content = BeautifulSoup(content)
        for a in get_content.find_all('a', href=True, attrs={'class': 'iUh30 tjvcx'}):
            link = a.find('cite', attrs={'class': 'iUh30 tjvcx'})
            self.link.append(link.text)
        time.sleep(2)
        self.driver.quit()

    def save(self):
        db = pandas.DataFrame({'Link': self.link})
        db.to_csv('link.csv', index=False, encoding='utf-8')


bot = Crawler()
bot.browse()
bot.collect()
bot.save()
