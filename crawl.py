import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import openpyxl


search = input("검색할 키워드를 입력해주세요:")

page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만입력):"))
print("크롤링할 페이지: ", page, "페이지")

page_num = 0

if page == 1:
    page_num = 1
elif page == 0:
    page_num = 1
else:
    page_num = page+9*(page-1)


url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + \
    search + "&start=" + str(page_num)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75"}

original_html = requests.get(url, headers=headers)
html = BeautifulSoup(original_html.text, "html.parser")

articles = html.select("div.group_news > ul.list_news > li div.news_area > a")

news_title = []
for i in articles:
    news_title.append(i.attrs['title'])
print(news_title, "\n")

df = pd.DataFrame(data=news_title, columns=["기사"])
df
df.to_excel("main_news.xlsx")
