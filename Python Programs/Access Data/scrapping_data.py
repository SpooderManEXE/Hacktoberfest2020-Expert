import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Sample links:
# http://py4e-data.dr-chuck.net/comments_42.html (o/p: Count=50, Sum=2553)
# http://py4e-data.dr-chuck.net/comments_975457.html (o/p: Count=50, Sum=2726)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter - ')
if len(url)<1: url='http://py4e-data.dr-chuck.net/comments_42.html' #Default URL
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
sum=0
count=0
for tag in tags :
	count = count + 1
	sum = sum + int(tag.contents[0])
print('Count',count)
print('Sum',sum)