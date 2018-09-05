import time,os
import requests
import random
from selenium import webdriver

# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 17:01
# @Author  : Shoo Zhao

import json
import re,zipfile,os
str1 = '<a href="/Right/DraftAction.do?processID=detail&amp;draftId=75472" target="_blank" style="color:#00a7ad;">Hourly&nbsp;News&nbsp;2018-08-22&nbsp;14:00:15</a>'
print(str1)

res = re.findall('>(.*?)</a>' , str1)
print(res)
print(type(res))
print(res[0])
newstr = res[0].replace('&nbsp;', ' ')
print(newstr)

res2 = re.match('>(.*?)</a>', str1)
print(res2)



line = 'Cate is a cat are gold'

re3 = re.match(r'(.*) is (.*) are (.*)',line)
if re3:
    print(re3.group())
    print(re3.group(1))
    print(re3.group(2))
    print(re3.group(3))

import re
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))

s = 'd a f'

print(s.split(' '))
a=re.sub(' ','',s)
print(a)


list1 = [2,3,5]

list2=[1,2,3,4,5,6,7,8,9,10]
print(list2[0:-1:3])
for i in list2[2:-1:3]:
    print(i)

if (0 in list2)& (9 in list2):
    print('true')
else:
    print('false')

z = zip(list2)
print(z)
print(type(z))
# f = zipfile.ZipFile(r"C:\Users\shoo\Downloads\资源下载.zip",'r')
# for file in f.namelist():
#     print(file)
#     f.extract(file,'./')

# f = zipfile.ZipFile(r"C:\Users\shoo\AppData\Local\Temp\资源下载.zip", 'r')
# for file in f.namelist():
#     f.extract(file, r'C:\Users\shoo\Downloads')

# 检查zip文件是否存在
my_file = r"C:\Users\shoo\AppData\Local\Temp\资源下载.zip"
if os.path.exists(my_file):
    os.remove(my_file)
    print("remove successfully")
else:
    print("no such file:", my_file)

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

def RefushPV(Numpv):

    i=1
    while(i<(Numpv+1)):
        driver.get('https://dazzle.yunshicloud.com/cdv1tmpl/text_detail.html?id=5b358f8894c1ec4dab2b642e&companyId=CDVCLOUD&productId=dazzle&classify=doc&viewType=weixin')
        time.sleep(1)

        try:
            driver.refresh()  #刷新页面的方法
            print('refresh successfully!{0}'.format(i))
        except Exception as e:
            print('Exception found!{}'.format(e))

        i+=1


if __name__=='__main__':
    RefushPV(2000)
    driver.quit()
	
	
	ddddddddddddddddddddddddddddddd
		ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd	ddddddddddddddddddddddddddddddd

