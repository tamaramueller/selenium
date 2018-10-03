from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# created by Tamara Mueller

url = "http://www.quantbet.com/quiz/dev"


def gcd(x, y):
     while y != 0:
         (x, y) = (y, x % y)
     return x

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
driver.get(url)
driver.get(url)

nrs = driver.find_elements_by_xpath("//strong")
nr1 = nrs[0].text
nr2 = nrs[1].text

driver.find_element_by_id('calchainput').send_keys(str(gcd(int(nr1), int(nr2))))
driver.find_element_by_xpath("//button").click()
print(driver.find_element_by_xpath("//div[@class='quiz-content']//div").text)

