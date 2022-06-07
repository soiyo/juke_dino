import pandas as pd  # 데이터프레임 처리 모듈

query = "서초구맛집"

df = pd.read_csv("naver(서초구 맛집).csv")["data"]  # 파싱한 csv파일 불러오기
title = pd.read_csv("naver(서초구 맛집).csv")["title"]  # 파싱한 csv파일 불러오기

delete_stars = df[~df.str.contains("별점")].index  # 별점 없는 행 지우기
refined_df = df.drop(index=delete_stars, axis=0)
refined_title = title.drop(index=delete_stars, axis=0)

data_list = refined_df.values.tolist()

for i in range(len(data_list)):
    # 별점 숫자 앞 제거
    data_list[i] = data_list[i].split("별점")[1]
    data_list[i] = data_list[i].split("\n")[1]

    # 나머지 한글 제거
    data_list[i] = data_list[i].replace("방문자리뷰", "").replace("블로그리뷰", "")

    # 별점, 방문자리뷰, 저장수 분리
    data_list[i] = data_list[i].split(" ")

rating = []
review = []
save = []

for i in range(len(data_list)):
    rating.append(data_list[i][0])
    review.append(data_list[i][1])
    save.append(data_list[i][2])


# # 데이터 프레임 만들기
mydata = {
    "title": refined_title,
    "stars": rating,
    "review": review,
    "visitor_save": save,
}
store_frame = pd.DataFrame(mydata)
print(store_frame)

# # data 컬럼 삭제

# # naver_df = naver_df.drop(["data"], axis=1)
store_frame.to_csv("naver({}).csv".format(query), encoding="utf-8-sig")
