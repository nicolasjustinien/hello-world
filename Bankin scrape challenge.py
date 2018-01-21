import time
import json
import selenium
from selenium import webdriver
import selenium.webdriver.chrome.service
from selenium.webdriver.support.ui import WebDriverWait
import json



def reload_page(driver,tag):
    try:
        alert = driver.switch_to_alert()
        if alert.text=='Oops! Something went wrong':
            alert.accept()
            return True
    except:
        pass
    try:
        if driver.find_elements_by_tag_name(tag)==[] or driver.find_elements_by_tag_name(tag)==None :
            return True
    except:
        pass
    return False

def main():
    service = selenium.webdriver.chrome.service.Service('/Users/nicolasjustinien/Downloads/chromedriver')
    service.start()
    capabilities = {'chrome.binary': '/Applications'}
    driver = webdriver.Remote(service.service_url, capabilities)
    webpage_without_number = 'https://web.bankin.com/challenge/index.html?start='
    previous_webpage_number = '-1'
    webpage_number = '0'
    tag = 'tr'
    headers = ['Account', 'Transaction', 'Amount']
    output_list = []
    driver.get(webpage_without_number + webpage_number)
    while int(previous_webpage_number)<int(webpage_number):
        while reload_page(driver, tag):
            driver.get(webpage_without_number + webpage_number)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_tag_name(tag))
        transactions = driver.find_elements_by_tag_name("tr")
        for row in transactions:
            row_item_list = row.text.split(' ')
            print(row_item_list)
            output_list.append(row_item_list)
        output_list.remove(headers)
        previous_webpage_number = webpage_number
        webpage_number = str(output_list[len(output_list)-1][2])
        print('-------------------------------\n')
        driver.get(webpage_without_number + webpage_number)
    print('-------------------------------\n'+'Done'+'\n-------------------------------')
    print(output_list)
main()