# %matplotlib inline # notebook을 실행한 브라우저에서 바로 그림을 볼 수 있게 해주는 것

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Jupyternotebook(또는 ipython)에서 경고 메시지를 무시하고 싶을 때:
import warnings

warnings.filterwarnings("ignore")
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import chromedriver_autoinstaller

# chromedriver의 path 설정 후 실행
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

# 크롤링할 사이트 주소를 정의합니다.
source_url = "https://map.kakao.com/"


# 카카오 지도에 접속합니다
driver.get(source_url)

# 검색창에 검색어를 입력합니다
searchbox = driver.find_element_by_xpath("//input[@id='search.keyword.query']")
searchbox.send_keys("강남역 고기집")

# 검색버튼을 눌러서 결과를 가져옵니다
searchbutton = driver.find_element_by_xpath("//button[@id='search.keyword.submit']")
driver.execute_script("arguments[0].click();", searchbutton)

# 검색 결과를 가져올 시간을 기다립니다
time.sleep(2)

# 검색 결과의 페이지 소스를 가져옵니다
html = driver.page_source

# BeautifulSoup을 이용하여 html 정보를 파싱합니다
soup = BeautifulSoup(html, "html.parser")
moreviews = soup.find_all(name="a", attrs={"class": "moreview"})

# a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.
page_urls = []
for moreview in moreviews:
    page_url = moreview.get("href")
    print(page_url)
    page_urls.append(page_url)

# 크롤링에 사용한 브라우저를 종료합니다.
driver.close()
