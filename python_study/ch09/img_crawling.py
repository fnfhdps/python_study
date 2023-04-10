import requests
import urllib
import time

class TEXT:
    def __init__(self, url):
        self.url = url
        self.html = ''

    def text_ver(self):
        head = {
        'User-Agnet':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0 rv:11.0) like Gecko'
        }
        site = requests.get(self.url, headers=head)
        self.html = site.text
    
    def text_find(self, text):
        #for i in range(n):
        pos = self.html.find(text)
        self.html = self.html[pos+1:]
    
    def text_core(self, text1, text2, n1=0, n2=0, cho=1):
        find1 = self.html.find(text1) + n1
        self.html = self.html[find1:]
        find2 = self.html.find(text2)
        core = self.html[: find2+n2]
        if cho == 1:
            self.html = self.html[find2+1:]
        return core

class IMG_SAVE:
    def __init__(self, img_url, fname):
        self.img_url = img_url
        self.fname = fname

    def img_save(self):
        try:
            print(self.img_url)
            urllib.request.urlretrieve(self.img_url, self.fname)
        except Exception as e:
            print(self.img_url, self.fname, e)

class delay:
    def __init__(self, n):
        self.n = n
        time.sleep(self.n)
