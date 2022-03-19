from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql


#########fuctional part########

def login_window():
    root.destroy()
    import loginpage
    #clear function
def clear():
    entryfirstname.delete(0,END)
    entrylastname.delete(0, END)
    enterycontact.delete(0,END)
    enteryemail.delete(0,END)
    enterypassword.delete(0,END)
    comboquestion.current(0)
    check.set(0)




    #error message fo emplty field

def register():
    if entryfirstname.get()==''or entrylastname.get()==''or enteryemail.get()=='' or enterycontact.get()==''\
        or enterypassword.get()=='' or enteryconfirmpassword.get()=='' or comboquestion.get()=='Select'or enteryanswer.get()=='':
        messagebox.showerror('Error','All Fields Are Required', parent=root)

    #password mismatch

    elif enterypassword.get()!=enteryconfirmpassword.get():
        messagebox.showerror('Error', 'Password Mismatch',parent=root)

    #check button check
    elif check.get()==0:
        messagebox.showerror('Error','Agree to our terms and conditions',parent=root)

#Database connection
    else:
        try:

            con=pymysql.connect(host='localhost',user='root',password='chiranjeevKCR',database='FinalProject')
            cur=con.cursor()
            cur.execute('select * from student where email=%s ',enteryemail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('Error','User Already Exists')
            else:
                cur.execute('insert into student (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                            (entryfirstname.get(),entrylastname.get(),enterycontact.get(),enteryemail.get(),
                             comboquestion.get(),enteryanswer.get(),enterypassword.get()))
                con.commit()
                con.close()

                messagebox.showinfo('Success','Registration is succesfull')
                clear()
                root.destroy()
                import loginpage

        except Exception as e:
            messagebox.showerror('error', f'Error due to {e}')




#########GUI part#########
root=Tk()

root.geometry('1350x750+20+20')
root.title('EasyConfig Application')

bgimage=PhotoImage(file='bg.png')
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0,y=0)

registerFrame=Frame(root,width=650,height=650)
registerFrame.place(x=630,y=30)

titleLabel=Label(registerFrame,text='EasyConfig Registration Form',font=('arial',22,'bold'),fg='black')
titleLabel.place(x=20,y=5)

#register form first name
firstnameLable=Label(registerFrame,text='First Name', font=('times new roman',18,'bold'),fg='gray50')
firstnameLable.place(x=20,y=80)
entryfirstname=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entryfirstname.place(x=20,y=115)

#register form last name
lastnameLable=Label(registerFrame,text='Last Name', font=('times new roman',18,'bold'),fg='gray50')
lastnameLable.place(x=370,y=80)
entrylastname=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entrylastname.place(x=370,y=115)

#contact number
contactLable=Label(registerFrame,text='Contact', font=('times new roman',18,'bold'),fg='gray50')
contactLable.place(x=20,y=200)
enterycontact=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
enterycontact.place(x=20,y=235)

#email
emaillabel=Label(registerFrame,text='E-mail', font=('times new roman',18,'bold'),fg='gray50')
emaillabel.place(x=370,y=200)
enteryemail=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
enteryemail.place(x=370,y=235)

#question
questionlabel=Label(registerFrame,text='Security Question', font=('times new roman',18,'bold'),fg='gray50')
questionlabel.place(x=20,y=320)
comboquestion=Combobox(registerFrame,font=('times new roman', 16),state='readonly')
comboquestion['values']=('Select','Your Pet Name?','Date of Birth?','Birth place?','Best friend Name?','Your favorite hobbie?')
comboquestion.place(x=20,y=355)
comboquestion.current(0)

#Answer
answerlabel=Label(registerFrame,text='Answer', font=('times new roman',18,'bold'),fg='gray50')
answerlabel.place(x=370,y=320)
enteryanswer=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
enteryanswer.place(x=370,y=355)

#password
passwordlabel=Label(registerFrame,text='Password', font=('times new roman',18,'bold'),fg='gray50')
passwordlabel.place(x=20,y=440)
enterypassword=Entry(registerFrame,font=('times new roman',18),bg='lightgray',show='*')
enterypassword.place(x=20,y=475)

#comfirm password
confirmpasswordlabel=Label(registerFrame,text='Confirm Password', font=('times new roman',18,'bold'),fg='gray50')
confirmpasswordlabel.place(x=370,y=440)
enteryconfirmpassword=Entry(registerFrame,font=('times new roman',18),bg='lightgray',show='*')
enteryconfirmpassword.place(x=370,y=475)

#check buttom for user agreements
check=IntVar()
checkButton=Checkbutton(registerFrame,text='I Agree All the terms and conditions' ,onvalue=1,offvalue=0,variable=check,font=('times new roman', 14,'bold'))
checkButton.place(x=20,y=530)

#register now button
buttonimage=PhotoImage(file='button.png')
registerButton=Button(registerFrame,image=buttonimage,bd=0,cursor='hand1',command=register)
registerButton.place(x=250,y=580)

#login image left side
loginimage=PhotoImage(file='log.png')
loginButton=Button(root,image=loginimage,bd=0,bg='black',cursor='hand1',command=login_window)
loginButton.place(x=230,y=330)



root.mainloop()