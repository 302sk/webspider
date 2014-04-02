import urllib
import urllib2
import math
import htmllib
from HTMLParser import HTMLParser


fp = open("fileurl.html", "w")
fp.write("<html><head><title>file list</title></head>\n<body>");
flag = 0
startpos = (0,0)
stoppos = (0,0)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            startpos = self.getpos()
            print "Encountered and start tag", startpos, tag
            print "url:", attrs
            flag = 1
    def handle_endtag(self, tag):
        if tag == 'a':
            stoppos = self.getpos()
            print "Encountered and end tag:", stoppos, tag
    def handle_data(self, data):
        if flag == 1:
            print "Encountered some data :", data

parser = MyHTMLParser()
code = 1
print "take over the world!"
url = "http://filex.sdufe.edu.cn/down.php"
for code in range(1, 10):
    value = {'forenter':'',
             'code':code,
             'vcode':0,
             'Submit':'+++%CC%E1%C8%A1+++'
        }
    data = urllib.urlencode(value)
    req = urllib2.Request(url, data)
    try:
        response = urllib2.urlopen(req, timeout = 5)
    except urllib2.URLError, e:
        fp.write("\n</body>\n</html>")
        fp.close()
        raise MyException("There was an error: %r" % e)
    html  = response.read()
 #   parser.feed(html)

    strpos = html.find("<a")
    endpos = html.find("</a>")

    print str(code)
    print html[strpos:endpos+4]
    fp.write(str(code))
    str1 = html[strpos:strpos+9] + "http://filex.sdufe.edu.cn/" #add domain name
    str2 = str1 + html[strpos+9:endpos+4]
    fp.write(str2)
    fp.write("</br>\n")

fp.write("\n</body>\n</html>")
fp.close()
#print html
