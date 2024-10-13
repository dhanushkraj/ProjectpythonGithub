from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("file:///E:/Python/Sandeep%20Sir/selenium%20complete%20notes/html/iframe.html")
driver.maximize_window()
sleep(3)

driver.switch_to.frame("frame1")

driver.find_element("id", "small-searchterms").send_keys("books")
sleep(2)
driver.find_element("xpath", "//input[@value='Search']").click()
sleep(10)

driver.switch_to.default_content()
sleep(3)

driver.switch_to.frame("frame2")

driver.find_element("id", "visitsupport").click()
sleep(3)

driver.switch_to.default_content()
sleep(3)

driver.switch_to.frame("FR1")

driver.find_element("xpath", "(//a[contains(text(), 'Books')])[1]").click()
sleep(10)














# for company in companies:
#     print(f"{company:>15}", end='')
#
# print()
# print('-' * 55)
#
# while True:
#     for company in companies:
#         share_price = driver.find_element(By.XPATH, f"//a[text()='{company}']/../..//td[7]").text
#         print(f"{share_price:>15}", end="")
#     print()
#     sleep(5)




































