from tkinter import *
from scroll1 import *
from pyglet import *
from screeninfo import get_monitors
from datetime import datetime
import speech_recognition as sr
import platform
import pyttsx3
from os import system
m=get_monitors()
mnum=1
Y2=620
def speak_ans():
    global query
    j=0
    query=list(query)
    while j<len(query):
        if query[j] in ['-','>']:
            query[j]=' '
        else:
            j=j+1
    query=''.join(query)
    name=platform.system().lower()
    if name=='windows' or name=='linux':
        engine = pyttsx3.init('sapi5')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say(query)
        engine.runAndWait()
    else:
        system('say '+query)
def speech_reg():
    speech_b.config(state='disabled')
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Listening......')
        audio = r.listen(source)
        try:
            print('tryt')
            text=r.recognize_google(audio,language='en-IN')
            on_click(0)
            entry.insert(0,text)
            send_b.invoke()
        except:
            print('Say that again please...')
        speech_b.config(state='active')
def sen_checking(query):
    global c,words
    m=''
    for i in query:
        if i not in words:
            c=1
            m=m+i+" is improper please correct it\n"
    if c==1:
        m=m+"\nNOTE:-Don't use any person name in case if you have used please remove" 
        bot_reply=Label(f3,wraplength="310",text=m,justify=LEFT)
        bot_reply.pack(side='left')
def faq1():
    global b1
    on_click(0)
    entry.insert(0,b1['text'])
    send_b.invoke()
def faq2():
    global b2
    on_click(0)
    entry.insert(0,b2['text'])
    send_b.invoke()
def faq3():
    global b3
    on_click(0)
    entry.insert(0,b3['text'])
    send_b.invoke()
def faq4():
    global b4
    on_click(0)
    entry.insert(0,b4['text'])
    send_b.invoke()
def faq5():
    global b5
    on_click(0)
    entry.insert(0,b5['text'])
    send_b.invoke()
def faq6():
    global b6
    on_click(0)
    entry.insert(0,b6['text'])
    send_b.invoke()
def click_lbl(event):
    w=Toplevel()
    p=PhotoImage(file='flowChart.png')
    la=Label(w,image=p)
    la.pack()
    w.mainloop()
def forward():
    global back_b,forward_b,l_reg,rlist
    back_b.configure(state=ACTIVE)
    global i
    if i==len(rlist)-2:
        forward_b.config(state=DISABLED)
    i=i+1
    l_reg.grid_forget()
    l_reg.config(image=rlist[i])
    l_reg.grid(row=0,column=0)
def back():
    global back_b,forward_b,l_reg,rlist
    global i
    if i==len(rlist)-1:
        forward_b.config(state=ACTIVE)
    if i==0 or i==1:
        back_b.config(state=DISABLED)
    i=i-1
    l_reg.grid_forget()
    l_reg.config(image=rlist[i])
    l_reg.grid(row=0,column=0)
def registration_pics():
    global back_b,forward_b,l_reg,rlist
    rwin=Toplevel()
    f=Frame(rwin)
    rpic1=PhotoImage(file='1.png')
    rpic2=PhotoImage(file='2.png')
    rpic2_1=PhotoImage(file='2_1.png')
    rpic3=PhotoImage(file='3.png')
    rpic4=PhotoImage(file='4.png')
    rpic5=PhotoImage(file='5.png')
    rpic6=PhotoImage(file='6.png')
    rlist=[rpic1,rpic2,rpic2_1,rpic3,rpic4,rpic5,rpic6]
    l_reg=Label(rwin,image=rpic1)
    l_reg.grid(row=0,column=0,columnspan=3)
    f.grid()
    back_b=Button(f,text='<<',command=back,state=DISABLED)
    back_b.grid(row=0,column=0)
    forward_b=Button(f,text='>>',command=forward)
    forward_b.grid(row=0,column=2)
    rwin.mainloop()
def lodging_pics():
    global back_b,forward_b,l_reg,rlist
    rwin=Toplevel()
    f=Frame(rwin)
    rpic1=PhotoImage(file='pg_1.png')
    rpic2=PhotoImage(file='pg_2.png')
    rpic2_1=PhotoImage(file='pg_2_1.png')
    rpic3=PhotoImage(file='pg_3.png')
    rpic4=PhotoImage(file='pg_4.png')
    rpic5=PhotoImage(file='pg_5.png')
    rlist=[rpic1,rpic2,rpic2_1,rpic3,rpic4,rpic5]
    l_reg=Label(rwin,image=rpic1)
    l_reg.grid(row=0,column=0,columnspan=3)
    f.grid()
    back_b=Button(f,text='<<',command=back,state=DISABLED)
    back_b.grid(row=0,column=0)
    forward_b=Button(f,text='>>',command=forward)
    forward_b.grid(row=0,column=2)
    rwin.mainloop()
def query_filtering(query):
    global q_list,pun,fil
    query=list(query)
    j=0
    while j<len(query):
        if query[j] in pun:
            query[j]=' '
        else:
            j=j+1
    query=''.join(query)
    query=query.split()
    i=0
    while i<len(query):
        if query[i] in fil:
            query.remove(query[i])
        else:
            i=i+1
    q_list=query
    return query
def response(query):
    global ind
    cl=[]
    print(query)
    for i in quest:
        c=0
        for j in query:
            if j in i:
                c=c+1
        cl.append(c)
        if c==len(query):
            break
    x=max(cl)
    print(cl)
    ind=cl.index(x)
    return answers[ind]
def on_click(event):
    global entry
    entry.delete(0,END)
    send_b.configure(state='active')
    entry.configure(fg='black')
    entry.unbind('<Button-1>')
    entry.bind('<Return>',user_Q)
def user_Q(x):
    global f3,c,query
    c=0
    back='lightgray'
    query=entry.get()
    d_query=query
    if query=="":
        return
    entry.delete(0,END)
    frame.pack(fill=BOTH, expand=True)
    f2=Frame(frame.inner,bg=back,borderwidth=10)
    label=Label(f2,wraplength="400",text=query,justify=LEFT,fg='white',bg='blue',font=("bold", 15))
    label.pack(side='right')
    dt=Frame(frame.inner,bg=back,borderwidth=10)
    dtl=Label(dt,text=str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second)+'  '+str(datetime.now().day)+'/'+str(datetime.now().month)+'/'+str(datetime.now().year))
    dtl.pack(side='right')
    f2.pack(side=TOP,fill='x')
    dt.pack(fill='x')
    f3=Frame(frame.inner,borderwidth=10,bg=back)
    f3.pack(side=TOP,fill='x')
    f4=Frame(frame.inner,borderwidth=10,bg=back)
    lpic=Label(f3,image=pic,justify=LEFT,bg=back)
    lpic.pack(side='left')
    query=query.lower()
    query=query_filtering(query)
    sen_checking(query)
    if c==1:
        return
    query=response(query)
    if d_query in ['who are you','can i know about you']:
        query=' I am bot you can ask me any queries related to this website'
    if d_query in ['how can i call you']:
        query="I don't have any name.Just type your query"
    bot_reply=Label(f3,wraplength="310",text=query,justify=LEFT)
    bot_reply.pack(side='left')
    global i
    if ind==8:
            b=Button(f4,text='registration',command=registration_pics)
            b.pack()
            f4.pack()
            i=0
    else:
       if ind==6:
            b=Button(f4,text='lodge',command=lodging_pics)
            b.pack()
            f4.pack()
            i=0
       elif ind==9:
                picf=PhotoImage(file='flow1.png')
                flow=Label(f4,image=picf)
                flow.pack()
                flow.bind('<Button-1>',click_lbl)
                f4.pack()
    f5=Frame(frame.inner,borderwidth=10,bg=back)
    b_speak=Button(f5,text="Speak",command=speak_ans)
    b_speak.pack()
    f5.pack()
    frame.pack(fill=BOTH, expand=True)
    frame. _on_frame_configure()
def chatbot():
    global entry,send_b,speech_b,frame,pic,quest,answers,b1,b2,b3,b4,b5,b6,pun,fil,words
    questions=open('questions.txt',encoding='UTF-8').read().split('$')
    quest=[i.split() for i in questions]
    answers=open('answers.txt',encoding='UTF-8').read().split('$')
    pun=open('puntuations.txt',encoding='UTF-8').read().split()
    fil=open('query_filters.txt',encoding='UTF-8').read().split()
    words=open('Overall words.txt').read().split('\n')
    window=Tk()
    f1=Frame(window)
    w=(m[0].width)-456
    h=(m[0].height)-(88+620)
    window.geometry('444x620+'+str(w)+'+'+str(h))
    window.configure(bg='lightgray')
    window.resizable(0,0)
    window.title('Chat Bot')
    pic1=PhotoImage(file='main.png')
    l=Label(window,image=pic1,bg='lightgray')
    l.pack()
    pic=PhotoImage(file='bot.png')
    window.iconbitmap('icon.ico')
    f1.configure(background='light gray')
    f1.pack(side='bottom')
    entry=Entry(f1,width=62,fg='grey')
    entry.pack(side='left')
    entry.insert(0,"Enter Your Query Here")
    entry.bind('<Button-1>',on_click)
    voiceicon=PhotoImage(file='microphone.png')
    sendicon=PhotoImage(file='send.png')
    send_b=Button(f1,image=sendicon,command=lambda:user_Q(frame.canvas.yview_moveto(1)),state=DISABLED)
    send_b.pack(side='left')
    speech_b=Button(f1,image=voiceicon,command=speech_reg)
    speech_b.pack(side='left')
    frame = VerticalScrolledFrame(window, 
            width=444,height=620, 
            background='lightgray')
    topframe=Frame(frame.inner,bg='lightgray',borderwidth=10)
    topframe.pack(fill='x')
    b1=Button(topframe,text="About CPGRAMS",command=faq1,borderwidth=4,relief='raised')
    b1.pack(side='left')
    l=Label(topframe,text="  ",bg='lightgray')
    l.pack(side='left')
    b2=Button(topframe,text="Registration Process",command=faq2,borderwidth=4,relief='raised')
    b2.pack(side='left')
    l=Label(topframe,text="  ",bg='lightgray')
    l.pack(side='left')
    b3=Button(topframe,text="How to Lodge a Grievance",command=faq3,borderwidth=4,relief='raised')
    b3.pack(side='left')
    topframe1=Frame(frame.inner,bg='lightgray',borderwidth=10)
    topframe1.pack(fill='x')
    b4=Button(topframe1,text="Contact Details of DARP&G",command=faq4,borderwidth=4,relief='raised')
    b4.pack(side='left')
    l=Label(topframe1,text="  ",bg='lightgray')
    l.pack(side='left')
    b6=Button(topframe1,text="Time taken for grievance redressal",command=faq6,borderwidth=4,relief='raised')
    b6.pack(side='left')
    topframe2=Frame(frame.inner,bg='lightgray',borderwidth=10)
    topframe2.pack()
    b5=Button(topframe2,text="Flow of Grievance",command=faq5,borderwidth=4,relief='raised')
    b5.pack(side='left')
    l=Label(topframe2,text="                        ",bg='lightgray')
    l.pack(side='left')
    frame.pack()
    window.mainloop()
def mainicon():
    pic=image.load_animation('icon.gif')
    picsprite=sprite.Sprite(pic)
    w=picsprite.width
    h=picsprite.height
    win=window.Window(w,h,"chat bot",style='borderless')
    win.set_location((m[0].width)-136,(m[0].height)-168)
    gl.glClearColor(1,1,1,1)
    @win.event
    def on_mouse_press(x, y, button, modifiers):
        if button==window.mouse.LEFT:
            win.close()
            chatbot()
    @win.event
    def on_draw():
        win.clear()
        picsprite.draw()
    app.run()
mainicon()
