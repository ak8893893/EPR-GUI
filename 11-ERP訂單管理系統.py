"""
標題 : ERP 訂單管理系統 var 0.4
作者 : 賴韋銘 AK
時間 : 2022/4/10
備註 : 新增刪除鍵與圖表功能
"""

"""
ERP訂單管理系統
畫面
1. 4個 label 訂單編號  商品名稱 金額 備註
2. 2個 label Enter 商品名稱 金額
3. 1個 spinBox 訂單編號
4. 1個 ScrolledText 備註
5. 改為訂單狀況 (未處理，已寄出，已收到，結案) 可以用 GUI-LABELFRAME-RAIDO 來做
6. 1個 Tree 列表  ( 訂單編號, 商品名稱, 金額, 備註,訂單狀況 )  
7. 1個按鈕 "Save" (列印內容)
8. toolbar,(可以畫面就好了、離開那個可以出去)
9. menu 下拉式選單(畫面就好了)
10.一個 toobar 圖片放上去 待之後開發
11.刪除資料的按鈕
"""
# 匯入資料庫
import tkinter as tk                                                       # tkinter 函式庫，用來做GUI視窗
from PIL import Image,ImageTk                                              # PIL函式庫，用來導入圖片放到GUI中
from tkinter import ttk                                                    # tkinter 中的 ttk 函式庫,用來做各種功能的GUI
from tkinter.scrolledtext import ScrolledText                              # 用來做多行輸入框的
import matplotlib.pyplot as plt                                            # 繪製圖表的函式庫


# 0. 建立視窗物件
win = tk.Tk()                                                              # 建立主式窗物件
win.title(" ERP 訂單管理系統, copyright 賴韋銘 AK")                                              # 主式窗顯示名稱
win.resizable(0,0)                                                         # 視窗可否調整大小
win.minsize(1250,600)                                                      # 視窗最小尺寸

# 10. 一個假的 toolbar 圖片放上去 待之後開發
fakeToolBar = Image.open("fake-tool-bar.png")                              # 開啟工具列的圖片檔
fakeToolBar = fakeToolBar.resize((1250,55),Image.ANTIALIAS)                # 重新調整圖片尺寸
fakeToolBar = ImageTk.PhotoImage(fakeToolBar)                              # 把這個圖片放到GUI物件中準備使用
labelfakeToolBar = tk.Label(win,image=fakeToolBar)                         # 將 productImg 放入 win 這個視窗中
labelfakeToolBar.place(x=0,y=0)                                            # 將此圖片物件放置到這個位置

# 1.建立四個標籤 訂單編號  商品名稱 金額 備註
labelBookNum = tk.Label(win,text="訂單編號",font=("標楷體",20))              # 訂單編號文字標籤
labelBookNum.place(x=10,y=70)                                             # 訂單編號文字標籤放置位置
labelMerchandiseName = tk.Label(win,text="商品名稱",font=("標楷體",20))      # 商品名稱文字標籤
labelMerchandiseName.place(x=10,y=120)                                    # 商品名稱文字標籤放置位置
labelPrice = tk.Label(win,text="  金額",font=("標楷體",20))                 # 金額文字標籤
labelPrice.place(x=10,y=170)                                              # 金額文字標籤放置位置
labelNote = tk.Label(win,text="  備註",font=("標楷體",20))                 # 備註文字標籤
labelNote.place(x=10,y=220)                                               # 備註文字標籤放置位置
labelWay = tk.Label(win,text="運送方式",font=("標楷體",20))                # 運送方式文字標籤
labelWay.place(x=500,y=70)                                               # 運送方式文字標籤放置位置

# 2.建立兩個 label Enter 商品名稱 金額
entryTextName = tk.StringVar()                                                  # 建立名字輸入框的內容變數
entryMerchandiseName=tk.Entry(win,font=("標楷體",20),textvariable=entryTextName)  # 新增名字輸入框 Entry
entryMerchandiseName.place(x=140,y=120)                                         # 放置名字輸入框到主視窗
entryTextPrice = tk.Variable()                                                  # 建立價格輸入框的內容變數
entryPrice=tk.Entry(win,font=("標楷體",20),textvariable=entryTextPrice)          # 新增價格輸入框 Entry
entryPrice.place(x=140,y=170)                                                   # 加入價格輸入框到主視窗

# 3. 1個 spinBox 訂單編號
def value_changed():                                                      # 定義 Spinbox 數字調整 時的功能
    print(book_value.get())                                               # 印出現在的數字
book_value = tk.StringVar(value=0)                                        # 建立訂單編號的變數
spin_box = ttk.Spinbox(                                                  # 訂單編號 spinbox 的數字範圍和變數和更改時會執行的動作
    win,
    from_=0,
    to=9999999999,
    textvariable=book_value,
    command=value_changed,font=("標楷體",20))
spin_box.place(x=140,y=70)                                                # 訂單編號 spinbox的放置位置

# 4. 1個 ScrolledText 備註
# separator = ttk.Separator(win, orient='horizontal')                       # 建立一個分割線
# separator.pack(fill='x')                                                  # 分割線放置位置
st = ScrolledText(win, width=50,  height=2,font=("標楷體",20))             # 建立一個 備註 多行輸入格 scrolledtext
st.place(x=140,y=220)                                                     # 備註 多行輸入格放置在這個位置

# 5. 右邊改為訂單狀況 (未處理，已寄出，已收到，結案) 可以用 GUI-LABELFRAME-RAIDO 來做
lf1 = ttk.LabelFrame(win, text='訂單狀況')                                  # 建立一個 訂單狀況 label frame 物件
lf1.place(x=865,y=130)                                                    # 訂單狀況 label frame 物件放置位置
# 訂單狀況 label frame 物件 內放入 多選一的元件 Radiobutton
radioValue = tk.StringVar()                                               # 多選一的元件 Radiobutton 的變數
radioValue.set('未處理')                                                   # 初始值設定
rdioOne = tk.Radiobutton(lf1, text='未處理',variable=radioValue, value='未處理',font=("標楷體",16))   # 未處理 radio按鈕的建立 注意： 要建立於 lf1 表格中
rdioTwo = tk.Radiobutton(lf1, text='已寄出',variable=radioValue, value='已寄出',font=("標楷體",16))   # 已寄出 radio按鈕的建立 注意： 要建立於 lf1 表格中
rdioThree = tk.Radiobutton(lf1, text='已收到',variable=radioValue, value='已收到',font=("標楷體",16)) # 已收到 radio按鈕的建立 注意： 要建立於 lf1 表格中
rdioFour = tk.Radiobutton(lf1, text='結案  ',variable=radioValue, value='結案  ',font=("標楷體",16)) # 結案 radio按鈕的建立 注意： 要建立於 lf1 表格中
rdioOne.pack()                                                                                     # 未處理 radio按鈕的位置
rdioTwo.pack()                                                                                     # 已寄出 radio按鈕的位置
rdioThree.pack()                                                                                   # 已收到 radio按鈕的位置
rdioFour.pack()                                                                                    # 結案   radio按鈕的位置

# 9. menu 下拉式選單(畫面就好了)
def on_field_change(index, value, op):                                                             # 定義 運送方式 下拉式選單選取時的功能
    print("combobox updated to ", comboboxValue1.get())                                            # 印出 運送方式 下拉式選單目前的值
comboboxValue1 = tk.StringVar()                                                                    # 建立 運送方式 下拉式選單的變數
comboboxValue1.trace('w',on_field_change)                                                          # 注意：當資料不同時，就會呼叫 on_field_change
wayChoosen = ttk.Combobox(win, width=27, textvariable=comboboxValue1,font=("標楷體",20))            # 建立 運送方式 下拉式選單的物件於主式窗
wayChoosen['values'] = ('空運',                                                                    # Adding combobox drop down list
                          '海運',
                          '陸運',
                          '宅配',
                          '超商店到店')
wayChoosen.place(x=630,y=70)                                                                      # 運送方式 下拉式選單的放置位置

# 6. 1個 Tree 列表  ( 訂單編號, 商品名稱, 金額, 備註,訂單狀況 )  110-GUI-tree-表格-列表.py
columns = ('labelBookNum', 'labelMerchandiseName','labelPrice','labelNote',"labelWay",'process')  # define columns 定義欄位名稱
tree = ttk.Treeview(win, columns=columns, show='headings',height=13)                              # 建立 Tree 列表的物件於主視窗
tree.place(x=30,y=300)                                                                            # Tree 列表的放置位置
tree.heading('labelBookNum', text='訂單編號')                                                      # define headings 定義每個欄位的名稱
tree.heading('labelMerchandiseName', text='商品名稱')                                              # define headings 定義每個欄位的名稱
tree.heading('labelPrice', text='金額')                                                           # define headings 定義每個欄位的名稱
tree.heading('labelNote', text='備註')                                                            # define headings 定義每個欄位的名稱
tree.heading('labelWay', text='運送方式')                                                          # define headings 定義每個欄位的名稱
tree.heading('process', text='處理狀況')                                                           # define headings 定義每個欄位的名稱
contacts = [('11214 ', '玻璃杯',180,'小心輕放','海運','未處理'),                                     # 放一些初始就在資料庫的資料
            ('9527', '石頭',25,'正常搬運','陸運','結案  ')]
# add data to the treeview
for contact in contacts:                                                                        # 把初始資料庫的物件一一放入 tree 表格中
    tree.insert('', tk.END, values=contact)

def item_selected(event):                                                                        # 把選到的物件放入 LIST record 中
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)
    # 2-4. 把 tree 列表中的資料放到輸入框內

        book_value.set(record[0])             # 訂單編號放入
        entryTextName.set(record[1])          # 訂單名稱放入
        entryTextPrice.set(record[2])         # 訂單金額放入
        st.delete("1.0",tk.END)               # 訂單備註清除
        st.insert(tk.INSERT,record[3])        # 訂單備註放入
        comboboxValue1.set(record[4])         # 訂單運送方式放入
        radioValue.set(record[5])             # 訂單狀況呈現

tree.bind('<<TreeviewSelect>>', item_selected)                     # 連結到所選物件

# 8. toolbar 離開按鈕
exitImg = Image.open("exit.jpg")                                   # 讀取 exit 照片檔
exitImg = exitImg.resize((55,55),Image.ANTIALIAS)                  # 重塑照片大小
exitImg = ImageTk.PhotoImage(exitImg)                              # 把圖片放入物件中
def exitFun():                                                     # 定義離開按鈕的功能
    exit()                                                         # 執行離開
exitBtn = tk.Button(win,image=exitImg,command=exitFun)             # 建立離開按鈕物件
exitBtn.place(x=10,y=2)                                            # 離開按鈕的放置位置

# 7. 1個按鈕 "Save" (添加此筆訂單)
def addBook():                                                         # 存檔按鈕的功能
    Note_content = st.get('1.0', 'end')                                # 備註欄內的所有資料
    print(Note_content)
    print(book_value.get())
    print(entryMerchandiseName.get())
    print(entryPrice.get())
    print(Note_content)
    print(radioValue.get())
    print(contacts)
    print(comboboxValue1.get())
    readyToInput = [(book_value.get(),entryMerchandiseName.get(),entryPrice.get(),Note_content,comboboxValue1.get(),radioValue.get())] # 把準備要放入的資料全部讀取起來
    dataBase = contacts.extend(readyToInput)                        # 放入所有要加入的資料到資料庫中
    print(dataBase)                                                 # 印出所有資料庫中的資料
    for contact in readyToInput:                                    # 把要放入的資料放在 Tree 列表 中
        tree.insert('', tk.END, values=contact)
buttonInput = tk.Button(win, text="添加此筆訂單",command=addBook,font=("標楷體",20)) # 建立 添加此筆資料的按鈕
buttonInput.place(x=1000,y=170)                                      # 放置 添加此筆資料的按鈕到這位置

# 11.刪除資料的按鈕
def deleteFun():                                                        # 定義刪除所選資料的功能
    if len(tree.selection())>0:
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
    else:
        tkMessageBox.showerror("操作錯誤", "請先選取要刪除的資料")  # 錯誤視窗
buttonDelete = tk.Button(win, text="刪除此筆訂單",command=deleteFun,font=("標楷體",20))  # 建立 刪除按鈕
buttonDelete.place(x=1000,y=220)                                         # 放置刪除按鈕到此位置

# 13. 做加上繪製圖表的按鈕 繪製出商品金額的圖表
drawChartImg = Image.open("draw-chart.png")                            # 開啟繪製圖片的 icon 圖片檔
drawChartImg = drawChartImg.resize((55,55),Image.ANTIALIAS)            # 重塑圖片大小
drawChartImg = ImageTk.PhotoImage(drawChartImg)                        # 將圖片放入物件中準備使用
def chartFun():                                                        # 定義繪圖功能
    print("draw a chart")
    x = [1, 2, 3, 4]                                                   # x 軸的資料
    y = [1, 2, 3, 4]                                                   # y 軸的資料
    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)           # bar 中放入的資料 和呈現方式
    plt.show()                                                         # 展現圖表
drawChartBtn = tk.Button(win,image=drawChartImg,command=chartFun)      # 建立繪製圖表的按鈕在主視窗上
drawChartBtn.place(x=115,y=1)                                          # 放置繪製圖表的按鈕在這個位置

# 12. 加上 ttk 的主題 Create an instance of Style widget
style = ttk.Style()                                                    # 建立 主題 物件
style.theme_use('clam')                                                # 主題使用 clam 主題

# 程式主循環
win.mainloop()












