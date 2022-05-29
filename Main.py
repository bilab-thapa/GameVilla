
'''========================================================================= Starting ==================================================================================================='''
from tkinter import *
from tkinter import messagebox
import sys
import os
import pickle
import tkinter as tk
import random

'''====================================================================== Screen Destroy ====================================================================================================='''
def del1():
    screensuc.destroy()
    screenlog.destroy()
    mainpage()
def del2():
    screenw.destroy()
def del3():
    screene.destroy()
def back():
    
    screenreg.destroy()
    main_screen()
def back1():
    
    screenlog.destroy()
    main_screen()

def reserve():
    root.destroy()
    messagebox.showinfo('Reserved', 'You will Be Notified Shortly. Thank You......... ')

def creserve():
    croot.destroy()
    messagebox.showinfo('Reserved', 'You will Be Notified Shortly. Thank You......... ')
'''====================================================================== Login Sucess =================================================================================================================='''


def login_sucess():
    global screensuc
    screensuc = Tk()
    screensuc.config(bg = 'royalblue4')
    screensuc.title("Sucess")
    screensuc.geometry('200x150')
    Label(screensuc,text = "", bg= 'royalblue4').pack()
    Label(screensuc,text = "", bg = 'royalblue4').pack()
    Label(screensuc, text = 'Logged In Sucessfully.').pack(fill = X)
    Label(screensuc,text = "", bg = 'royalblue4').pack()
    Button(screensuc, text = 'OK', command = del1).pack()


'''==================================================================== Incorrect Password ==============================================================================================='''      

def wpassword():
    global screenw
    screenw = Tk()
    screenw.title("Wrong Password")
    screenw.geometry('300x150')
    screenw.config(bg = 'steel blue')
    Label(screenw,text = "", bg = 'steel blue').pack()
    Label(screenw,text = "", bg = 'steel blue').pack()
    Label(screenw,fg = 'red', text = 'Password might be incorrect.').pack(fill = X)
    Label(screenw,text = "", bg = 'steel blue').pack()
    Button(screenw, text = 'OK', command = del2).pack()


'''======================================================================== User Error ============================================================================================'''    

def user_error():
    global screene
    screene = Tk()
    screene.title("User Error")
    screene.geometry('300x150')
    screene.config(bg= 'darkorchid2')
    Label(screene,text = "",bg = 'darkorchid2').pack()
    Label(screene,text = "",bg = 'darkorchid2').pack()
    Label(screene, text = 'No Available User Found.',fg = 'green2', font = ('arial',10,'bold')).pack(fill = X)
    Label(screene,text = "",bg = 'darkorchid2').pack()
    Button(screene, text = 'OK', command = del3).pack()


'''========================================================================= Registration ========================================================================================='''
 
def register_info():
    
    username_info = username.get()
    password_info = password.get()

    data = [username_info, password_info]

    with open (username_info, 'ab')as file_1:
        pickle.dump(data, file_1)
    if not username_info or not password_info:
        Label(screenreg, text = 'Invalid Reg',fg = 'red', bg = 'white').pack(fill = X)
    else: 
        Label(screenreg, text = 'Successfully registered your data', fg = 'green', font = ('arial',10,'bold')).pack(pady = 5)



'''=========================================================================== Login Check =============================================================================================='''

def login_check():
    try:

        usernamex = username_verify.get()
        passwordx = password_verify.get()
        username_entry2.delete(0, END)
        password_entry2.delete(0,END)

        file_1 = os.listdir()
        print (usernamex)
        with open (usernamex,'rb') as file_2:
            d = pickle.load(file_2)
            print(d)
        
        if usernamex in d[0]:
            if not passwordx:
                wpassword()
            elif passwordx in d[1]:
                login_sucess()
            
            else:
                wpassword()
        elif not usernamex and not passwordx:
            user_error()
        elif not usernamex:
            wpassword()
        elif not passwordx:
            wpassword()
        else:
            user_error()
    except FileNotFoundError:
        user_error()


'''========================================================================== Register Window =================================================================================='''

def register():
    screen.destroy()
    global screenreg
    screenreg = Tk()
    screenreg.title("Register")
    screenreg.state('zoomed')
    screenreg.config(bg='#3b5998')
    
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()


    Label(screenreg,text = "",bg='#3b5998').pack()
    Label(screenreg,text = "",bg='#3b5998').pack()
    Label(screenreg,text = "Enter your info below:", bg ='white',fg = 'black').pack(fill = X)
    Label(screenreg,text = "",bg='#3b5998').pack()
    Label(screenreg,text = "",bg='#3b5998').pack()
    Label(screenreg,text = "",bg='#3b5998').pack()

    Label(screenreg,text = 'Username',bg='#3b5998',fg = 'white').pack()
    username_entry = Entry(screenreg, textvariable = username)
    username_entry.pack()

    Label(screenreg,text = "",bg='#3b5998').pack()

    Label(screenreg,text = 'Password',bg='#3b5998',fg = 'white').pack()
    password_entry = Entry(screenreg, textvariable = password, show = '*')
    password_entry.pack()
    Label(screenreg,text = "",bg='#3b5998').pack()

    Button(screenreg ,text = 'Register', height = '1' , width = '10', command = register_info).pack()
    Label(screenreg,text = "",bg='#3b5998').pack()
    Button(screenreg,text ='Back',height = '1',width = '4',command = back).pack() 


'''=========================================================================== Login Window ==================================================================================='''

def login_verification():
    screen.destroy()
    global screenlog
    screenlog = Tk()
    screenlog.title("Login Page")
    screenlog.state('zoomed')
    screenlog.config(bg="#FF5700", )
    Label(screenlog,text = "",bg="#FF5700", ).pack()
    Label(screenlog,text = "",bg="#FF5700", ).pack()
    Label (screenlog, text = "  Please enter your login details: ",bg="white", ).pack(fill = X)
    Label(screenlog,text = "",bg="#FF5700", ).pack()
    Label(screenlog,text = "",bg="#FF5700", ).pack()
    
    
    global username_verify
    global password_verify
    global username_entry2
    global password_entry2

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screenlog, text = "Username :",bg="#FF5700").pack()
    username_entry2 = Entry(screenlog, textvariable = username_verify)
    username_entry2.pack()
    
    Label(screenlog,text = "",bg="#FF5700").pack()

    Label(screenlog, text = "Password :",bg="#FF5700").pack()
    password_entry2 = Entry(screenlog, textvariable = password_verify, show ='*')
    password_entry2.pack()

    Label(screenlog,text = "",bg="#FF5700").pack()

    c = Checkbutton(screenlog,text = 'Keep me signed in', bg = '#FF5700')
    c.pack()
    Label(screenlog,text = "",bg="#FF5700").pack()
    Button(screenlog, text = "Log In", width = 12, height = 1, command = login_check).pack()
    Label(screenlog,text = "",bg="#FF5700").pack()
    Button(screenlog,text ='Back',height = '1',width = '4',command = back1).pack() 
    

'''============================================================================== Main Screen ========================================================================================='''

def main_screen():
    global screen
    screen = Tk()
    screen.state('zoomed')
    screen.title('GAMEVILLA 0.1')
    screen.config(bg= 'indigo')
    Label (text = "WELCOME TO GAMEVILLA",height = 4,fg = 'blue', bg = 'gold', font = ('times new roman' ,16, 'bold')).pack(fill = X)
    Label(text = "", bg = 'indigo').pack()
    Button(text = "Login", height = '2', width = '30',fg = 'indigo', bg = '#00FF80', command = login_verification,font = ('times new roman' ,9, 'bold'), borderwidth = 7).pack()
    Label(text = '',fg = 'indigo', bg = 'indigo').pack()
    Label(text = '',fg = 'indigo', bg = 'indigo').pack()
    Label(text = '',fg = 'indigo', bg = 'indigo').pack()
    Label(text = '',fg = 'indigo', bg = 'indigo').pack()
    
    
    Button(text = "Register", height = '2', width = '30',fg = 'indigo', bg = '#00FF80', command = register,font = ('times new roman' ,9, 'bold'), borderwidth = 7).pack() 
    
    screen.mainloop()


'''============================================================================ Reservation Selection ===================================================================='''

def pcpage():
    class PC(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.master = master
            self.time = TIME(self)
            self.time.grid(row=0)

    class TIME(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.master = master
            self.onebtn = tk.Button(self, text='One Hour', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)
            self.twobtn = tk.Button(self, text='Two Hour', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)
            self.threebtn =  tk.Button(self, text = 'Three Hour',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)
            self.fourbtn = tk.Button(self, text = 'Four Hour',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)
            self.fivebtn = tk.Button(self, text = 'Five Hour',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)
            self.nightbtn = tk.Button(self, text = 'All Nighter',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = reserve)

            self.onebtn.pack(pady=5)
            self.twobtn.pack(pady=5)
            self.threebtn.pack(pady = 5)
            self.fourbtn.pack( pady = 5)
            self.fivebtn.pack(pady = 5)
            self.nightbtn.pack(pady = 5)

    def main():
        global root
        root = tk.Tk()
        root.title('PC Time')
        root.geometry('300x350')
        res = PC(root)
        res.pack()
        root.mainloop()

    if __name__ == '__main__':
        main()

def cpage():
    class C(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.master = master
            self.time = TIME(self)
            self.time.grid(row=0)

    class TIME(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.master = master
            self.onebtn = tk.Button(self, text='One Hour',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)
            self.twobtn = tk.Button(self, text='Two Hour',  bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)
            self.threebtn =  tk.Button(self, text = 'Three Hour', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)
            self.fourbtn = tk.Button(self, text = 'Four Hour', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)
            self.fivebtn = tk.Button(self, text = 'Five Hour', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)
            self.nightbtn = tk.Button(self, text = 'All Nighter', bg = '#fcec03', fg = 'black',font = ('times new roman' ,14, 'bold'), command = creserve)

            self.onebtn.pack(pady=5)
            self.twobtn.pack(pady=5)
            self.threebtn.pack(pady = 5)
            self.fourbtn.pack( pady = 5)
            self.fivebtn.pack(pady = 5)
            self.nightbtn.pack(pady = 5)

    def main():
        global croot
        croot = tk.Tk()
        croot.geometry('300x350')
        croot.title('Console Time')
        res = C(croot)
        res.pack()
        root.mainloop()

    if __name__ == '__main__':
        main()


        


'''=========================================================================== Store Page ==========================================================================================='''

def store():

    
    screenmain.destroy()
    class Bill:
        def __init__(self,root):
            self.root=root
            self.root.state('zoomed')
            self.root.title("Billing")
            bg_color='#00a5cf'
            Label(self.root,text="BILL PAYMENT  ",bd=15,bg='#e84302',fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

            #================ Hardware ==========================

            self.monitor=IntVar()
            self.mouse=IntVar()
            self.keyboard=IntVar()
            self.headphone=IntVar()
            self.speaker=IntVar()
            self.mousepad=IntVar()

            #================ Games ==========================
            
            self.pes=IntVar()
            self.gow=IntVar()
            self.rl=IntVar()
            self.cod=IntVar()
            self.gta=IntVar()
            self.pubg=IntVar()

            #================ Food and Cold Drinks ==========================

            self.momo=IntVar()
            self.chat=IntVar()
            self.chow=IntVar()
            self.coke=IntVar()
            self.fanta=IntVar()
            self.sprite=IntVar()

            #================ Total Product Price & Tax ==========================

            self.hardware_p=StringVar()
            self.games_p=StringVar()
            self.drinks_p=StringVar()

            self.hardware_tax=StringVar()
            self.game_tax=StringVar()
            self.drink_tax=StringVar()

            #================Cutomers==================================

            self.c_name=StringVar()
            self.c_phone=StringVar()

            self.bill_no=StringVar()
            x=random.randint(1000,9999)
            
            self.bill_no.set(str(x))

            self.search_bill=StringVar()




            #============================================Customer Frame ====================================
            file=LabelFrame(self.root,bd=8,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            file.place(x=0,y=80,relwidth=1)

            Label(file,text="Customer Name",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
            Entry(file,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

            Label(file,text="Contact No",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
            Entry(file,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

            Label(file,text="Bill Number",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
            Entry(file,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

            Button(file,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12").grid(row=0,column=6,padx=6,pady=10)


            #======================================== Hardware Frame ========================================
            
            F2=LabelFrame(self.root,bd=8,text="Hardwares",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F2.place(x=5,y=180,width=325,height=380)

            Label(F2,text="Monitor",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.monitor ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            Label(F2,text="Mouse",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.mouse ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

            Label(F2,text="Keyboard",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.keyboard, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

            Label(F2,text="Headphone",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.headphone, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            Label(F2,text="Speaker",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.speaker ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            Label(F2,text="Mousepad",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            Entry(F2,width=10,textvariable=self.mousepad ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            
            
            #============================ Games Section =====================================================
            
            F3=LabelFrame(self.root,bd=8,text="GameZones",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F3.place(x=340,y=180,width=325,height=380)

            Label(F3,text="PES",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.pes,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            Label(F3,text="God Of War",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.gow,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

            Label(F3,text="Rocket League",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.rl,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

            Label(F3,text="Call Of Duty",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.cod,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            Label(F3,text="GTA V",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.gta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            Label(F3,text="PUBG",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            Entry(F3,width=10,textvariable=self.pubg,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            

            #============================= Food and Drinks Section ===============================================
            
            F4=LabelFrame(self.root,bd=8,text="Food & Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F4.place(x=675,y=180,width=325,height=380)

            Label(F4,text="Momo",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.momo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            Label(F4,text="Chatpate",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.chat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

            Label(F4,text="Chowmin",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.chow,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

            Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            Label(F4,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
            
            Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
            
            #========================== Side Bill Section ==============================================
            F5=Frame(self.root,bd=8,relief=GROOVE)
            F5.place(x=1010,y=180,width=340,height=380)

            Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)		
            scrol_y=Scrollbar(F5,orient=VERTICAL)
            self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)
            

            #================================ Lables and Buttons =================================================

            F6=LabelFrame(self.root,bd=8,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
            F6.place(x=0,y=560,relwidth=1,height=140)
            Label(F6,text="Total Hardware Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.hardware_p,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

            Label(F6,text="Total Games Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.games_p,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
            Label(F6,text="Total Food&Drinks Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.drinks_p,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


            Label(F6,text="Hardware Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.hardware_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

            Label(F6,text="Games Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.game_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

            Label(F6,text="Food&Drinks Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
            Entry(F6,width=18,textvariable=self.drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


            btn_F=Frame(F6,bd=7,relief=GROOVE)
            btn_F.place(x=740,width=590,height=102)

            Button(btn_F,text="Total",command=self.total,bg="indigo",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
            Button(btn_F,text="Generate Bill",command=self.bill_area,bg="indigo",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
            Button(btn_F,text="Clear",command=self.clear_data,bg="indigo",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
            Button(btn_F,text="Exit",command=self.Exit_app,bg="indigo",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=3,padx=4,pady=5)
            
            self.welcome_bill()
    #======================== Total bills =======================================
        def total(self):
            self.c_s_p=self.monitor.get()*60000
            self.c_fc_p=self.mouse.get()*1500
            self.c_fw_p=self.keyboard.get()*5000
            self.c_hs_p=self.headphone.get()*4000
            self.c_hg_p=self.speaker.get()*20000
            self.c_bl_p=self.mousepad.get()*1000
            self.total_hardware=float(
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hs_p+
                                            self.c_hg_p+
                                            self.c_bl_p
                                            )
            self.hardware_p.set("Rs. "+str(self.total_hardware))
            self.c_tax=round((self.total_hardware*0.1),2)
            self.hardware_tax.set("Rs. "+str(self.c_tax))

            self.g_r_p=self.pes.get()*2800
            self.g_f_p=self.gow.get()*4000
            self.g_d_p=self.rl.get()*2000
            self.g_w_p=self.cod.get()*3000
            self.g_s_p=self.gta.get()*3000
            self.g_t_p=self.pubg.get()*2000

            self.total_games_p=float(
                                            self.g_r_p+
                                            self.g_f_p+
                                            self.g_d_p+
                                            self.g_w_p+
                                            self.g_s_p+
                                            self.g_t_p
                                            )
            self.games_p.set("Rs. "+str(self.total_games_p))
            self.g_tax=round((self.total_games_p*0.02),2)
            self.game_tax.set("Rs. "+str(self.g_tax))

            self.d_m_p=self.momo.get()*120
            self.d_c_p=self.chat.get()*80
            self.d_f_p=self.chow.get()*100
            self.d_t_p=self.coke.get()*60
            self.d_l_p=self.fanta.get()*60
            self.d_s_p=self.sprite.get()*60
            self.tdrinks_price=float(
                                            self.d_m_p+
                                            self.d_c_p+
                                            self.d_f_p+
                                            self.d_t_p+
                                            self.d_l_p+
                                            self.d_s_p
                                            )
            self.drinks_p.set("Rs. "+str(self.tdrinks_price))
            self.d_tax=round((self.tdrinks_price*0.05),2)
            self.drink_tax.set("Rs. "+str(self.d_tax))


            self.Total_bill=float(
                                    self.total_hardware+
                                    self.total_games_p+
                                    self.tdrinks_price+
                                    self.c_tax+
                                    self.g_tax+
                                    self.d_tax
                                )	

        def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t Welcome to Game Villa \n")
            self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n ====================================")
            self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
            self.txtarea.insert(END,f"\n ====================================")


        def bill_area(self):
            if self.c_name.get()=="" or self.c_phone.get()=="":
                messagebox.showerror("Error","Customer Details are must")
            elif self.hardware_p.get()=="Rs. 0.0" and self.games_p.get()=="Rs. 0.0" and self.drinks_p.get()=="Rs. 0.0" :
                messagebox.showerror("Error","No Product Purchased")
            else:	
                self.welcome_bill()
                #========Hardwares==========
                if self.monitor.get()!=0:
                    self.txtarea.insert(END,f"\n Monitor\t\t{self.monitor.get()}\t\t{self.c_s_p}")

                if self.mouse.get()!=0:
                    self.txtarea.insert(END,f"\n Mouse\t\t{self.mouse.get()}\t\t{self.c_fc_p}")

                if self.keyboard.get()!=0:
                    self.txtarea.insert(END,f"\n Keyboard\t\t{self.keyboard.get()}\t\t{self.c_fw_p}")
                
                if self.headphone.get()!=0:
                    self.txtarea.insert(END,f"\n Headphone\t\t{self.headphone.get()}\t\t{self.c_hs_p}")

                if self.speaker.get()!=0:
                    self.txtarea.insert(END,f"\n Speaker\t\t{self.speaker.get()}\t\t{self.c_hg_p}")
                
                if self.mousepad.get()!=0:
                    self.txtarea.insert(END,f"\n Mousepad\t\t{self.mousepad.get()}\t\t{self.c_bl_p}")
            
                #========Games==========
                if self.pes.get()!=0:
                    self.txtarea.insert(END,f"\n PES\t\t{self.pes.get()}\t\t{self.g_r_p}")

                if self.gow.get()!=0:
                    self.txtarea.insert(END,f"\n God Of War\t\t{self.gow.get()}\t\t{self.g_f_p}")

                if self.rl.get()!=0:
                    self.txtarea.insert(END,f"\n Rocket League\t\t{self.rl.get()}\t\t{self.g_d_p}")
                
                if self.cod.get()!=0:
                    self.txtarea.insert(END,f"\n Call Of Duty\t\t{self.cod.get()}\t\t{self.g_w_p}")

                if self.gta.get()!=0:
                    self.txtarea.insert(END,f"\n GTA V\t\t{self.gta.get()}\t\t{self.g_s_p}")
                
                if self.pubg.get()!=0:
                    self.txtarea.insert(END,f"\n PUBG\t\t{self.pubg.get()}\t\t{self.g_t_p}")
            
                #========Food & Drinks==========
                if self.momo.get()!=0:
                    self.txtarea.insert(END,f"\n MOMO\t\t{self.momo.get()}\t\t{self.d_m_p}")

                if self.chat.get()!=0:
                    self.txtarea.insert(END,f"\n Chatpate\t\t{self.chat.get()}\t\t{self.d_c_p}")

                if self.chow.get()!=0:
                    self.txtarea.insert(END,f"\n Chowmin\t\t{self.chow.get()}\t\t{self.d_f_p}")
                
                if self.coke.get()!=0:
                    self.txtarea.insert(END,f"\n Coca Cola\t\t{self.coke.get()}\t\t{self.d_t_p}")

                if self.fanta.get()!=0:
                    self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_l_p}")
                
                if self.sprite.get()!=0:
                    self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
                
                self.txtarea.insert(END,f"\n ------------------------------------")
                if self.hardware_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Hardware Tax\t\t{self.hardware_tax.get()}")
                if self.game_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Games Tax\t\t{self.game_tax.get()}")
                if self.drink_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Food&Drink Tax\t\t{self.drink_tax.get()}")
                
                self.txtarea.insert(END,f"\n Total Bill : \t\t Rs. {self.Total_bill}")
                self.txtarea.insert(END,f"\n ------------------------------------")
                self.save_bill()

        def save_bill(self):
            op=messagebox.askyesno("Saving Bill.....","Do You Want Save your Bill")

            if op>0:
                self.bill_data=self.txtarea.get('1.0',END)
                file=open("Bills/"+str(self.bill_no.get())+".txt","w")
                file.write(self.bill_data)
                file.close()
                messagebox.showinfo("Saving.....",f"{self.c_name.get()} Your Bill No : {self.bill_no.get()}  Successfully Saved please see the Bills folder on bill directory to see your Bills")
            else:
                return	

        def find_bill(self):
            valid="no"
            for i in os.listdir("Bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    file=open(f"Bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in file:
                        self.txtarea.insert(END,d)
                    file.close()
                    valid="yes"
            if valid=="no":
                messagebox.showerror("Error","Invalid Bill Number ..Please Enter Valid Bill Number")
        
        def clear_data(self):
            op=messagebox.askyesno("Clearing...","Do You Really Want to Clear All data")
            if op>0:
            
                #================ Hardware Items ==========================

                self.monitor.set(0)
                self.mouse.set(0)
                self.keyboard.set(0)
                self.headphone.set(0)
                self.speaker.set(0)
                self.mousepad.set(0)

                #================ Games Section ==========================
                
                self.pes.set(0)
                self.gow.set(0)
                self.rl.set(0)
                self.cod.set(0)
                self.gta.set(0)
                self.pubg.set(0)

                #================ Cold Drinks ==========================

                self.momo.set(0)
                self.coke.set(0)
                self.chow.set(0)
                self.coke.set(0)
                self.fanta.set(0)
                self.sprite.set(0)

                #================ Total Price and TAX==========================

                self.hardware_p.set("")
                self.games_p.set("")
                self.drinks_p.set("")

                self.hardware_tax.set("")
                self.game_tax.set("")
                self.drink_tax.set("")

                #================ Detail of Customer ==================================

                self.c_name.set("")
                self.c_phone.set("")

                self.bill_no.set("")
                x=random.randint(1000,9999)
                
                self.bill_no.set(str(x)) 

                self.search_bill.set("")
                self.welcome_bill()

        def Exit_app(self):
            op=messagebox.askyesno("Exit","Do You Really Want to Exit")
            if op>0:
                self.root.destroy()
                mainpage()

    root=Tk()
    obj = Bill(root)
    root.mainloop()	

    
'''======================================================================== After Mainscreen =====================================================================================''' 

def mainpage():
    global screenmain
    screenmain = Tk()
    screenmain.title('WELCOME')
    #width, height = screenmain.winfo_screenwidth(), screenmain.winfo_screenheight()
    screenmain.state('zoomed')
    #screenmain.geometry('%dx%d+0+0'% (width,height))
    screenmain.config(bg = 'indigo')

    pcbutton = Button(screenmain, text="PC", height = '2', width = '30', command = pcpage)
    pcbutton.pack(pady = 10)
    console = Button(screenmain, text="Console", height = '2', width = '30', command = cpage)
    console.pack(pady = 10)
    storebtn = Button(screenmain, text = 'Store', height = '2', width = '30', command = store)
    storebtn.pack(pady = 10)



main_screen()





