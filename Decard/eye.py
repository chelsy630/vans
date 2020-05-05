from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time
#設定webdriver及
driver = webdriver.Chrome('C:/Users/User/Downloads/chromedriver.exe')
url = 'https://www.dcard.tw/f'
driver.get(url)

inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('python')


driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)
html = driver.page_source
soup =bs(html,'html.parser')
meta_data = []
#獲得文章的看板、作者、時間
for x in soup.find_all('span',{'class':'sc-6oxm01-2 hiTIMq'}):
    meta_data.append((x.text.strip()))
print(meta_data)
forums =[] #找到看板
author =[] #找到作者
time =[]
for i in range(len(meta_data)):
    if i %3 ==0:
        forums.append(meta_data[i])
    if i %3 ==1:
        author.append(meta_data[i])
    if i %3 ==2:
        time.append(meta_data[i])
titles = []
for x in soup.find_all('h2',{'class':'sc-1v1d5rx-3 eihOFJ'}):
    titles.append(x.text)
# print(titles)
herfs = []
for x in soup.find_all('a',{'class':'sc-1v1d5rx-4 gCVegi'}):
    herfs.append(x['href'])
links = []
for herf in herfs:
    links.append(urljoin(url,herf))
print(links)

# for i in range(len(forums)):
    # print(forums[i],titles[i],links[i])
