import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url= input('Enter - ')
data= urllib.request.urlopen(url).read().decode()
#print(type('data'))

#data ='''<commentinfo>tag</commentinfo>'''
#print("~~~",data)
c=0
commentsinfo = ET.fromstring(data)#starting tag. ie is "commentinfo" in this case
lst = commentsinfo.findall('comments/comment')#and thge path.ie "commentinfo/comments/comment"
#print("$$",type('lst'))
print('User count:', len(lst))

for item in lst:
    #print('Name', item.find('name').text)    #get the txt btw <name> tag
    #print('count', item.find('count').text)  #get the txt btw <count> tag
    c=c+int(item.find('count').text)

print("sum :",c)

#http://py4e-data.dr-chuck.net/comments_42.xml in this case 2553
#http://py4e-data.dr-chuck.net/comments_967204.xml in this case 2212
