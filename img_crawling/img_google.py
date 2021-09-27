from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver import Edge
import StringIO
import tempfile
import requests
import zipfile
import time

# s = requests.Session()
plusUrl = "풍경"
# baseUrl = 'https://www.google.com/search?q={}&tbm=isch&ved='.format(quote_plus(plusUrl))
crawl_num = 40
url = 'https://www.google.com/search?q={}&tbm=isch&ved='.format(quote_plus(plusUrl))  # 한글 검색 자동 변환
# url = s.get(plusUrl).text
# driver = webdriver.Chrome('C:\\Users\\argos\\Downloads\\chromedriver_win32\\chromedriver.exe')
# driver = Edge(executable_path='/path/to/MicrosoftWebDriver.exe')
# driver = webdriver.Ie(executable_path='/path/to/IEDriverServer.exe')
download_url = 'https://msedgedriver.azureedge.net/94.0.992.31/edgedriver_win64.zip'
# file_name = download_url.split('/')[-1]
with tempfile.mkstemp(suffix='.zip',prefix='edgedriver_win64') as f:
    b = requests.get(download_url, stream=True, verify=False)
    f.write(b)
    a = zipfile.ZipFile(f).extractall()
    driver = webdriver.Edge(a)
    driver.get(url)
# time.sleep(5)
url = driver.page_source

soup = bs(url, "html.parser")

img = soup.find_all('img' ,class_="rg_i Q4LuWd")
# img = soup.select('img._image._listImage')

print(img)
n = 1
for i in img:
    print(i)
    try:
        imgUrl = i['src']
    except:
        imgUrl = i['data-src']

    im = 'goo_output\img' + str(n) + '.jpg'

    with urlopen(imgUrl) as f ,open(im, 'wb') as h:  # w - write b - binary
        img = f.read()
        h.write(img)
    n += 1
    if n > crawl_num:
        break
    # time.sleep(0.1)

driver.quit()

print('Image Crawling is done.')