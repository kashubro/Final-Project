from tkinter import*
from tkinter import messagebox
import pymysql
from tkinter import ttk
#fuction#####
    ##############reset password#############

def reset_password():
    if mailentry.get()=='':
        messagebox.showerror('Error','Please enter the email address to reset password')
    else:
        con=pymysql.connect(host='localhost',user='root',password='chiranjeevKCR',database='FinalProject')
        cur=con.cursor()
        cur.execute('select * from student where email=%s',mailentry.get())
        row=cur.fetchone()
        if row==None:
            messagebox.showerror('Error','Please enter a valid email address')
        else:
            con.close()

            def change_password():
                if securityquesCombo.get()=='Select' or answerEntry.get()==''or newpassEntry.get()=='':
                    messagebox.showerror('Error','All Fields are required')
                else:
                    con=pymysql.connect(host='localhost',user='root',password='chiranjeevKCR',database='FinalProject')
                    cur=con.cursor()
                    cur.execute('select * from student where email=%s and question=%s and answer=%s',(mailentry.get(),
                                securityquesCombo.get(),answerEntry.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror('Error','Security Question or Answer is incorrect',parent=root2)
                    else:
                        cur.execute('update student set password=%s where email=%s',(newpassEntry.get(),mailentry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success','Your Password is changed. Login with new Password',parent=root2)
                        securityquesCombo.current(0)
                        answerEntry.delete(0,END)
                        newpassEntry.delete(0,END)
                        root2.destroy()
            root2=Toplevel()
            root2.title('Foget Password')
            root2.geometry('470x568+400+60')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()
            forgetLabel=Label(root2,text='Forget',font=('times new roman',22,'bold'),bg='white')
            forgetLabel.place(x=128,y=10)

            forgetpassLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), bg='white',fg='green')
            forgetpassLabel.place(x=225, y=10)

            passwordimage=PhotoImage(file='password.png')
            passImageLabel=Label(root2,image=passwordimage,bg='black')
            passImageLabel.place(x=170,y=70)

            securityquestionlabel=Label(root2,text='Security Question',font=('times new roman',15,'bold'),bg='white')
            securityquestionlabel.place(x=68,y=235)

            securityquesCombo=ttk.Combobox(root2,font=('times new roman',15,),state='readonly')
            securityquesCombo['values']=('Select','Your Pet Name?','Date of Birth?','Birth place?','Best friend Name?','Your favorite hobbie?')

            securityquesCombo.place(x=60,y=280)
            securityquesCombo.current(0)

            answerLabel=Label(root2,text='Answer',font=('times new roman',15,'bold'),bg='white')
            answerLabel.place(x=60,y=310)

            answerEntry = Entry(root2, font=('times new roman', 15,), fg='black', width=30,
                                      bg='white')
            answerEntry.place(x=60, y=350)

######## new password######

            newpassLabel = Label(root2, text='New Password', font=('times new roman', 15, 'bold'), fg='black',
                                 bg='white')
            newpassLabel.place(x=60, y=400)

            newpassEntry = Entry(root2, font=('times new roman', 15,), fg='black', width=30,
                                 bg='white')
            newpassEntry.place(x=60, y=440)

######### change password button#########

            changepassbutton = Button(root2, text='Change Password', font=('arial', 17, 'bold'), bg='green',
                                      fg='white', cursor='hand2', activebackground='green',
                                      activeforeground='white',
                                      command=change_password)
            changepassbutton.place(x=130, y=500)



            root2.mainloop()

    ##########connect with main#########
def register_window():
    window.destroy()
    import FinalProject


def sigin():
    if mailentry.get()==''or passentry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    else:
        try:
            ####Database connection##########
            con=pymysql.connect(host='localhost',user='root',password='chiranjeevKCR',database='FinalProject')
            cur=con.cursor()
            cur.execute('select * from student where email=%s and password=%s',(mailentry.get(),passentry.get()))
            row=cur.fetchone()

            if row==None:
                messagebox.showerror('Error','Invaild Email or Password')
            else:
                messagebox.showinfo('Success','Welcome to EasyConfig')
                window.destroy()
                import chat

        except Exception as e:
            messagebox.showerror('Error',f'Error is due to {e}')
#GUI#########
window=Tk()

window.geometry('900x600+50+50')
window.title('EasyConfig login page')

#background image
bgloginimage=PhotoImage(file='login.png')
bgloginLable=Label(window,image=bgloginimage)
bgloginLable.place(x=0,y=0)

# user image

frame=Frame(window,width=560,height=320,bg='white')
frame.place(x=180,y=140)

userimage=PhotoImage(file='user.png')
userimageLabel=Label(frame,image=userimage, bg='black')
userimageLabel.place(x=15,y=50)

#maillabel

maillabel=Label(frame,text='Email',font=('arial',20,'bold'),bg='white')
maillabel.place(x=280,y=70)
mailentry=Entry(frame,font=('arial',20),bg='white',fg='black')
mailentry.place(x=280,y=110)

#password label

passLabel = Label(frame, text='Password', font=('arial', 20, 'bold'), bg='white', fg='black')
passLabel.place(x=280, y=150)
passentry = Entry(frame, font=('arial', 20,), bg='white', fg='black',show='*')
passentry.place(x=280, y=200)

#register button
regbutton = Button(frame, text='Register New Account?', font=('arial', 10,), bd=0, fg='gray20', bg='white',
                   cursor='hand2',activebackground='white', activeforeground='gray20',command=register_window)
regbutton.place(x=280, y=250)

#forget password button
forgetbutton = Button(frame, text='Forget Password?', font=('arial', 9,), bd=0, fg='red', bg='white',
                      cursor='hand2',activebackground='white', activeforeground='gray20',command=reset_password)
forgetbutton.place(x=450, y=250)

#login button

loginbutton2 = Button(frame, text='Login', font=('arial', 10, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white',command=sigin)
loginbutton2.place(x=470, y=280)





window.mainloop()