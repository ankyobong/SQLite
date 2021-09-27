import os
import urllib.request
import requests
from PIL import Image
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
import time

# s = requests.Session()
baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusUrl = "풍경"
crawl_num = 40
url = baseUrl + quote_plus(plusUrl)  # 한글 검색 자동 변환
# url = s.get(plusUrl).text
driver = webdriver.Chrome('C:\\Users\\argos\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get(url)
time.sleep(3)
url = driver.page_source
# url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%B0"
# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# html = urlopen(url).read()
soup = bs(url, "html.parser")
# time.sleep(10)
img = soup.find_all('img' ,class_="_image _listImage")
# img = soup.select('img._image._listImage')
# img = soup.find_parents('img')
print(img)
n = 1
for i in img:
    print(i)
    try:
        imgUrl = i['data-lazy-src']
    except:
        imgUrl = i['src']
    im = 'output\img' + str(n) + '.jpg'
    # if not os.path.exists('output\img' + str(n) + '.jpg'):
    #     os.mkdir('output')
    with urlopen(imgUrl) as f ,open(im, 'wb') as h:  # w - write b - binary
        img = f.read()
        h.write(img)
    n += 1
    if n > crawl_num:
        break
    # time.sleep(0.1)

driver.quit()

print('Image Crawling is done.')
