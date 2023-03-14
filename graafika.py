﻿from tkinter import*
k=0
def klikker():
    global k
    k+=1
    nupp.configure(text=k)
    if k%2==0:
        raam.itemconfig(pildid,image=pilt1)
    else:
        raam.itemconfig(pildid,image=pilt2)


def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)
tekst="Aken"
aken=Tk()
aken.geometry("500x700")
aken.title(tekst)
aken.iconbitmap("League-of-Legends.ico")

pealkiri=Label(aken,
              text="Tkinteri põhielemendid",
              bg="gold",
              fg="#2f8245",
              font="Algerian 20",
              height=3,
              width=25)
nupp=Button(aken,
            text="valjuta mind",
            bg="Blue",
            fg="#2f8245",
            font="Algerian 20",
            activebackground="Red",
            activeforeground="Green",
            height=3,
            width=20,
            command=klikker)
raam=Canvas(aken,
            width=260,
            height=260,
            bg="black")
pilt1=PhotoImage(file="Minecraft-256.png")
pilt2=PhotoImage(file="Sims-3-256.png")
pildid=raam.create_image(2,2,image=pilt1,anchor=NW)
tekst_kast=Entry(aken,
                 fg="Lightblue",
                 bg="Grey",
                 font="Algerian 20",
                 width=20,
                 justify=CENTER)

tekst_kast.bind("<Return>",text_to_lbl)#Enter

pealkiri.pack()
tekst_kast.pack()#side=LEFT,RIGHT
nupp.pack()
raam.pack()
aken.mainloop()

