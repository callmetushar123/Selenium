from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


#name = input("Enter the  username")
#password = input("Enter the password")
name = ""
password = ""
if name== "" and  password =="":
    name = input("Enter the username: ")
    #password = input("Enter the password: ")
    #print("Enter the password: ")
    password = getpass.getpass()
else:
    pass

driver = webdriver.Chrome(executable_path=r"C:/Users/Tushar/Desktop/chromedriver.exe")
#time.sleep(2)
driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession")


user = driver.find_element_by_id("identifierId")
user.send_keys(name)
button = driver.find_element_by_id("identifierNext").click()
time.sleep(2)

p = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
p.send_keys(password)
buttom = driver.find_element_by_id("passwordNext").click()



##pasword field
#//*[@id="password"]/div[1]/div/div[1]/input
##username field
#//*[@id="identifierId"]

#first next
#//*[@id="identifierNext"]/span/span

##last next
##//*[@id="passwordNext"]/span
