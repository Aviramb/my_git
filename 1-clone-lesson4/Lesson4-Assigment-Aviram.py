# #1+2
# from selenium import webdriver
# CH_PATH = "c:\chromedriver.exe"
# chrome_driver = webdriver.Chrome(CH_PATH)
# chrome_driver.get("http://www.walla.co.il")
# get_title = chrome_driver.title
# print(get_title)
# chrome_driver.refresh()
# get_name = chrome_driver.name
# print(get_name)
# if get_title == get_name:
#     print("name and title are the same")
# else:
#     print("different")
# FF_PATH = "c:\msedgedriver.exe"
# FF_Driver = webdriver.Edge(FF_PATH)
# FF_Driver.get("http://www.ynet.co.il")

# 3. No.The ID changes every refresh..
# 4. Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
from selenium import webdriver
# from selenium.webdriver.common.keys import keys
# from selenium.webdriver.common.keys import keys
CH_PATH = "c:\chromedriver.exe"
chrome_driver = webdriver.Chrome(CH_PATH)
chrome_driver.get("https://translate.google.co.il")
search = chrome_driver.find_element_by_css_selector("textarea")
# search = chrome_driver.find_element_by_id("yDmH0d")
# search = chrome_driver.find_element_by_xpath("//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div")
# //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div
# search = chrome_driver.find_element_by_id("yDmH0d")
# search = chrome_driver.find_element_by_id("i5")
search.send_keys("car")
# search.send_keys(keys.RETURN)

# 5.
chrome_driver.get("https://www.youtube.com/")
search = chrome_driver.find_element_by_css_selector("input")
# search = chrome_driver.find_element_by_id("search")
search.send_keys("minecraft to nintndo")
search = chrome_driver.find_element_by_id("search-icon-legacy")
search.click()

# 7.
chrome_driver.get("https://www.facebook.com")
user = chrome_driver.find_element_by_id("email")
user.send_keys("bachar.aviram@gmail.com")
password = chrome_driver.find_element_by_id("pass")
password.send_keys("1234")
login = chrome_driver.find_element_by_name("login")
login.click()