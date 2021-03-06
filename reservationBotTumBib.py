import os, datetime, time, pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=os.path.join("..", "/Users/lorenz/PycharmProjects/TenFastfingersBot/chromedriver_96"))

def print_start():
    print("***********************************")
    print("***********************************")
    print("Reaching out for https://www.ub.tum.de/en/reserve-study-desks\n")
    print("BOT is started")
    print("***********************************")
    print("***********************************")


userDetails = {
    'name' : 'Lorenz Dang',
    'email': 'lorenz.dang@gmail.com',
    'tumID': 'ga45lak'
}
print_start()
#driver.get('https://10fastfingers.com/typing-test/german')

while True:
    pyautogui.click(500,500)
    driver.get('https://www.ub.tum.de/en/reserve-study-desks')
    body = driver.find_element_by_css_selector('body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    x = datetime.date.today() + datetime.timedelta(days=1)
    xx = datetime.date.today() + datetime.timedelta(days=2)
    tomorrowsDate = str((x.strftime('%d. ') + x.strftime('%B %Y')))
    dayAfterTomorrowDate = str((xx.strftime('%d. ') + xx.strftime('%B %Y')))
    print("Set Tomorrow Date", tomorrowsDate, "and DayAfterTomorrow Date", dayAfterTomorrowDate)
    time.sleep(3)
    try:
        pageDate = driver.find_element_by_css_selector('table > tbody > tr.odd.views-row-first > td.views-field.views-field-field-tag > span').text
        print("found date on page", pageDate)
        #if tomorrowsDate in pageDate:
        allrows = driver.find_elements_by_css_selector(
            '#block-system-main > div > div > div.view-content > table > tbody > tr')
        for row in allrows:
            print(row.text)
            if tomorrowsDate in row.text and "Main Campus" in row.text or dayAfterTomorrowDate in row.text and "Main Campus" in row.text:
                print("MATCH FOUND! Tomorrows Date", tomorrowsDate, "found in current row", row.text)
                reservationLink = row
                ActionChains(driver).move_to_element(reservationLink).perform()
                reservationLink = reservationLink.find_element_by_css_selector('a')
                print(reservationLink)
                break
            else:
                print("NO match was found")

        #reservationLink = driver.find_element_by_css_selector('table > tbody > tr.odd.views-row-first > td.views-field.views-field-views-conditional.internlink > a')
        #reservationLink = driver.find_element_by_css_selector('#block-system-main > div > div > div.view-content > table > tbody > tr:nth-child(1) > td.views-field.views-field-views-conditional.internlink > a')
        #ActionChains(driver).move_to_element(reservationLink).perform()
        #print("slot", driver.find_element_by_css_selector('table > tbody > tr.odd.views-row-first').text)
        print("reservation link", reservationLink.get_attribute('href'))
        driver.get(reservationLink.get_attribute('href'))
        time.sleep(3)
        body = driver.find_element_by_css_selector('body')
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        nameInput = driver.find_element_by_css_selector('#edit-field-tn-name-und-0-value')
        nameInput.send_keys(userDetails['name'])
        emailInput = driver.find_element_by_css_selector('#edit-anon-mail.form-text')
        emailInput.send_keys(userDetails['email'])
        TumButton = driver.find_element_by_css_selector('#edit-field-stud-ma-und > div:nth-child(1) > label')
        TumButton.click()
        tumIDInput = driver.find_element_by_css_selector('#edit-field-tum-kennung-und-0-value')
        tumIDInput.send_keys(userDetails['tumID'])
        fstCheckBox = driver.find_element_by_css_selector('#edit-field-benutzungsrichtlinien > div > label')
        ActionChains(driver).move_to_element(fstCheckBox).move_by_offset((-100), (0)).click().perform()
        sndCheckBox = driver.find_element_by_css_selector('#edit-field-datenschutzerklaerung > div > label')
        ActionChains(driver).move_to_element(sndCheckBox).move_by_offset((-40), (0)).click().perform()
        time.sleep(3)
        submitButton = driver.find_element_by_css_selector('#edit-submit').click()
        ActionChains(driver).move_to_element(submitButton).perform()
        submitButton.click()
        print("is Reservation Confirmation in page source? ", ('Reservation Confirmation' in driver.page_source))
        if 'Reservation Confirmation' in driver.page_source:
            print("RESERVATION SUCCESSFUL")
            driver.close()
            break
        else:
            print("RESERVATION FAILED; retry in 10 seconds")
            time.sleep(10)
       # else:
          #  print('fail')
           # time.sleep(10)
    except Exception as e:
        print('ERROR with Exception:', e)
#print("shutting down machine now")
#os.system('shutdown -s')

    # allrows = driver.find_elements_by_css_selector('#block-system-main > div > div > div.view-content > table > tbody > tr')
    # for row in allrows:
    #     print(row.text)
    #     if tomorrowsDate in row.text and "Main Campus" in row.text:
    #         reservationLink = row
    #         reservationLink = reservationLink.find_element_by_css_selector('a').get_attribute('href')
    #         print(reservationLink)
    #         break


