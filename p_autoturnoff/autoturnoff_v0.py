import tkinter as tk
import os


win = tk.Tk()  # 建立主視窗  注意: 檔名不要取import的名字 盡量不要把自己寫的 .py 文件取作存在的 module 名稱, 因為在 import 的時候, python 會先找尋當下的目錄並且載入該文件作為 module, 這自然不是我們要的XD

win.title('自動關機')  # 視窗名稱
win.geometry('800x600')  # 大小
win.configure(background='white')  # 背景顏色

# function部分


def cal_time_btm():  # 自動關機區塊
    get_min = float(minute_entry.get())
    get_sec = float(second_entry.get())
    total_sec = str(int(get_min*60+get_sec))
    result = '你的電腦將會在{}秒後關機'.format(total_sec)
    result_label.configure(text=result)

    cmd = 'shutdown -s -t '+total_sec

    os.system(cmd)


def cancel_btm():  # 取消自動關機區塊
    cmd1 = 'shutdown -a'
    os.system(cmd1)


header_label = tk.Label(win, text='這是一個計時器')
header_label.pack()

minute_frame = tk.Frame(win)  # 以下為minute_frame 群組

minute_frame.pack(side=tk.TOP)
minute_label = tk.Label(minute_frame, text='分')
minute_label.pack(side=tk.LEFT)
minute_entry = tk.Entry(minute_frame)
minute_entry.pack(side=tk.LEFT)  # 以上對齊父元件

second_frame = tk.Frame(win)
second_frame.pack(side=tk.TOP)
second_label = tk.Label(second_frame, text='秒')
second_label.pack(side=tk.LEFT)
second_entry = tk.Entry(second_frame)
second_entry.pack(side=tk.LEFT)

result_label = tk.Label(win)
result_label.pack()

calculate_btn = tk.Button(
    win, text='馬上執行', command=cal_time_btm)  # command綁定按鈕按下後事件
calculate_btn.pack()

cancel_btm = tk.Button(win, text='取消關機', command=cancel_btm)
cancel_btm.pack()

win.mainloop()  # 常駐主視窗
