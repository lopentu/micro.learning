# python3 crawl.py3 http://www.ltn.com.tw
from sys import argv                
from urllib import request 
from bs4 import BeautifulSoup        

url=argv[1]  # 'http://www.ltn.com.tw'             #先取得目標網址       

def crawl_text(url='http://www.ltn.com.tw'):
    u=request.urlopen(url)                         #根據網址讀取HTML檔案
    html_doc=u.read().decode('utf8')

    raw=BeautifulSoup(markup=html_doc).get_text()           #去除HTML標籤
    for line in raw.split('\n'):
        first_char=line[0]
        if first_char>='一' and first_char<='龜':        #只輸出中文(Unicode)
            print(line)

crawl_text(url=argv[1])
