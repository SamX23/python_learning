from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time


class BrowseBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.product = []
        self.prices = []
        self.ratings = []

    def crawl(self):
        self.driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq')
        time.sleep(3)

    def define(self):
        content = self.driver.page_source
        soup = BeautifulSoup(content)
        for a in soup.find_all('a', href=True, attrs={'class': '_31qSD5'}):
            name = a.find('div', attrs={'class': '_3wU53n'})
            price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
            rating = a.find('div', attrs={'class': 'hGSR34'})
            #  _2beYZw
            self.product.append(name.text)
            self.prices.append(price.text)
            self.ratings.append(rating.text)

        time.sleep(3)
        self.driver.quit()

    def save(self):
        db = pd.DataFrame({'Product Name': self.product, 'Price': self.prices, 'Rating': self.ratings})
        db.to_csv('products.csv', index=False, encoding='utf-8')


bot = BrowseBot()
bot.crawl()
bot.define()
bot.save()
