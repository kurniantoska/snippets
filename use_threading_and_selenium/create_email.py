from selenium import webdriver
import time
import json
import threading

with open('test.json') as json_data:
   user_pass = json.load(json_data)


def create_email(username:str, passwd:str):
	url_create_email = 'https://mail.protonmail.com/create/new?language=en'

	driver = webdriver.Chrome('D:\master\webdriver\chromedriver_win32\chromedriver.exe')
	driver.get(url_create_email)
	
	print(driver.session_id)

	driver.find_element_by_id('username').send_keys(username)
	time.sleep(2)
	driver.find_element_by_id('password').send_keys(passwd)
	time.sleep(2)
	driver.find_element_by_id('passwordc').send_keys(passwd)
	time.sleep(2)
	driver.find_element_by_class_name('signUpProcess-btn-create').click()

loop_counter = 0
for k, v in user_pass.items():
	# use Thread(target=functions, args=(argument for functions))
	t = threading.Thread(target=create_email, args=(k,v))
	t.start()
	loop_counter += 1
	print(loop_counter)
	if loop_counter > 4:
		break

# use join to stop the thread		
t.join()

# source : https://www.simplifiedpython.net/python-threading-example/
