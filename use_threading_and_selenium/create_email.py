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
	# driver.find_element_by_xpath('//*[@title="Sign Up"]').click()
	# time.sleep(2)
	# driver.find_element_by_xpath('//*[@id="signup-plans"]/div[5]/div[1]/div[1]/div/div[3]/i[1]').click()
	# time.sleep(2)
	# driver.find_element_by_xpath('//*[@id="freePlan"]').click()
	driver.find_element_by_id('username').send_keys(username)
	driver.find_element_by_id('password').send_keys(passwd)
	driver.find_element_by_id('passwordc').send_keys(passwd)

loop_counter = 0
for k, v in user_pass.items():
	t = threading.Thread(target=create_email, args=(k,v))
	t.start()
	loop_counter += 1
	print(loop_counter)
	if loop_counter > 4:
		break

# for k,v in asyncio.as_completed(user_pass.items()):
#     result = await k,v
#     create_email(k, v)

# username = [k for k,v in user_pass.items() ]
# password = [v for k,v in user_pass.items() ]
