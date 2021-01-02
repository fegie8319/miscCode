import os
import time
import tkinter as tk

window = tk.Tk()

window.title('Auto Turn Off')
window.geometry('300x200')

# 固定視窗大小
window.resizable(0, 0)


# 定義函式
def run_m():
    # 變數處理
    run_min = min_entry.get()
    run_sec = sec_entry.get()

    # user不輸入的防呆
    if len(run_min) == 0:
        run_min = '0'

    if len(run_sec) == 0:
        run_sec = '0'

    total_time = int(run_min) * 60 + int(run_sec)

    final_command = 'shutdown -s -t ' + str(total_time)
    os.system(final_command)


def run_c():
    cancel_command = ' shutdown -a'
    os.system(cancel_command)


def run_leave():
    tk.destroy()


# 畫面顯示值
min_label = tk.Label(window, text="分鐘數:", font=('Arial', 13)).place(x=30, y=10)
sec_label = tk.Label(window, text="秒鐘數:", font=('Arial', 13)).place(x=30, y=40)
# 宣告輸入欄位 min=分鐘,sec=秒數
min_entry = tk.Entry(window, show=None).place(x=100, y=12)
sec_entry = tk.Entry(window, show=None).place(x=100, y=42)

# 宣告按鈕
start_button = tk.Button(window, text='執行', font=('Arial', 12), width=5, height=1, command=run_m).place(x=80, y=100)
cancel_button = tk.Button(window, text='取消', font=('Arial', 12), width=5, height=1, command=run_c).place(x=160, y=100)
leave_button = tk.Button(window, text='離開', font=('Arial', 12), width=5, height=1, command=run_leave).place(x=220, y=150)

# 擺放各組件
# min_label.pack()
# sec_label.pack()
# min_entry.pack()
# sec_entry.pack()
# start_button.pack(side=tk.LEFT)
# cancel_button.pack(side=tk.RIGHT)

# loop
window.mainloop()
