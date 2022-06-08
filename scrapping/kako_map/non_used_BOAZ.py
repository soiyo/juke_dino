import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import chromedriver_autoinstaller

# chromedriver의 path 설정 후 실행
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

driver.maximize_window()

df = pd.read_csv(
    "/Users/raymond/Documents/Python/scrapping/Untitled", index_col=0
)  # 열을 0번째 인덱스으로 하겠다.

items = ["강남역 맛집", "성수역 맛집"]
count = 0
current = 0
goal = len(items)
for item in items:
    current += 1
    print("진행상황 : ", current, "/", goal, sep="")
    # 리뷰가 없을 때의 코드
    driver.get("https://map.kakao.com/")  # 카카오 지도 접속하기
    searchbox = driver.find_element_by_xpath(
        "//input[@id='search.keyword.query']"
    )  # 검색창에 입력하기
    searchbox.send_keys(item)
    time.sleep(2)
    searchbutton = driver.find_element_by_xpath(
        "//button[@id='search.keyword.submit']"
    )  # 검색버튼 누르기
    driver.execute_script("arguments[0].click();", searchbutton)
    time.sleep(2)

    if len(driver.find_elements_by_xpath("//a[@class='moreview']")) != 0:
        print("식당 존재")
        driver.execute_script('window.open("about:blank", "_blank");')  # 새 탭 열기
        reviewbutton = driver.find_element_by_xpath("//a[@class='numberofscore']")
        time.sleep(2)
        content_url = reviewbutton.get_attribute("href")
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])  # 새 탭으로 이동
        driver.get(content_url)  # 링크 열기
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        review_lists = soup.select(".list_evaluation > li")
        print(len(review_lists))
        if len(review_lists) != 0:
            for i, review in enumerate(review_lists):
                user_review = review.select(".txt_comment > span")  # 리뷰
                rating = review.select(".grade_star > em")  # 별점
                try:
                    img_url = review_lists[i].select_one("a.link_photo > img ")["src"]
                except:
                    continue
                user_id = review.select(
                    ".append_item > a[data-userid]"
                )  # user 정보 html 파싱
                timestamp = review.select(" div > span.time_write")  # 시간정보
                try:
                    row = {
                        "UserID": user_id[0].get("data-userid"),
                        "ItemID": item,
                        "Rating": rating[0].text,
                        "Timestamp": timestamp[0].text,
                    }
                    row = pd.DataFrame(row, index=[i])
                    rating_df = rating_df.append(row, ignore_index=True)
                    review_row = {"ItemID": item, "review": user_review[0].text}
                    review_row = pd.DataFrame(review_row, index=[i])
                    review_elem = review_elem.append(review_row, ignore_index=True)
                    try:
                        img_row = {
                            "UserID": user_id[0].get("data-userid"),
                            "ItemID": item,
                            "img_url": img_url,
                        }
                        img_row = pd.DataFrame(img_row, index=[i])
                        img_elem = img_elem.append(img_row, ignore_index=True)
                    except:
                        img_row = {"UserID": None, "ItemID": item, "img_url": None}
                        img_row = pd.DataFrame(img_row, index=[i])
                        img_elem = img_elem.append(img_row, ignore_index=True)

                    time.sleep(3)
                except:
                    row = {
                        "UserID": None,
                        "ItemID": item,
                        "Rating": None,
                        "Timestamp": timestamp[0].text,
                    }
                    row = pd.DataFrame(row, index=[i])
                    rating_df = rating_df.append(row, ignore_index=True)
                    review_row = {"ItemID": item, "review": user_review[0].text}
                    review_row = pd.DataFrame(review_row, index=[i])
                    review_elem = review_elem.append(review_row, ignore_index=True)
                    try:
                        img_row = {
                            "UserID": user_id[0].get("data-userid"),
                            "ItemID": item,
                            "img_url": img_url,
                        }
                        img_row = pd.DataFrame(img_row, index=[i])
                        img_elem = img_elem.append(img_row, ignore_index=True)
                    except:
                        img_row = {
                            "UserID": user_id[0].get("data-userid"),
                            "ItemID": item,
                            "img_url": None,
                        }
                        img_row = pd.DataFrame(img_row, index=[i])
                        img_elem = img_elem.append(img_row, ignore_index=True)
                    time.sleep(1)

        else:
            print("리뷰가 없습니다")

        try:
            for i in range(2, 500):
                time.sleep(3)
                another_review = driver.find_element_by_xpath(
                    "//a[@data-page='" + str(i) + "']"
                )
                another_review.click()
                time.sleep(3)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                review_lists = soup.select(".list_evaluation > li")
                if len(review_lists) != 0:
                    for i, review in enumerate(review_lists):
                        user_review = review.select(".txt_comment > span")  # 리뷰
                        rating = review.select(".grade_star > em")  # 별점
                        try:
                            img_url = review_lists[i].select_one("a.link_photo > img ")[
                                "src"
                            ]
                        except:
                            continue
                        user_id = review.select(
                            ".append_item > a[data-userid]"
                        )  # user 정보 html 파싱
                        timestamp = review.select(" div > span.time_write")  # 시간정보
                        try:
                            row = {
                                "UserID": user_id[0].get("data-userid"),
                                "ItemID": item,
                                "Rating": rating[0].text,
                                "Timestamp": timestamp[0].text,
                            }
                            row = pd.DataFrame(row, index=[i])
                            rating_df = rating_df.append(row, ignore_index=True)
                            review_row = {
                                "UserID": user_id[0].get("data-userid"),
                                "ItemID": item,
                                "review": user_review[0].text,
                            }
                            review_row = pd.DataFrame(review_row, index=[i])
                            review_elem = review_elem.append(
                                review_row, ignore_index=True
                            )
                            try:
                                img_row = {
                                    "UserID": user_id[0].get("data-userid"),
                                    "ItemID": item,
                                    "img_url": img_url,
                                }
                                img_row = pd.DataFrame(img_row, index=[i])
                                img_elem = img_elem.append(img_row, ignore_index=True)
                            except:
                                img_row = {
                                    "UserID": user_id[0].get("data-userid"),
                                    "ItemID": item,
                                    "img_url": None,
                                }
                                img_row = pd.DataFrame(img_row, index=[i])
                                img_elem = img_elem.append(img_row, ignore_index=True)
                            time.sleep(1)

                        except:
                            row = {
                                "UserID": None,
                                "ItemID": item,
                                "Rating": None,
                                "Timestamp": timestamp[0].text,
                            }
                            row = pd.DataFrame(row, index=[i])
                            rating_df = rating_df.append(row, ignore_index=True)
                            review_row = {
                                "UserID": user_id[0].get("data-userid"),
                                "ItemID": item,
                                "review": user_review[0].text,
                            }
                            review_row = pd.DataFrame(review_row, index=[i])
                            review_elem = review_elem.append(
                                review_row, ignore_index=True
                            )
                            try:
                                img_row = {
                                    "UserID": user_id[0].get("data-userid"),
                                    "ItemID": item,
                                    "img_url": img_url,
                                }
                                img_row = pd.DataFrame(img_row, index=[i])
                                img_elem = img_elem.append(img_row, ignore_index=True)
                            except:
                                img_row = {
                                    "UserID": user_id[0].get("data-userid"),
                                    "ItemID": item,
                                    "img_url": None,
                                }
                                img_row = pd.DataFrame(img_row, index=[i])
                                img_elem = img_elem.append(img_row, ignore_index=True)

        except:
            print("더 이상 리뷰 존재 X")
            driver.close()
        driver.switch_to.window(tabs[0])
        print("기본 페이지로 돌아가자")

    else:
        print("식당 존재 x")
