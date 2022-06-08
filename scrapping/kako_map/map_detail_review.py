import pandas as pd

# Jupyternotebook(또는 ipython)에서 경고 메시지를 무시하고 싶을 때:
# import warnings
# warnings.filterwarnings("ignore")
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import chromedriver_autoinstaller

###################################
# 🔎 검색어를 입력하세요
query = "마포구청역 맛집"
###################################


# chromedriver의 path 설정 후 실행
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

columns = [
    "personal_star",
    "review",
    "url",
    "title",
    "category",
    "total_star",
    "location",
]
df = pd.DataFrame(columns=columns)


# 크롤링할 사이트 주소를 정의합니다.
source_url = "https://map.kakao.com/"


# 카카오 지도에 접속합니다
driver.get(source_url)

# 검색창에 검색어를 입력합니다
searchbox = driver.find_element_by_xpath("//input[@id='search.keyword.query']")
searchbox.send_keys(query)

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
titles = soup.find_all(name="a", attrs={"class": "link_name"})
categories = soup.find_all(name="span", attrs={"class": "subcategory clickable"})
total_stars = soup.find_all(name="em", attrs={"class": "num"})
# print(stars)

# a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.
page_urls = []
page_names = []
page_categories = []
page_total_stars = []

for title, moreview, category, total_star in zip(
    titles, moreviews, categories, total_stars
):
    page_name = title.get_text()
    # print(page_name)
    page_names.append(page_name)
    # print(page_names)

    page_url = moreview.get("href")
    # print(page_url)
    page_urls.append(page_url)
    # print(page_urls)

    page_category = category.get_text()
    # print(page_category)
    page_categories.append(page_category)
    # print(page_categories)

    page_total_star = total_star.get_text()
    page_total_stars.append(page_total_star)

for page_url, page_name, page_category, page_total_star in zip(
    page_urls, page_names, page_categories, page_total_stars
):  # 두 개의 변수를 받아
    # print(page_name, page_url)

    # 상세보기 페이지에 접속합니다
    driver.get(page_url)
    time.sleep(2)

    # 첫 페이지 리뷰를 크롤링합니다
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    contents_div = soup.find(name="div", attrs={"class": "evaluation_review"})

    location = soup.find(name="span", attrs={"class": "txt_address"})  # 위치를 가져옵니다.
    loacation_big = location.text.split(" ")[:2][0]
    loacation_small = location.text.split(" ")[:2][1].replace("/n", "")
    full_location = loacation_big + " " + loacation_small
    print(full_location, end="")
    try:
        # 별점을 가져옵니다.
        rates = contents_div.find_all(name="em", attrs={"class": "num_rate"})
        # 리뷰를 가져옵니다.
        reviews = contents_div.find_all(name="p", attrs={"class": "txt_comment"})
    except AttributeError as e:  # 별점, 리뷰 없을때 pass
        pass

    for rate, review in zip(rates, reviews):
        row = [
            rate.text[0],
            review.find(name="span").text,
            page_url,
            page_name,
            page_category,
            page_total_star,
            full_location,
        ]  # 넣을 데이터
        series = pd.Series(row, index=df.columns)
        df = df.append(series, ignore_index=True)

    # 2-3페이지의 리뷰를 크롤링합니다
    for button_num in range(2, 3):
        # 오류가 나는 경우(리뷰 페이지가 없는 경우), 수행하지 않습니다.
        try:
            another_reviews = driver.find_element_by_xpath(
                "//a[@data-page='" + str(button_num) + "']"
            )
            another_reviews.click()
            time.sleep(2)

            # 페이지 리뷰를 크롤링합니다
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            contents_div = soup.find(name="div", attrs={"class": "evaluation_review"})

            # 별점을 가져옵니다.
            rates = contents_div.find_all(name="em", attrs={"class": "num_rate"})

            # 리뷰를 가져옵니다.
            reviews = contents_div.find_all(name="p", attrs={"class": "txt_comment"})

            for rate, review in zip(rates, reviews):
                row = [rate.text[0], review.find(name="span").text]
                series = pd.Series(row, index=df.columns)
                df = df.append(series, ignore_index=True)
        except:
            break

driver.close()

# 4점 이상의 리뷰는 긍정 리뷰, 3점 이하의 리뷰는 부정 리뷰로 평가합니다.
df["label"] = df["personal_star"].apply(lambda x: 1 if float(x) > 3 else 0)
# print(df.shape)
# print(df.head())

df.to_csv("kakao({}).csv".format(query), index=False)

print("csv 파일 생성 완료!")
