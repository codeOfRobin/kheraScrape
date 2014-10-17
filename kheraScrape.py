import mechanize
import cookielib
from bs4 import BeautifulSoup
import re
import io
import sys
import csv
reload(sys)
sys.setdefaultencoding("utf8")

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
for x in xrange(1,182):
	preurl='http://eci.nic.in/archive/Dec2007/pollupd/ac/states/S06/Aconst'
	if (x<10):
		url=preurl+'0'+str(x)+'.htm'
	else:
		url=preurl+str(x)+'.htm'
	r = br.open(url)
	html = r.read()
	html=br.response().read();
	parsed_html = BeautifulSoup(html,'html.parser')
	tableList=parsed_html.find_all('table')
	bList=parsed_html.find_all('b')#insert KRK joke here
	print bList[3].font.string

	#extract polling percentage
	table1=tableList[1]
	strongs2=table1.find_all('strong')
	print strongs2[-1].string#gives last element

	#extract lead
	table2=tableList[2]
	strongs=table2.find_all('strong')
	print strongs[-4].string
	print strongs[-1].string

	with open('eggs.csv', 'a') as csvfile:
	    spamwriter = csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_ALL)
	    spamwriter.writerow([bList[3].font.string,strongs2[-1].string,strongs[-4].string,strongs[-1].string,float(strongs[-1].string)/float(strongs[-4].string)])
