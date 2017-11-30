			
from selenium import webdriver				
				
driver=webdriver.Chrome()				
				
driver.get ("https://www.baidu.com/")				
baiduserach=driver.find_element_by_id("kw")				
baiduserach.send_keys("helloworld")	
driver.quit()		
driver.close()