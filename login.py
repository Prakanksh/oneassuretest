import time
from selenium import webdriver

def login():
    driver = webdriver.Chrome(r"C:\Users\Syn_A\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://app.oneassure.in")
    driver.implicitly_wait(10)
    driver.find_elements_by_class_name("MuiInput-input")[0].send_keys("9166833189")
    driver.find_elements_by_class_name("MuiInput-input")[1].send_keys("Prakanksha123")
    time.sleep(5)
    driver.find_element_by_class_name("MuiButton-label").click()
    time.sleep(5)
    driver.find_elements_by_class_name("MuiButtonBase-root")[0].click()
    driver.find_elements_by_class_name("MuiListItem-button")[1].click()
    time.sleep(7)
    driver.find_elements_by_class_name("MuiSvgIcon-root")[1].click()
    driver.find_elements_by_class_name("MuiInput-input")[0].send_keys("Prakanksha Nagpalthi")
    driver.find_elements_by_class_name("MuiInput-input")[1].send_keys("9619975427")
    driver.find_elements_by_class_name("MuiInput-input")[2].send_keys("nagpalprakanksh@gmail.com")
    driver.find_elements_by_class_name("MuiButton-label")[1].click()

    driver.find_elements_by_class_name("add_reminder")[0].click()
    driver.find_elements_by_class_name("MuiInput-input")[0].send_keys("02-02-2022")
    driver.find_elements_by_class_name("MuiInput-input")[1].click()
    driver.find_elements_by_class_name("MuiListItem-button")[2].click()
    driver.find_elements_by_class_name("MuiInput-input")[2].send_keys("This is the reminder")
    driver.find_elements_by_class_name("MuiButton-label")[1].click()
    driver.find_elements_by_class_name("MuiButton-label")[1].click()
    text = driver.find_elements_by_class_name("margin_left_6")[1].text
    print(text)