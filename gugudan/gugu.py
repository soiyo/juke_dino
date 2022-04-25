# # 2단
# for i in range(1, 11):
#     result = 2*i
#     print(f'구구단을 외자! {2}*{i}={result}')

# 1단~10단
for i, num in enumerate(range(1, 11)):
    for i in range(1, 11):
        print(f'구구단을 외자! {num}*{i}={num*i}')


# # 1단~10단 정렬(fstring 이용해서)
# for i, num in enumerate(range(1, 11)):
#     for i in range(1, 11):
#         print(f'구구단을 외자! {num:>2}*{i}={num*i}')
