import time
import sys
import os

import pandas as pd
import numpy as np

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import warnings

warnings.filterwarnings("ignore")

# 검색어 입력
# guery = input('검색지역? ')
query = "서초구 맛집"

path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)
driver.get(
    f"https://map.naver.com/v5/search/{query}?c=14203933.7141038,4562681.4505997,10,0,0,0,dh"
)

# 검색결과 iframe 접근
driver.switch_to.frame("searchIframe")

# 처음 돌릴 땐 자료 60개 수집..
# 1페이지로 돌아간 뒤 한번 더 돌리면 300개 정도 추출됨 (검색 결과 많은 경우)


title_list = []
f_data_list = []

try:
    for i in range(1, 7):
        driver.find_element_by_link_text(str(i)).click()
        try:
            for j in range(3, 70, 3):
                element = driver.find_elements_by_css_selector(".OXiLu")[j]
                ActionChains(driver).move_to_element(element).key_down(
                    Keys.PAGE_DOWN
                ).key_up(Keys.PAGE_DOWN).perform()
        except:
            pass

        # 가게이름
        title_raw = driver.find_elements_by_css_selector(".OXiLu")
        for title in title_raw:
            title = title.text
            title_list.append(title)

        # 평점 등 데이터
        data_raw = driver.find_elements_by_css_selector("._17H46")
        for data in data_raw:
            data = data.text
            f_data_list.append(data)

except:
    pass

print(len(title_list), len(f_data_list))

# 데이터 프레임 만들기
df = pd.DataFrame({"title": title_list, "data": f_data_list})


df.to_csv("naver({}).csv".format(query), encoding="utf-8-sig")
