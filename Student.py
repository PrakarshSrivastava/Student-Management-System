###########################################################ADD SUBMIT

#####################################################################ConnectButtons
def addstudent():
    def submitadd():#this is your part first we have to get data
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime=time.strftime('%H:%M:%S')#we also have column of these two
        addeddate=time.strftime('%d/%m/%Y')
        try:#TRY check the constraints in the database
            s='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(s,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))#sequence same
            con.commit()#if we want to modify then we have to use commit like apdate,add
            res=messagebox.askyesnocancel('Notifications','Id {} Name {} Added Successfully And Want To Clean The Form'.format(id,name),parent=addroot)#if we have filled the data and if we leave it as it is then we have to delete one bye one like id name email etc to overcome this we ask the use what to do
            #means yes or no
            if res==True:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:#primary key voilation
            messagebox.showerror('Notifications','ID Already Exist Try Another ID',parent=addroot)

        #to show data in columns in show data frame
        s='select * from studentdata1'
        mycursor.execute(s)
        datas=mycursor.fetchall()#ye sara data datas variable mh daal dega ur jo data aynge wo sare tuples k form mh aayenge
        #pehle data ko clean karenge kyu screen pr rahega to baar dikhega
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
            studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview
        #Addded PART Done :)


    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('Custom-Icon-Design-Pretty-Office-10-Student-id.ico')
    addroot.resizable(False,False)
    #--------------------------------------------------------------addStudentLabels
    idlabel=Label(addroot,text='Enter Id',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Enter Name',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Enter Mobile',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Enter Email',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Enter Address',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(addroot,text='Enter Gender',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(addroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    ########################################### Add Student Entry #################################################################
    idval=StringVar()
    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval=StringVar()
    nameentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileval=StringVar()
    mobileentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailval=StringVar()
    emailentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=370)

    addressval=StringVar()
    addressentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    genderval=StringVar()
    genderentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=250)

    dobval=StringVar()
    dobentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)
    #---------------------------------------------------------AddButton
    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()
def searchstudent():
    ###########################################################ADD SUBMIT
    def search():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addeddate=time.strftime('%d/%m/%Y')#we can search with date also but not with time
        if (id!=''):
            s='select * from studentdata1 where id =%s'
            mycursor.execute(s,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (name!=''):
            s='select * from studentdata1 where name =%s'
            mycursor.execute(s,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (mobile!=''):
            s='select * from studentdata1 where mobile =%s'
            mycursor.execute(s,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (email!=''):
            s='select * from studentdata1 where email =%s'
            mycursor.execute(s,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (address!=''):
            s='select * from studentdata1 where address =%s'
            mycursor.execute(s,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (gender!=''):
            s='select * from studentdata1 where gender =%s'
            mycursor.execute(s,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (dob!=''):
            s='select * from studentdata1 where dob =%s'
            mycursor.execute(s,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        elif (addeddate!=''):
            s='select * from studentdata1 where addeddate =%s'
            mycursor.execute(s,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]#as we get datas in the form of tuples
                studenttable.insert('',END,values=vv)#start se end tak jayga and it stores values in column wise automatically in ttk treeview

        #Search PART Done :)




    #####################################################################ConnectButtons
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('Custom-Icon-Design-Pretty-Office-10-Student-id.ico')
    searchroot.resizable(False,False)
    #--------------------------------------------------------------addStudentLabels
    idlabel=Label(searchroot,text='Enter Id',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(searchroot,text='Enter Name',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(searchroot,text='Enter Mobile',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(searchroot,text='Enter Email',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(searchroot,text='Enter Address',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(searchroot,text='Enter Gender',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(searchroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(searchroot,text='Enter Date',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    ########################################### Add Student Entry #################################################################
    idval=StringVar()
    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval=StringVar()
    nameentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileval=StringVar()
    mobileentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailval=StringVar()
    emailentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressval=StringVar()
    addressentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderval=StringVar()
    genderentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobval=StringVar()
    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateval=StringVar()
    dateentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    #---------------------------------------------------------AddButton
    submitbtn=Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150,y=490)



    searchroot.mainloop()
def deletestudent():
    cc=studenttable.focus()  #tree view mh ek faida h jha click kre wo hme pta chl jayga by .focus ur cc batayga ki kis place pr hmne click kiya h
    content=studenttable.item(cc)#hme sara content mil jayga us place pr jha click kiye h cc ki madad se ur dict k form mh return karega
    pp=content['values'][0]#it gives id
    s='delete from studentdata1 where id=%s' #delete querry
    mycursor.execute(s,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully'.format(pp))#yha tk done means delte ho chuka h but at a time nhi show kr rha h
    s='select * from studentdata1'
    mycursor.execute(s)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  # as we get datas in the form of tuples
        studenttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        time=timeval.get()
        date=dateval.get()
        #update querry
        s='update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(s,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','ID {} modified successfully'.format(id),parent=updateroot)
        s='select * from studentdata1'
        mycursor.execute(s)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  # as we get datas in the form of tuples
            studenttable.insert('', END, values=vv)

    #####################################################################ConnectButtons
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x600+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('Custom-Icon-Design-Pretty-Office-10-Student-id.ico')
    updateroot.resizable(False,False)
    #--------------------------------------------------------------addStudentLabels
    idlabel=Label(updateroot,text='Enter Id',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Enter Name',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Enter Mobile',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Enter Email',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Enter Address',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(updateroot,text='Enter Gender',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(updateroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Enter Date',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot,text='Enter Time',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    ########################################### Add Student Entry #################################################################
    idval=StringVar()
    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameval=StringVar()
    nameentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileval=StringVar()
    mobileentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailval=StringVar()
    emailentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressval=StringVar()
    addressentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderval=StringVar()
    genderentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobval=StringVar()
    dobentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateval=StringVar()
    dateentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeval=StringVar()
    timeentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)

    #---------------------------------------------------------AddButton
    submitbtn=Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150,y=550)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if len(pp)!=0:# tm jha click karoge wha ka data update waale mh chla jayga
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()


def showstudent():
    s = 'select * from studentdata1'
    mycursor.execute(s)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]  # as we get datas in the form of tuples
        studenttable.insert('', END, values=vv)


def exportstudent():#convert in readable file for this we have use pandas and save data in file in local we use file dialog
    pass
    '''ff=filedialog.asksaveasfilename()#This will give the path where we have stored
gg=studenttable.get_children()#all columns data in tuple form
id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
for i in gg:
    content=studenttable.item(i)
    pp=content['values']
    id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
paths=r'{}.csv'.format(ff)
messagebox.showinfo('Notifications','Student Data Saved {}'.format(paths))'''
def exitstudent():
    res=messagebox.askyesnocancel('Do You Want To Exit ?')
    if res==True:
        root.destroy()
######################################ConnectToDatabase###################################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:#try password k liye likha gya h if sahi h to try chlega ur agr nhi to except wala chalega
            con=pymysql.connect(host=host,user=user,password=password)#i have taken a variable as a handler isi se hm baar baar kaam krenge
            mycursor=con.cursor()#defufaut hota ye dono line this is also a handler
            #in dono ko global is liye kiya h ki hme ise har jgh use krna hota h
        except:#if entered wrong in the above
            messagebox.showerror('Notifications','Data is incorrect please try again')
            return
        try:# ye code ek hi baar chalega try yha isliye use kiye h ki jb hum isko istalable bnaynge ur jb denge kisi ko use bnana na pde ye sab automatic create ho jay
            s='create database studentmanagementsystem1' #name
            mycursor.execute(s)#execute wil create database
            s='use studentmanagementsystem1'#to create tables in database first we have to use this database
            mycursor.execute(s)#ab use karega
            s='create table studentdata1(id int,name varchar(20),mobile varchar(20),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(s)#this will create table
            s='alter table studentdata1 modify column id int not null'#to make id primary key we have used alter(modify)
            mycursor.execute(s)
            s='alter table studentdata1 modify column id int primary key'#this will make id as primary key
            mycursor.execute(s)#this will make in table
            messagebox.showinfo('Notification', ' Database created and Now You are connected', parent=dbroot)#neche dekho

        except:#jb hamare pehle se bna hoga tb except chalega
            s='use studentmanagementsystem1'
            mycursor.execute(s)
            messagebox.showinfo('Notification','Now You are connected to the database',parent=dbroot)#jb connect hoga tb notify karega,parent kiske uper aayga
        dbroot.destroy()# try ur except kch na chle



    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.iconbitmap('Custom-Icon-Design-Pretty-Office-10-Student-id.ico')
    dbroot.resizable(False, False)
    dbroot.geometry('470x250+800+230')
    dbroot.config(bg='blue')
    #-----------------------------------------------------------------------ConnectDBLabel---------
    hostlabel=Label(dbroot,text='Enter Host: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel=Label(dbroot,text='Enter User: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel=Label(dbroot,text='Enter Password: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)
    #--------------------------------------------------------------------------ConnectDbEntry---------------------
    hostval=StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    #-------------------------------------------------------------------------ConnectDbButton---------------
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,bg='red2',activebackground='blue',activeforeground='white',bd=5,command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()
######################################################################################
def tick():
    time_string=time.strftime('%H:%M:%S')
    date_string=time.strftime('%d/%m/%Y')
    clock.config(text='Date:'+date_string+'\n'+'Time:'+time_string)
    clock.after(200,tick)
#############################################INTROSLIDER#########################################
import random
colors=['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)


def IntroLabelTick():
    global count,text
    if count>=len(ss):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text+=ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(100,IntroLabelTick)

#########################################################################################333
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
import time
import pandas
root=Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap('Custom-Icon-Design-Pretty-Office-10-Student-id.ico')
root.resizable(False,False)
##############################################################FRAMES################################################
#---------------------------------------------------------------------------DataEntryFrame---------
DataEntryFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel=Label(DataEntryFrame,text='----------Welcome----------',width=25,font=('chiller',25,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)

addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


ShowDataFrame=Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
#-------------------------------------------------------------------------------------------ShowData
#####################################################################################Styleofcolumns
style=ttk.Style()
style.configure('Treeview',font=('times',15,' bold'),backgroung='cyan',foreground='blue')
style.configure('Treeview.Heading',font=('chiller',20,' bold'),foreground='blue')

scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable=Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('Id',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='E-mail')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
################################################################removeZeroIndex
studenttable['show']='headings'
##################################################################Size of Colomns
studenttable.column('Id',width=100)
studenttable.column('Name',width=100)
studenttable.column('Mobile No',width=100)
studenttable.column('Email',width=100)
studenttable.column('Address',width=100)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=100)
studenttable.column('Added Date',width=100)
studenttable.column('Added Time',width=100)
########################################################################################Background of show
studenttable.pack(fill=BOTH,expand=1)


####################################################Slider##################################################
ss='Welcome To Student Management System'
count=0
text=''
###################################################################################################################
SliderLabel=Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
####################################################################################CLOCK###############################
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()
############################################ConnectToDataBaseButton####################################################
connectbutton=Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()
