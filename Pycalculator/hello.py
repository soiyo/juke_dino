# 계산기 만들기
import imp
import tkinter as tk  # gui 모듈 포함

window = tk.Tk()  # 창 생성

# 위젯 생성 및 적용
window.title('계산기')

operator = 'none'
calculation = 0


def button_click(key=0):
    global num1, num2
    if operator == 'none':
        if print_value.get() == '0':
            print_value.set(str(key))
            num1 = key
        else:
            num1 *= 10
            num1 += key
            print_value.set(str(num1))
    else:
        if print_value.get() == '0' or num2 == 0:
            print_value.set(str(key))
            num2 = key
        else:
            num2 *= 10
            num2 += key
            print_value.set(str(num2))


def operator_click(op):
    global operator
    operator = op


def calculate():
    global num1, num2, operator
    if operator == '+':
        calculation = num1 + num2
    elif operator == '-':
        calculation = num1 - num2
    else:
        calculation = 0

    print_value.set(str(calculation))
    num1 = 0
    num2 = 0
    operator = 'none'


def initalize():
    global num1, num2, operator
    num1 = 0
    num2 = 0
    operator = 'none'
    print_value.set('0')


# 0열
# 출력 창
num1, num2 = 0, 0
print_value = tk.StringVar()
print_value.set(0)
display = tk.Entry(window, width=30, textvariable=print_value,
                   justify='right').grid(columnspan=5, row=0)
# 1열
button = tk.Button(window, text='1', width=10, height=5,
                   command=lambda: button_click(1)).grid(column=0, row=1)
button = tk.Button(window, text='2', width=10, height=5,
                   command=lambda: button_click(2)).grid(column=1, row=1)
button = tk.Button(window, text='3', width=10, height=5,
                   command=lambda: button_click(3)).grid(column=2, row=1)
button = tk.Button(window, text='C', width=10, height=5,
                   command=initalize).grid(column=3, row=1)
# 2열
button = tk.Button(window, text='4', width=10, height=5,
                   command=lambda: button_click(4)).grid(column=0, row=2)
button = tk.Button(window, text='5', width=10, height=5,
                   command=lambda: button_click(5)).grid(column=1, row=2)
button = tk.Button(window, text='6', width=10, height=5,
                   command=lambda: button_click(6)).grid(column=2, row=2)
button = tk.Button(window, text='+', width=10, height=5,
                   command=lambda: operator_click('+')).grid(column=3, row=2)
# 3열
button = tk.Button(window, text='7', width=10, height=5,
                   command=lambda: button_click(7)).grid(column=0, row=3)
button = tk.Button(window, text='8', width=10, height=5,
                   command=lambda: button_click(8)).grid(column=1, row=3)
button = tk.Button(window, text='9', width=10, height=5,
                   command=lambda: button_click(9)).grid(column=2, row=3)
button = tk.Button(window, text='-', width=10, height=5,
                   command=lambda: operator_click('-')).grid(column=3, row=3)
# 4열
button = tk.Button(window, text='0', width=10, height=5,
                   command=lambda: button_click(0)).grid(column=0, row=4)
button = tk.Button(window, text='=', width=10, height=5,
                   command=calculate).grid(column=3, row=4)

# 여기까지 위젯 생성 및 적용
window.mainloop()  # 창 닫을때까지 실행

# reference : https://blog.naver.com/cflab/221965735770
