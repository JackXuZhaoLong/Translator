from tkinter import *
from tkinter import  messagebox
import requests
def translation():
    content = entry.get()
    content = content.strip()
    if content == "":
        messagebox.showwarning('提示', message='请输入要翻译的内容')
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        res = requests.post(url,data=data)
        result = res.json()
        trans = result['translateResult'][0][0]['tgt']
        resu.set(trans)



window = Tk()
window.geometry('372x100+914+438')
window.title('中英互译')

label = Label(window, text = '输入要翻译的文字:', font =('微软雅黑',12))
label.grid()
entry = Entry(window, font =('微软雅黑',15))
entry.grid(row = 0, column = 1)
label1 = Label(window, text = '输入要翻译的文字:', font =('微软雅黑',12))
label1.grid(row = 1,column = 0)
resu = StringVar()
entry1 = Entry(window, font =('微软雅黑',15), textvariable=resu)
entry1.grid(row = 1, column = 1)

button = Button(window, text = '翻译', width = 10, command = translation)
button.grid(row = 2, column = 0, sticky = W)
button1 = Button(window, text = '退出', width = 10, command = window.quit)
#sticky 对齐方式
button1.grid(row = 2, column = 1, sticky = E)



window.mainloop()