from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import random

log = open("log.txt", "a")
# driver = webdriver.Chrome()
def renew_grade():
    # driver = webdriver.Chrome("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
    driver = webdriver.Chrome('/Users/zhangtingyu/Desktop/chromedriver')
    driver.get("http://www.acorn.utoronto.ca/")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/div[2]/p[2]/a").click()
    log.write("able to enter username/pwd\n")
    username = driver.find_element_by_xpath("//*[@id=\"username\"]")
    username.clear()
    username.send_keys("zhan3852")
    pwd = driver.find_element_by_xpath("//*[@id=\"password\"]")
    pwd.clear()
    pwd.send_keys("Longlingyu420")
    submit = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/form/button")
    submit.click()
    log.write("login\n")
    try:
        submit.click()
    except:
        pass
    counter = 0
    while True:
        if counter % 5 == 0:
            driver.get("https://acorn.utoronto.ca/sws/timetable/scheduleView.do#/calendar")
        driver.get("https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/courses/1")
        time.sleep(1)#random.randint(1, 3))
        try:
            driver.find_element_by_xpath("//*[@id=\"CSC420H1-planCourseBox\"]/div[1]/div[1]/div[2]/div[1]/a/span[2]").click()
            # submit_ = driver.find_element_by_xpath("//*[@id=\"plan-CSC420H1-LEC-0101\"]/tr/td[5]/div[4]/a")
            # #submit_ = driver.find_element_by_xpath("//*[@id=\"plan-MAT245H1-LEC-0101\"]/tr/td[5]/div[4]/a")
            # submit_.click()
            # content = driver.page_source
            time.sleep(1)#random.randint(1,3))
            driver.find_element_by_xpath("//*[@id=\"LEC0101\"]").click()
            # driver.find_element_by_xpath("//*[@id=\"plan\"]").click()
            #driver.find_element_by_xpath("//*[@id=\"course-modal\"]/div/div[2]/div/div[1]/button").click()
            driver.find_element_by_xpath("//*[@id=\"enrol\"]").click()
            driver.find_element_by_xpath("//*[@id=\"course-modal\"]/div/div[2]/div/div[1]/button").click()
            driver.refresh()
            counter += 1
        except:
            pass
    

    # soup = BeautifulSoup(content,"lxml")
    # lst1 = soup.find(class_ = "spaceAvailability")#find("//*[@id=\"LEC-0101\"]/tr/td[5]/div/div/div/div[1]/span")

    # print(lst1.find(class_= "spaceAvailabilityDetails ng-hide"))
  
        
renew_grade()
