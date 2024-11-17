# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:34:13 2024

@author: user
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import filedialog
import Code_For_AES
import cv2
import os
from tkinter import messagebox

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIA6GBME6J32QWPHHVZ'
SECRET_KEY = '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'


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Code_For_AES.Encryptor(key)


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
        w2 = tk.Label(self, text="Advanced Privacy and Confidentiality Image Encryption", bg="white"  ,fg="black"  ,width=45  ,height=1,font=('times', 30, 'italic bold underline'))
        w2.place(x=150,y=10) 
        
        
        def gotosecond():
            print("move to next page")
            controller.show_frame(SecondPage)
        def gotothird():
            print("move to next page")
            controller.show_frame(ThirdPage)
        
        k=tk.Button(self,text="Patient Login", command=gotosecond, bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 20, 'italic bold underline'))
        k.place(x=200,y=200)
        
        t=tk.Button(self,text="Doctor Login", command=gotothird, bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 20, 'italic bold underline'))
        t.place(x=800,y=400)
        
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
         
        
        self.configure(bg='white')
        #Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))
        #Label.place(x=40, y=150)
        w2 = tk.Label(self, text="Patient Page", bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 30, 'italic bold underline'))
        w2.place(x=300,y=10)
        
        L1 = tk.Label(self, text="Patient Name", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=500, y=200)
        T1 = tk.Entry(self, width = 30, bd = 5)
        T1.place(x=700, y=200)
        
        L2 = tk.Label(self, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=500, y=300)
        T2 = tk.Entry(self, width = 30, show='*', bd = 5)
        T2.place(x=700, y=300)
        
        def verify():
            try:
                with open("sendercredential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        print(u.strip())
                        print(p.strip())
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            i = 1
                            break                        
                    if i == 1:
                        controller.show_frame(FourthPage)
                    else:
                        messagebox.showinfo("Error", "Patient Not Found!!")
                        
                    
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
        
        B1 = tk.Button(self, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=700, y=400)
        
        def gotofirst():
            print("Go back to Home page")
            controller.show_frame(FirstPage)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="white")
            window.title("Patient Register")
            l1 = tk.Label(window, text="Patient Name:", font=("Arial",15), bg="white")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="white")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="white")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("sendercredential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=1200, y=100)
        
        B3 = tk.Button(self, text="Back", bg = "dark orange", font=("Arial",15), command=gotofirst)
        B3.place(x=20, y=100)

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
         
        
        self.configure(bg='white')
        #Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))
        #Label.place(x=40, y=150)
        w2 = tk.Label(self, text="Doctor Page", bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 30, 'italic bold underline'))
        w2.place(x=300,y=10)
        
        L1 = tk.Label(self, text="Doctor Name", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=500, y=200)
        T1 = tk.Entry(self, width = 30, bd = 5)
        T1.place(x=700, y=200)
        
        L2 = tk.Label(self, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=500, y=300)
        T2 = tk.Entry(self, width = 30, show='*', bd = 5)
        T2.place(x=700, y=300)
        
        def verify():
            try:
                with open("receivercredential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        print(u.strip())
                        print(p.strip())
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            i = 1
                            break                        
                    if i == 1:
                        controller.show_frame(FifthPage)
                    else:
                        messagebox.showinfo("Error", "Doctor Not Found!!")
                    '''
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(FifthPage)
                            i = 1
                            break
                        else:
                            messagebox.showinfo("Error", "Please provide correct username and password!!")
                    '''
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
        
        B1 = tk.Button(self, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=700, y=400)
        
        def gotofirst():
            print("Go back to Home page")
            controller.show_frame(FirstPage)
        
        def register():
            window = tk.Tk()
            window.resizable(0,0)
            window.configure(bg="white")
            window.title("Doctor Register")
            l1 = tk.Label(window, text="Doctor Name:", font=("Arial",15), bg="white")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x = 200, y=10)
            
            l2 = tk.Label(window, text="Password:", font=("Arial",15), bg="white")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x = 200, y=60)
            
            l3 = tk.Label(window, text="Confirm Password:", font=("Arial",15), bg="white")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x = 200, y=110)
            
            def check():
                if t1.get()!="" or t2.get()!="" or t3.get()!="":
                    if t2.get()==t3.get():
                        with open("receivercredential.txt", "a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            b1 = tk.Button(window, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)
            
            window.geometry("470x220")
            window.mainloop()
            
        B2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15), command=register)
        B2.place(x=1200, y=100)
         
        B3 = tk.Button(self, text="Back", bg = "dark orange", font=("Arial",15), command=gotofirst)
        B3.place(x=20, y=100)
        
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
         
        
        self.configure(bg='white')
        
        self.t2 = tk.Entry(self, width=30, bd=5)
        self.t2.place(x = 700, y=200)
        #Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))
        #Label.place(x=40, y=150)
        w2 = tk.Label(self, text="Encryption", bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 30, 'italic bold underline'))
        w2.place(x=300,y=10)
        
        w1 = tk.Label(self, text="Enter the Patient Name", bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 15))
        w1.place(x=250,y=150)
        
        self.T1 = tk.Entry(self, width = 30, bd = 5)
        self.T1.place(x=700, y=150)
        
        k=tk.Button(self,text="Browse for the Image to Encrypt", command=self.showImgg, bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 15))
        k.place(x=250,y=200)
        
        w2 = tk.Label(self, text="Enter the Secret Key", bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 15))
        w2.place(x=250,y=300)
        
        self.T3 = tk.Entry(self, width = 30, bd = 5)
        self.T3.place(x=700, y=300)
        
        t=tk.Button(self,text="Encrypt Image", command=self.Encrypt, bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 20, 'italic bold underline'))
        t.place(x=900,y=400)
        
        Button = tk.Button(self, text="Home",bg = "dark orange", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=1100, y=50)
        
        Button = tk.Button(self, text="Back",bg = "dark orange", font=("Arial", 15), command=self.destroy)
        Button.place(x=50, y=50)
        
        
             
        
        
    
    def showImgg(self):
            #self.load = askopenfilename(filetypes=[("Image File",'.jpeg .jpg .png .HEIC')])
            self.file_path = filedialog.askopenfilename()
            self.filename = os.path.basename(self.file_path)
            self.t2.delete(0, tk.END)  # Clear the entry field
            self.t2.insert(0, self.filename)  # Insert the selected file path        
                
            
            
            im = Image.open(self.file_path)
            
            im = im.resize((300, 150))
        
            render = ImageTk.PhotoImage(im)
    
            # labels can be text or images
            img = tk.Label(self, image=render,width=300,height=150)
            img.image = render
            img.place(x=950, y=200)       
        
    
        
    def Encrypt(self):
        if self.file_path:
            self.file_name = self.file_path.split("/")[-1]
        print(self.file_name)
        
        print(self.T1.get())
        
        buck =  self.T1.get()+"imgsec"
        
        def append_to_file(filename, values):
            with open(filename, 'a') as file:
                file.write("{0}".format(values))
                file.write('\n')                
        
        
        enc.encrypt_file(self.file_name)
        
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        val = self.file_name.strip()+","+ self.T3.get().strip()
        print(val)
        append_to_file("authent.txt", val)
    
        try:
            s3.upload_file(self.file_name+'.enc', buck, self.file_name+'.enc')
            print("Upload encrypted Successful")
            s3.upload_file('authent.txt', buck, 'authent.txt')
            print("Upload Successful")
            file_path = 'authent.txt'

            # Check if the file exists before deleting
            if os.path.exists(file_path):
                # Delete the file
                os.remove(file_path)
            
            messagebox.showinfo("Secured Storage in Cloud", "Medical Image Encrypted Successfully!")
            
            return True
        
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
        
            
        
        
        
        
        
class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
         
        
        self.configure(bg='white')
        #Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "orange", font=("Arial Bold", 25))
        #Label.place(x=40, y=150)
        self.t2 = tk.Entry(self, width=30, bd=5)
        self.t2.place(x = 700, y=200)
        
        
        w2 = tk.Label(self, text="Decryption", bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 30, 'italic bold underline'))
        w2.place(x=300,y=10)  
        
        w1 = tk.Label(self, text="Enter the Patient Name", bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 15))
        w1.place(x=250,y=150)
        
        self.T1 = tk.Entry(self, width = 30, bd = 5)
        self.T1.place(x=700, y=150)
        
        k=tk.Button(self,text="Browse for the Image to Decrypt", command=self.showImgg, bg="white"  ,fg="black"  ,width=30  ,height=1,font=('times', 15))
        k.place(x=250,y=200)
        
        
        w2 = tk.Label(self, text="Enter the Secret Key", bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 15))
        w2.place(x=250,y=300)
        
        self.T3 = tk.Entry(self, width = 30, bd = 5)
        self.T3.place(x=700, y=300)
        
        t=tk.Button(self,text="Decrypt Image", command=self.Decrypt, bg="white"  ,fg="black"  ,width=20  ,height=1,font=('times', 20, 'italic bold underline'))
        t.place(x=900,y=450)
        
        Button = tk.Button(self, text="Home",bg = "dark orange", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=1100, y=50)
        
        Button = tk.Button(self, text="Back",bg = "dark orange", font=("Arial", 15), command=self.destroy)
        Button.place(x=50, y=50)
        
    def showImgg(self):
        self.file_path = filedialog.askopenfilename()
        self.filename = os.path.basename(self.file_path)
        self.t2.delete(0, tk.END)  # Clear the entry field
        self.t2.insert(0, self.filename)  # Insert the selected file path         
        
    def Decrypt(self):
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        
        print(self.T1.get())
        
        buck =  self.T1.get()+"imgsec"
        print(buck)
    
        s3.download_file(buck,self.filename,self.filename)
        #print('Downloaded Encrypted Image')
        
        s3.download_file(buck,'authent.txt','authent.txt')
        #print('Downloaded Data')
        
        print(self.T3.get())
        
        with open("authent.txt", "r") as f:
            info = f.readlines()
            i  = 0
            for e in info:
                fn, sk =e.split(",")
                #print(fn.strip())
                #print(sk.strip())
                if sk.strip() == self.T3.get():
                    i = 1
                    break                        
            if i == 1:
                enc.decrypt_file(self.filename)
                d = self.filename.split(".")
                img = d[0]+"."+d[1]
                #print(img)             
                     
                im = Image.open(img)
                     
                im = im.resize((300, 150))
                 
                render = ImageTk.PhotoImage(im)
             
                # labels can be text or images
                img = tk.Label(self, image=render,width=300,height=150)
                img.image = render
                img.place(x=950, y=250)
                
                file_path = 'authent.txt'
                
                '''

                # Check if the file exists before deleting
                if os.path.exists(file_path):
                    # Delete the file
                    os.remove(file_path)
                '''
                
                messagebox.showinfo("Downloaded from Cloud", "Medical Image Decrypted Successfully!")
            else:
                messagebox.showinfo("Error", "Secret Not matched!!!")       
        
        
        
             
         
        
      
        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 800)
        window.grid_columnconfigure(0, minsize = 1300)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage, FifthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title(" Application")
            
app = Application()
app.maxsize(1300,800)
app.mainloop()