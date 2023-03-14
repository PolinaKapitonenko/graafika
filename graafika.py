from tkinter import*

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
            width=20)

pealkiri.pack()
nupp.pack()
aken.mainloop()

