#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImage(html):
    reg = r'src="(.+?\.png)" alt'
    imgre = re.compile(reg)
    #print(imgre)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.png' % x)
        #print(imgurl)
        x+=1

def getFile(url):
    urllib.urlretrieve(url)

html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")

#print(html)
#getImage(html)
getFile("https://github.com/git-for-windows/git/releases/download/v2.13.3.windows.1/Git-2.13.3-64-bit.exe")