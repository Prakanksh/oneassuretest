from login import *
import time


def Register():
    driver = webdriver.Chrome(r"C:\Users\Syn_A\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://app.oneassure.in")
    driver.implicitly_wait(10)
    my_list = driver.find_elements_by_class_name("MuiTypography-caption")[2]
    my_list.click()
    driver.find_element_by_id("standard-full-width").send_keys("9166833189")
    driver.find_element_by_class_name("MuiButton-label").click()
    otp = int(input("enter the otp"))
    driver.find_element_by_id("standard-full-width").send_keys(otp)
    driver.find_element_by_class_name("MuiButtonBase-root").click()
    time.sleep(5)
    driver.find_elements_by_class_name("MuiInput-input")[1].send_keys("Prakanksha Nagpal")
    driver.find_elements_by_class_name("MuiInput-input")[2].send_keys("Prakanksha123")
    driver.find_elements_by_class_name("MuiInput-input")[3].send_keys("nagpalprakankshabvpy@gmail.com")
    driver.find_elements_by_class_name("MuiInput-input")[4].send_keys("324005")
    driver.find_element_by_class_name("MuiButton-label").click()
    print("===========")
    driver.close()
    login()


Register()
