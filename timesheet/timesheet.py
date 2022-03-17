import time
from selenium import webdriver

List =[]

# code for opening the url and login
driver = webdriver.Chrome(executable_path='C:/Users/crochet/PycharmProjects/First-test/Chrome/chromedriver11.exe')
url1=driver.get('https://bitsinglass.mydsr.co.in/home')
driver.maximize_window()
em=driver.find_element_by_xpath("//input[@id='username']")
em.send_keys('manisha.bahuguna@bitsinglass.com')
em=driver.find_element_by_xpath("//input[@id='password']")
em.send_keys('Admin123#')
bt=driver.find_element_by_xpath("//div[@class='form-group clearfix']/input[@id='submit']").click()
time.sleep(4)

#--------------------
Dict = {}
ListLeaveID = []
ListDuration = []
ListType=[]
ListStartDate = []
ListEndDate=[]


driver.find_element_by_xpath("//span[contains(text(), 'Leaves')]").click()
Cols = driver.find_elements_by_xpath("//tr[@class='odd gradeX']")
length=len(Cols)
print(length)

for k in range(6):
    Cols = driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/thead/tr/th[" + str(k+1) +"]").text
    print(Cols)

for j in range(length):
    LeaveID=driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/tbody/tr["+str(j+1)+"]/td[2]").text
    ListLeaveID.append(LeaveID)

    Duration = driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/tbody/tr[" + str(j+1) + "]/td[3]").text
    ListDuration.append(Duration)

    Type = driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/tbody/tr[" + str(j+1) + "]/td[4]").text
    ListType.append(Type)

    StartDate = driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/tbody/tr[" + str(j+1) + "]/td[5]").text
    ListStartDate.append(StartDate)

    EndDate = driver.find_element_by_xpath("//table[@class='table  table-bordered table-hover']/tbody/tr[" + str(j+1) + "]/td[6]").text
    ListEndDate.append(EndDate)


print(ListLeaveID)
print(ListDuration)
print(ListType)
print(ListStartDate)
print(ListEndDate)
driver.close()

