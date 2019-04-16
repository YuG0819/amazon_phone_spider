from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.bestbuy.com/')

if driver.find_element_by_class_name('us-link'):
    print('1111111')
else:
    print('00000')