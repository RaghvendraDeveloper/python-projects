from tkinter import *
windows=Tk()

windows.geometry("500x600")
windows.config(bg="white")
label1=Label(windows,text="Enter the link or text down:",font=("",22))
label1.pack()
entry1=Entry(windows,fg="lightgreen",bg="silver",
            font=("",50) ,width=600,)
entry1.pack()
#For secound line

label2=Label(windows,text="Enter the name you want to give:",font=("",22))
label2.pack()
entry2=Entry(windows,fg="lightgreen",bg="silver",
            font=("",50) ,width=600,)
entry2.pack()


def qrcodee():
    import  qrcode
    link_text=entry1.get()
    file_name = entry2.get()

    if   link_text !="" and file_name !="":
        image=qrcode.make(link_text)
        file_name="Qr_code_saved_images\\"+ file_name+".png"
        image.save( file_name)
        label3 = Message(windows, text="QrCode Seccesfully done:", font=("", 22),bg="yellow")
        label3.place(x=180,y=450)
    else:
        label3 = Message(windows, text="Fill out the form first", font=("", 22),bg="yellow")
        label3.place(x=180,y=450)

button=Button(windows,text="Submit",font=("",22) ,command=qrcodee)
button.pack()
windows.mainloop()

