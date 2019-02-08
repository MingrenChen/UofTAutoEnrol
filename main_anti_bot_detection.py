from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import random

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


script_select_course = '''
var Lec_code = "LEC0101";
var Tut_code = null;
var Pra_code = null;
var check_course = function(){
    var flag = false
    var sections = document.getElementsByClassName("modal-course-container")[0]
    var section = sections.getElementsByClassName("modal_course_enrolment")[0]
    var lecture = section.getElementsByTagName("table")[0]
    var tables;Lxm990409@
    if (check_type_exist(lecture)){
        if (Lec_code !== null){
            tables = lecture.getElementsByTagName('tbody')
            for (let i=0;i<tables.length;i++){
                let inp = tables[i].getElementsByTagName('input')[0]
                if (inp.id === Lec_code){
                    inp.click()
                    flag = true
                }
            }
        } else {
            tables = lecture.getElementsByTagName('tbody')
            var re = /\d+ of \d+ available./i ;
            for (let i=0;i<tables.length;i++){
                let text = $('#'+ tables[i].id + ' > tr > td.spaceAvailability > div > div > div > div:nth-child(1) > span')[0].innerText
                if (re.test(text)){
                    let inp = tables[i].getElementsByTagName('input')[0]
                    inp.click()
                    flag = true
                }
            }
        }
    }

}

var check_type_exist = function(elem){
    if (elem.getElementsByTagName('tbody').length === 0)return false
    return true
}
check_course()

'''

script_enrol_button = '''
var check_enrol_button = function(){
    let enrolbutton = document.getElementById("enrol")
    for (let i=0;i<enrolbutton.classList.length;i++){
        console.log(enrolbutton.classList[i])
        if (enrolbutton.classList[i] == 'disabled')
            return false
    }
    enrolbutton.click()
    return true
}

return check_enrol_button()
'''



def main(uname, password, course):
    script = '''
    var course_code = "''' + course[:-3] + '''"
    var t = 1;

    $(document).ready(function(){
      $('#typeaheadInput').val(course_code);
      $('#typeaheadInput').trigger('change');
    });
    var b = $( "#typeahead-search > div.ut-typeahead-container > form > div > div > div" ).select()[0].style.display = "block";
    b;

    var click_on_result = function(){
        var result = document.getElementsByClassName("ut-typeahead-results-list")[0].getElementsByTagName("li")[t]
        result.click()
    }
    '''

    #binary = FirefoxBinary('HKEY_LOCAL_MACHINE\SOFTWARE WOW6432Node\Mozilla\Mozilla Firefox\64.0.2\Main\PathToExe')
    # driver = webdriver.Firefox()

    #driver = webdriver.WebKitGTK('./geckodriver.exe')
    driver = webdriver.Chrome('./chromedriver')
    #driver = webdriver.Firefox('./geckodriver.exe')
    # driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
    driver.get("http://www.acorn.utoronto.ca/")
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/p[2]/a").click()
    username = driver.find_element_by_xpath("//*[@id=\"username\"]")

    username.clear()
    username.send_keys(uname)
    pwd = driver.find_element_by_xpath("//*[@id=\"password\"]")
    pwd.clear()
    pwd.send_keys(password)
    submit = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/form/button")
    submit.click()
    exception_count = 0
    # try:
    #     submit.click()
    # except:
    #     pass
    flag = False
    driver.get("https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/courses/0")
    while not flag:
        try:
            if exception_count == 5:
                driver.close()
                break
            driver.refresh()
            driver.execute_script(script)
            table_menu = driver.find_elements_by_xpath(
                "//*[@id=\"typeahead-search\"]/div[1]/form/div/div/div/div[1]/ul/li")
            if not table_menu:
                continue
            for i in table_menu:
                if i.find_element_by_tag_name("span").text[:10] == course:
                    i.click()
            try:
                driver.execute_script(script_select_course)
            
                flag = driver.execute_script(script_enrol_button)
            except:
                continue
            time.sleep(10)
            if flag:
                driver.close()
                break
            exception_count = 0

        except:
            exception_count +=1
            continue

    print('next')
    print(flag)
    if flag:
        exit(1)
while True:
    main("luxiaome", "Lxm990409@", "STA304H1 S")
