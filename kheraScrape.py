import sys
sys.path
import mechanize
import cookielib
from bs4 import BeautifulSoup
import re
import io
reload(sys);
sys.setdefaultencoding("utf8")

f=open('/Users/robinmalhotra2/Desktop/newfile 2.txt','w')
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# Open some site, let's pick a random one, the first that pops in mind:


from selenium import webdriver
 
path_to_chromedriver = '/Users/robinmalhotra2/Desktop/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url="http://eci.nic.in/archive/Dec2007/pollupd/ac/states/S06/a_index.htm"
browser.get(url)
elem=browser.swirch_to_active_element()
f.write( elem.get_attribute('innerHTML'))
# browser.find_element_by_xpath('/html/frameset/frameset')
# browser.switch_to_frame('state_right_frame')
# elem=browser.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]')
# f.write( elem.get_attribute('innerHTML'))
driver.quit()