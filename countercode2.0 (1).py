from tkinter import *

window = Tk()
window.title('by whx')
window.geometry('290x500')
window.resizable(0,0)

result=StringVar()
result1=StringVar()
result.set('')
result1.set('0')
l2=Label(window,textvariable=result,bg='#FFFFE0',anchor='se',font=('宋体',15))
l2.place(width=290,height=35)
l=Label(window,textvariable=result1,bg='#FFFFE0',anchor='se',font=('宋体',15))
l.place(y=35,width=290,height=35)

isdian = False

def hit_me(num):

    global isdian
    if num=='.':
        if isdian == False:
            oldnum=result.get()
            oldnum+=num
            result.set(oldnum)
            isdian = True
        else:
            pass
    elif result.get()=='0' and num!= '.':
        oldnum=num
        result.set(oldnum)
    else:
        if num == '+' or num == '-' or num == '*' or num == '/':
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)
            isdian = False
        else:
            oldnum = result.get()
            oldnum += num
            result.set(oldnum)



def hit_count():
    global isdian
    try:
        outcome=eval(result.get())
        result1.set(outcome)
        result.set('')
        isdian = False
    except SyntaxError :
        result.set('')
        result1.set('傻逼别乱来')
    except ZeroDivisionError :
        result.set('')
        result1.set('FBI WARNING')
    else:
        pass



def hit_back():
    if len(result.get()) > 0:
        if len(result.get()) == 1:
            result.set('0')
        else:
            result.set(result.get()[:-1])
    else:
        return result.get()


def hit_AC():
    global isdian
    result.set('')
    result1.set('0')
    isdian = False



bback = Button(window,text='delete',command=lambda :hit_back())
bback.place(y=150,x=10,height=60,width=60)
bdivision = Button(window,text='/',command=lambda :hit_me('/'))
bdivision.place(y=150,x=80,height=60,width=60)
bmultiply = Button(window,text='*',command=lambda :hit_me('*'))
bmultiply.place(y=150,x=150,height=60,width=60)
bmin = Button(window,text='-',command=lambda :hit_me('-'))
bmin.place(y=150,x=220,height=60,width=60)

bpow = Button(window,text='^',command=lambda :hit_me('**'))
bpow.place(y=80,x=10,height=60,width=60)
bleft = Button(window,text='(',command=lambda :hit_me('('))
bleft.place(y=80,x=80,height=60,width=60)
bright = Button(window,text=')',command=lambda :hit_me(')'))
bright.place(y=80,x=150,height=60,width=60)
bac = Button(window,text='AC',command=lambda :hit_AC())
bac.place(y=80,x=220,height=60,width=60)

b7 = Button(window,text='7',command=lambda :hit_me('7'))
b7.place(y=220,x=10,height=60,width=60)
b8 = Button(window,text='8',command=lambda :hit_me('8'))
b8.place(y=220,x=80,height=60,width=60)
b9 = Button(window,text='9',command=lambda :hit_me('9'))
b9.place(y=220,x=150,height=60,width=60)


b4 = Button(window,text='4',command=lambda :hit_me('4'))
b4.place(y=290,x=10,height=60,width=60)
b5 = Button(window,text='5',command=lambda :hit_me('5'))
b5.place(y=290,x=80,height=60,width=60)
b6 = Button(window,text='6',command=lambda :hit_me('6'))
b6.place(y=290,x=150,height=60,width=60)
bplus = Button(window,text='+',command=lambda :hit_me('+'))
bplus.place(y=220,x=220,height=130,width=60)

b1 = Button(window,text='1',command=lambda :hit_me('1'))
b1.place(y=360,x=10,height=60,width=60)
b2 = Button(window,text='2',command=lambda :hit_me('2'))
b2.place(y=360,x=80,height=60,width=60)
b3 = Button(window,text='3',command=lambda :hit_me('3'))
b3.place(y=360,x=150,height=60,width=60)
bdeng = Button(window,text='=',command=lambda :hit_count())
bdeng.place(y=360,x=220,height=130,width=60)

b0 = Button(window,text='0',command=lambda :hit_me('0'))
b0.place(y=430,x=10,height=60,width=130)
bb = Button(window,text='.',command=lambda :hit_me('.'))
bb.place(y=430,x=150,height=60,width=60)


window.mainloop()