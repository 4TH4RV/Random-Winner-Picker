import time
from tkinter import *
from tkinter import filedialog
from tkinter import font
import random


def createwindow():
    # Globals

    # GlobalVars openWindow
    global OpenFileButton
    global GenerateButton
    global OutputLabel

    global root

    root = Tk()
    root.title("Random winner generator")
    root.geometry("250x350")
    root.configure(bg="black")

    OpenFileButton = Button(root, text="Open File", command=choosefile, width=30, height=3, bg="grey", fg="white")
    GenerateButton = Button(root, text="GenerateRandom", command=generaterandom, width=20, height=3, bg="grey", fg="white")
    OutputLabel = Label(root, text="Open File", width=30, height=3, bg="grey", fg="white")

    OpenFileButton.place(rely=0.5, relx=0.5, anchor="center")

    mainloop()


def choosefile():
    f = filedialog.askopenfilename()
    if f is None:
        return
    global Entries
    File = open(f, mode="r")
    Entries = File.readlines()
    File.close()
    mainpage()


def mainpage():
    OpenFileButton.place_forget()
    GenerateButton.place(rely=0.5, relx=0.5, anchor="center")


def generaterandom():
    winner = Entries[random.randint(0, len(Entries) - 1)]
    initfont = font.Font(size=10)
    OutputLabel.config(font=initfont)
    GenerateButton.place_forget()
    GenerateButton.config(text="Retry")
    GenerateButton.pack()
    OutputLabel.place(rely=0.5, relx=0.5, anchor="center")
    OutputLabel.config(text="Winner is.")
    root.update()
    time.sleep(1)
    OutputLabel.config(text="Winner is..")
    root.update()
    time.sleep(1)
    OutputLabel.config(text="Winner is...")
    root.update()
    time.sleep(1)
    finalfont = font.Font(size=30)
    OutputLabel.config(text=winner, font=finalfont)


createwindow()
