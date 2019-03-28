from tkinter import *

window = Tk()
window.title('by whx')
window.geometry('288x495')
window.resizable(0,0)

result=StringVar()
result1=StringVar()   # 两个显示面板 分别显示过程和结果
isdeng=StringVar()
isdeng.set('0')
result.set('')
result1.set('0')
l2=Label(window,textvariable=result,bg='#FFFFE0',anchor='se',font=('宋体',15))
l2.place(width=290,height=35)
l=Label(window,textvariable=result1,bg='#FFFFE0',anchor='se',font=('宋体',15))
l.place(y=35,width=290,height=35)

isdian = False   #添加一个判断是否按下运算符号的标志,假设默认没有按下按钮

def hit_me(num):   #设置一个数字函数 判断是否按下数字 并获取数字将数字写在显示版

    global isdian     #全局化isdian和按钮状态
    if num=='.':
        if isdian == False:
            oldnum=result.get()
            oldnum+=num
            result.set(oldnum)
            isdian = True
        else:
            pass
    elif num == '+' and isdeng.get() != '0' or num == '-' and isdeng.get() != '0' or \
            num == '*'and isdeng.get() != '0' or num == '/' and isdeng.get() != '0' or \
             num == '/' and isdeng.get() != '0' or num == '**' and isdeng.get() != '0':
        oldnum = isdeng.get()
        oldnum += num
        result.set(oldnum)
        isdeng.set('0')
    elif result.get()=='0' and num!= '.':
        oldnum=num
        result.set(oldnum)
    elif  num == '+' and isdeng.get() == '0' or num == '-' and isdeng.get() == '0' or \
           num == '*' and isdeng.get() == '0' or num == '/' and isdeng.get() == '0' or \
            num == '/' and isdeng.get() == '0' or num == '**' and isdeng.get() == '0':
        oldnum=result.get()
        temp = len(oldnum)
        temp1 = oldnum[temp-1]
        temp2 = oldnum[temp - 2]
        if temp1 == '+' and temp2 != '*' or temp1 == '-' and temp2 != '*' or \
                temp1 == '*' and temp2 != '*'or temp1 == '/' and temp2 != '*':
            result.set(result.get()[:-1])
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
        elif  temp1 == '*' and temp2 == '*':
            result.set(result.get()[:-1])
            result.set(result.get()[:-1])
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
        else:
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
    else:
        if num == '+' or num == '-' or num == '*' or num == '/':
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
            isdeng.set('0')
            isdian = False
        else:
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
            isdeng.set('0')



def hit_count():     #错误处理
    global isdian
    try:
        outcome=eval(result.get())
        result1.set(round(outcome,10))
        isdeng.set(outcome)
        result.set('')
        isdian = False
    except SyntaxError :
        result.set('')
        result1.set('INPUT ERROR')
    except ZeroDivisionError :
        result.set('')
        result1.set('VALUE ERROR')
    else:
        pass



def hit_back():   #删除处理
    if len(result.get()) > 0:
        if len(result.get()) == 1:
            result.set('0')
        else:
            result.set(result.get()[:-1])
    else:
        return result.get()


def hit_AC():    #清空处理
    global isdian
    result.set('')
    result1.set('0')
    isdian = False


#按钮添加

bpow = Button(window,text='^',bd = 0.5,bg="#d9f9f4",command=lambda :hit_me('**'))
bpow.place(y=70,x=0,height=71.6,width=72)
bleft = Button(window,text='(',bd = 0.5,bg="#d9f9f4",command=lambda :hit_me('('))
bleft.place(y=70,x=72,height=71.6,width=72)
bright = Button(window,text=')',bd = 0.5,bg="#d9f9f4",command=lambda :hit_me(')'))
bright.place(y=70,x=144,height=71.6,width=72)
bac = Button(window,text='AC',bd = 0.5,bg="#d9f9f4",command=lambda :hit_AC())
bac.place(y=70,x=216,height=71.6,width=72)

bback = Button(window,text='delete',bg="#d9f9f4",bd = 0.5,command=lambda :hit_back())
bback.place(y=142,x=0,height=71.6,width=72)
bdivision = Button(window,text='/',bg="#d9f9f4",bd = 0.5,command=lambda :hit_me('/'))
bdivision.place(y=142,x=72,height=71.6,width=72)
bmultiply = Button(window,text='*',bg="#d9f9f4",bd = 0.5,command=lambda :hit_me('*'))
bmultiply.place(y=142,x=144,height=71.6,width=72)
bmin = Button(window,text='-',bg="#d9f9f4",bd = 0.5,command=lambda :hit_me('-'))
bmin.place(y=142,x=216,height=71.6,width=72)

b7 = Button(window,text='7',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('7'))
b7.place(y=214,x=0,height=71.6,width=72)
b8 = Button(window,text='8',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('8'))
b8.place(y=214,x=72,height=71.6,width=72)
b9 = Button(window,text='9',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('9'))
b9.place(y=214,x=144,height=71.6,width=72)


b4 = Button(window,text='4',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('4'))
b4.place(y=286,x=0,height=71.6,width=72)
b5 = Button(window,text='5',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('5'))
b5.place(y=286,x=72,height=71.6,width=72)
b6 = Button(window,text='6',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('6'))
b6.place(y=286,x=144,height=71.6,width=72)
bplus = Button(window,text='+',bd = 0.5,bg="#d9f9f4",command=lambda :hit_me('+'))
bplus.place(y=214,x=216,height=143.2,width=72)

b1 = Button(window,text='1',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('1'))
b1.place(y=358,x=0,height=71.6,width=72)
b2 = Button(window,text='2',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('2'))
b2.place(y=358,x=72,height=71.6,width=72)
b3 = Button(window,text='3',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('3'))
b3.place(y=358,x=144,height=71.6,width=72)
bdeng = Button(window,text='=',bd = 0.5,bg="#d9f9f4",command=lambda :hit_count())
bdeng.place(y=358,x=216,height=143.2,width=72)

b0 = Button(window,text='0',bd = 0.5,bg="#aeccc6",command=lambda :hit_me('0'))
b0.place(y=430,x=0,height=71.6,width=144)
bb = Button(window,text='.',bd = 0.5,bg="#d9f9f4",command=lambda :hit_me('.'))
bb.place(y=430,x=144,height=71.6,width=72)


window.mainloop()###事件循环