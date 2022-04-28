#!Python3

#import module

from random import randint
from time import sleep
import tkinter as tk
from tkinter import ttk, messagebox as msg
import threading

#data base

fivestarxd=[]
fivestar=[]
fourstarxd=[]
fourstar=[]
threestar=['弹弓','神射手之誓','鸦羽弓','翡玉法球','讨龙英杰谭','魔导绪论',
         '黑缨枪','以理服人','沐浴龙血的剑','铁影阔剑','飞天御剑',
         '黎明神剑','冷刃']

def cratekachi(xiandingwuxing,sixing):
    global fivestarxd,fivestar,fourstarxd,fourstar,nr,nrs,ckdata,wx_texts,sx_texts,wxt,sxt
    fivestarxd=xiandingwuxing
    fivestar=fivestarxd*5+['莫娜','迪卢克','七七','刻晴','琴']
    fourstarxd=sixing
    fourstar=fourstarxd*9+['迪奥娜','云堇','重云','凝光','行秋','罗莎莉亚',
                        '安柏','凯亚','丽莎','五郎','早柚','烟绯',
                        '托马','砂糖','诺艾尔','菲谢尔','北斗',
                        '香菱','雷泽','芭芭拉','弓藏','祭礼弓','绝弦',
                        '西风猎弓','昭心','祭礼残章','流浪乐章',
                        '西风秘典','西风长枪','匣里灭辰','雨裁',
                        '祭礼大剑','钟剑','西风大剑','匣里龙吟',
                        '祭礼剑','笛剑','西风剑','班尼特','辛焱','九条裟罗']
    nr=[]
    nrs=[]
    ckdata=[0,0,0,0]
    wx_texts=[]
    sx_texts=[]
    wxt=''
    sxt=''
    wx_text.set('')
    sx_text.set('')
    qy.update()
    if len(xiandingwuxing)==1:
        muqiankachi.set('目前卡池:'+xiandingwuxing[0])
    else:
        muqiankachi.set('目前卡池:常驻池') 
        fourstarxd=['迪奥娜','云堇','重云','凝光','行秋','罗莎莉亚',
                        '安柏','凯亚','丽莎','五郎','早柚','烟绯',
                        '托马','砂糖','诺艾尔','菲谢尔','北斗',
                        '香菱','雷泽','芭芭拉','弓藏','祭礼弓','绝弦',
                        '西风猎弓','昭心','祭礼残章','流浪乐章',
                        '西风秘典','西风长枪','匣里灭辰','雨裁',
                        '祭礼大剑','钟剑','西风大剑','匣里龙吟',
                        '祭礼剑','笛剑','西风剑','班尼特','辛焱','九条裟罗']
        fourstar=fourstarxd

kachis={'雷电将军':['班尼特','辛焱','九条裟罗'],'珊瑚宫心海':['班尼特','辛焱','九条裟罗'],'申鹤':['云堇','重云','凝光'],
        '温迪':['云堇','香菱','砂糖'],'神里绫人':['云堇','香菱','砂糖'],'神里绫华':['早柚','雷泽','罗莎莉亚'],
        '魈':['辛焱','北斗','迪奥娜'],'枫原万叶':['班尼特','雷泽','罗莎莉亚'],'钟离':['烟绯','北斗','行秋'],
        '甘雨':['烟绯','北斗','行秋'],'宵宫':['辛焱','迪奥娜','早柚'],'可莉':['香菱','行秋','诺艾尔'],
        '阿贝多':['砂糖','菲谢尔','班尼特'],'达达利亚':['凝光','北斗','迪奥娜'],'优菈':['辛焱','行秋','北斗'],
        '荒泷一斗':['芭芭拉','五郎','香菱'],'八重神子':['迪奥娜','托马','菲谢尔'],'常驻池':['莫娜','迪卢克','七七','刻晴','琴'],
        '胡桃':['迪奥娜','托马','早柚']}

nr=[]
nrs=[]
ckdata=[0,0,0,0]

wx_texts=[]
sx_texts=[]
wxt=''
sxt=''

#def function

def ck(cishu,ckdata):
    neirong=[]
    for i in range(cishu):
        a=0
        c=randint(1,1000)

        if ckdata[0]==179:
            neirong.append(fivestarxd[randint(0,len(fivestarxd)-1)])
            ckdata[0]=0;ckdata[1]=0;ckdata[2]=0;ckdata[3]=0
            continue

        if ckdata[1]==89:
            neirong.append(fivestar[randint(0,len(fivestar)-1)])
            if neirong[-1] in fivestarxd:
                ckdata[0]=0;ckdata[1]=0;ckdata[2]=0;ckdata[3]=0
                continue
            else:
                ckdata[1]=0;ckdata[2]=0;ckdata[3]=0;ckdata[0]+=1
                continue

        if ckdata[2]==19:
            neirong.append(fourstarxd[0])
            ckdata[2]=0;ckdata[3]=0;ckdata[0]+=1;ckdata[1]+=1
            continue

        if ckdata[3]==9:
            neirong.append(fourstar[randint(0,len(fourstar)-1)])
            if neirong[-1] in fourstarxd:
                ckdata[2]=0;ckdata[3]=0;ckdata[0]+=1;ckdata[1]+=1
                continue
            else:
                ckdata[3]=0;ckdata[0]+=1;ckdata[1]+=1;ckdata[2]+=1
                continue

        for a in range(1,7):
            if c==a:
                if ckdata[0]>=89:
                    neirong.append(fivestarxd[randint(0,len(fivestarxd)-1)])
                    ckdata[0]=0;ckdata[1]=0;ckdata[2]=0;ckdata[3]=0
                    continue
                else:
                    neirong.append(fivestar[randint(0,len(fivestar)-1)])
                    if neirong[-1] in fivestarxd:
                        ckdata[0]=0;ckdata[1]=0;ckdata[2]=0;ckdata[3]=0
                        continue
                    else:
                        ckdata[1]=0;ckdata[2]=0;ckdata[3]=0;ckdata[0]+=1
                        continue

        for a in range(7,58):
            if c==a:
                neirong.append(fourstar[randint(0,len(fourstar)-1)])
                if neirong[-1] in fourstarxd:
                    ckdata[2]=0;ckdata[3]=0;ckdata[0]+=1;ckdata[1]+=1
                    continue
                else:
                    ckdata[3]=0;ckdata[0]+=1;ckdata[1]+=1;ckdata[2]+=1
                    continue

        for a in range(58,1001):
            if c==a:
                neirong.append(threestar[randint(0,len(threestar)-1)])
                ckdata[0]+=1;ckdata[1]+=1;ckdata[2]+=1;ckdata[3]+=1
                continue
    return neirong,ckdata

def dc():
    global nr,nrs,ckdata,q1,q2,wx_texts,sx_texts,wst,xst
    ow=''
    nrs,ckdata=ck(1,ckdata)
    for i in nrs:
        ow=ow+'    ['+i+']'+'\n'
    msg.showinfo('单抽','获得:\n'+ ow)
    nr.append(nrs)
    for i in nrs:
        if i in fivestar:
            wxt=''
            wx_texts.append('['+i+'] ')
            for l in range(len(wx_texts)):
                if (l+1)%6==0:
                    wxt+=wx_texts[l]
                    wxt+='\n'
                else:
                    wxt+=wx_texts[l]
            wx_text.set(wxt)
        if i in fourstar:
            sxt=''
            sx_texts.append('['+i+'] ')
            for l in range(len(sx_texts)):
                if (l+1)%6==0:
                    sxt+=sx_texts[l]
                    sxt+='\n'
                else:
                    sxt+=sx_texts[l]
            sx_text.set(sxt)

    mas=tk.Label(qy, text=f'已{ckdata[1]}抽未出金.')
    mas.grid(row=2, column=0, columnspan=2, padx=40,pady=8)
    qy.update()

def sl():
    global nr,nrs,ckdata,q1,q2,wx_texts,sx_texts,wxt,sxt
    ow=''
    nrs,ckdata=ck(10,ckdata)
    for i in nrs:
        ow=ow+'['+i+']'+'\n'
    msg.showinfo('十连','获得:\n'+ ow)
    nr.append(nrs)
    for i in nrs:
        if i in fivestar:
            wxt=''
            wx_texts.append('['+i+'] ')
            for l in range(len(wx_texts)):
                if (l+1)%6==0:
                    wxt+=wx_texts[l]
                    wxt+='\n'
                else:
                    wxt+=wx_texts[l]
            wx_text.set(wxt)
        if i in fourstar:
            sxt=''
            sx_texts.append('['+i+'] ')
            for l in range(len(sx_texts)):
                if (l+1)%6==0:
                    sxt+=sx_texts[l]
                    sxt+='\n'
                else:
                    sxt+=sx_texts[l]
            sx_text.set(sxt)
    mas=tk.Label(qy, text=f'已{ckdata[1]}抽未出金.')
    mas.grid(row=2, column=0, columnspan=2, padx=40,pady=8)
    qy.update()

def savedat():
    if nr==[]:
        msg.showerror('错误','保存数据前请先进行抽卡！')
        return
    with open('.\\dat.txt','a') as dat:
        dat.write('\n')
        for i in range(len(nr)):
            dat.write(str(i+1) + '. ')
            for m in range(len(nr[i])):
                if m == len(nr[i])-1:
                    dat.write('['+nr[i][m]+'] ')
                    continue
                dat.write('['+nr[i][m]+'] , ')
            dat.write('\n\n')
        dat.write('\n\n')

def ccc():
    global qy
    while True:
        try:
            w1 = tk.Label(qy, text='©  SMB-STUDIO')
            w1.grid(row=7, column=0, columnspan=2, pady=8)
            qy.update()
            sleep(2)
            w1 = tk.Label(qy, text='未经允许,禁止转载')
            w1.grid(row=7, column=0, columnspan=2, pady=8)
            qy.update()
            sleep(2)
        except:
            break
def guanyu():
    msg.showinfo('关于','原神抽卡模拟器v2.1\n本程序由SMB-STUDIO制作，仅作测试之用。\n作者QQ：3396645909 GiHub：myphone12 \n喜欢的话记得点个Star哟！')

def upgrade():
    msg.showinfo('提示','该功能暂未开发！')
def choicekachi(juese):
    if juese!='常驻池':
        cratekachi([juese],kachis[juese])
        return
    else:
        cratekachi(kachis[juese],kachis[juese])
        return

#main program

#old

'''
print('---原神抽卡模拟器v2.1---')
while True:
    print('祈愿一次[1] 祈愿十次[2]')
    print('        退出[3]')
    try:
        a=int(input(':'))
    except:
        print('无法识别的序号.')
        break
    if a==1:
        nrs,ckdata=ck(1,ckdata)
        nr.append(nrs)
        print('获得:')
        for i in range(len(nrs)):
            print(f'[{nrs[i]}]')
        print(f'已{ckdata[1]}抽未出金.')
        nrs=[]
    elif a==2:
        nrs,ckdata=ck(10,ckdata)
        nr.append(nrs)
        print('获得:')
        for i in range(len(nrs)):
            print(f'[{nrs[i]}]')
        print(f'已{ckdata[1]}抽未出金.')
        nrs=[]
    elif a==3:
        print('正在退出....')
        break
    else:
        print('无法识别的序号.')
        break
'''

#new

qy=tk.Tk()
qy.title('原神抽卡模拟器v2.1')
qy.resizable(0, 0)

p1=tk.Label(qy, text='五星:', anchor='n', font=("Microsoft Yahei UI", 9))
p1.grid(row=0, column=0, padx=5,pady=8)
wx_text=tk.StringVar()
q1=tk.Label(qy, textvariable=wx_text, anchor='n', font=("Microsoft Yahei UI", 9),fg='orange')
q1.grid(row=0, column=1, padx=0, pady=8)
p2=tk.Label(qy, text='四星:', anchor='n', font=("Microsoft Yahei UI", 9))
p2.grid(row=1, column=0, padx=5,pady=8)
sx_text=tk.StringVar()
q2=tk.Label(qy, textvariable=sx_text, anchor='n', font=("Microsoft Yahei UI", 9),fg='purple')
q2.grid(row=1, column=1, padx=0, pady=8)

muqiankachi=tk.StringVar()
kac=tk.Label(qy, textvariable=muqiankachi)
kac.grid(row=3, column=0, columnspan=2, padx=40,pady=8)

b1=ttk.Button(qy, text='单抽', width=40, command=dc)
b1.grid(row=4, pady=10, column=0, columnspan=2, padx=6)
b2=ttk.Button(qy, text='十连', width=40, command=sl)
b2.grid(row=5, pady=10, column=0, columnspan=2, padx=6)
b3=ttk.Button(qy, text='保存数据', width=40, command=savedat)
b3.grid(row=6, pady=10, column=0, columnspan=2, padx=6)

xxx=threading.Thread(target=ccc)
xxx.start()

menubar = tk.Menu(qy)
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="雷电将军", command=lambda:choicekachi('雷电将军'))
filemenu.add_command(label="神里绫华", command=lambda:choicekachi('神里绫华'))
filemenu.add_command(label="珊瑚宫心海", command=lambda:choicekachi('珊瑚宫心海'))
filemenu.add_command(label="达达利亚", command=lambda:choicekachi('达达利亚'))
filemenu.add_command(label="胡桃", command=lambda:choicekachi('胡桃'))
filemenu.add_command(label="温迪", command=lambda:choicekachi('温迪'))
filemenu.add_command(label="神里绫人", command=lambda:choicekachi('神里绫人'))
filemenu.add_command(label="宵宫", command=lambda:choicekachi('宵宫'))
filemenu.add_command(label="枫原万叶", command=lambda:choicekachi('枫原万叶'))
filemenu.add_command(label="钟离", command=lambda:choicekachi('钟离'))
filemenu.add_command(label="优菈", command=lambda:choicekachi('优菈'))
filemenu.add_command(label="可莉", command=lambda:choicekachi('可莉'))
filemenu.add_command(label="阿贝多", command=lambda:choicekachi('阿贝多'))
filemenu.add_command(label="荒泷一斗", command=lambda:choicekachi('荒泷一斗'))
filemenu.add_command(label="魈", command=lambda:choicekachi('魈'))
filemenu.add_command(label="甘雨", command=lambda:choicekachi('甘雨'))
filemenu.add_command(label="申鹤", command=lambda:choicekachi('申鹤'))
filemenu.add_command(label="八重神子", command=lambda:choicekachi('八重神子'))
filemenu.add_separator()
filemenu.add_command(label="常驻池", command=lambda:choicekachi('常驻池'))
menubar.add_cascade(label="卡池切换",menu=filemenu)

menubar.add_command(label="更新数据", command=upgrade)

menubar.add_command(label="关于", command=guanyu)

qy.config(menu=menubar)

cratekachi(['雷电将军'],kachis['雷电将军'])
qy.mainloop()
