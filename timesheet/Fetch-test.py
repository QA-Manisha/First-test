import time
from selenium import webdriver
import random
import string

Error =[]
# code for opening chrome
driver = webdriver.Chrome(executable_path='C:/Users/crochet/PycharmProjects/First-test/Chrome/chromedriver11.exe')

# code for opening URL
driver.get('https://bitsinglass.mydsr.co.in/home')
driver.maximize_window()

for l in range(2):
       #Random Username entered
       un=driver.find_element_by_xpath("//input[@id='username']")
       username=''.join(random.choice(string.ascii_letters) for x in range(8))
       un.send_keys(username+"@gmail.com")
       # Random password of length 8 with letters, digits, and symbols---
       pwd=driver.find_element_by_xpath("//input[@id='password']")
       password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8))
       pwd.send_keys(password)
       # Click on submit button
       driver.find_element_by_xpath("//div[@class='form-group clearfix']/input[@id='submit']").click()
       errormsg= driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
       Error.append(errormsg)
val=[]
for val in Error:
    if val == ",":
        break
    print(val)
time.sleep(1)
driver.close()


# em=driver.find_element_by_xpath("//input[@id='username']")
# em.send_keys('manisha.bahuguna@bitsinglass.com')
# em=driver.find_element_by_xpath("//input[@id='password']")
# em.send_keys('Admin123#')
# bt=driver.find_element_by_xpath("//div[@class='form-group clearfix']/input[@id='submit']").click()



