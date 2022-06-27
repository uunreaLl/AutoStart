# coding=utf-8
import tkinter.simpledialog
from tkinter import *
from tkinter import messagebox as mb
import tkinter.font
import os
from tkinter import filedialog

print((os.path.exists(r"C:\Users\pavlo\OneDrive\Рабочий стол\Anime Gang"),
       os.path.isfile(r"C:\Users\pavlo\OneDrive\Рабочий стол\Anime Gang")))

file = open(os.path.dirname(os.path.basename(__file__))+"autostartFile.txt", "r", encoding="utf-8")
if os.path.getsize(os.path.dirname(os.path.basename(__file__))+"autostartFile.txt") > 5:
    for i in file:
        i = i[:-1]
        if not os.path.exists(i):
            pass
        else:
            os.startfile(i)
else:
    pass
file.close()

# Main window_Setting
window = Tk()
window.title("Main menu")

# Customization
window.geometry("850x500+{}+{}".format(window.winfo_screenwidth()//2-425, window.winfo_screenheight()//2-275))
window.config(bg="black")

# Window_Size
window_width = window.winfo_screenmmwidth()
window_height = window.winfo_screenmmheight()

# Menu
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)


# Some_classes
class Message:
    def __init__(self):
        self.message = "It isn`t file, it is directory. Try again"


class Font:
    def __init__(self):
        self.font = tkinter.font.Font(family="Times", size=14)


# Testing
def is_link(link):
    print(link)
    if os.path.exists(link):
        if not os.path.isfile(link):
            mb.showerror(title="Incorrect link", message=Message().message)
            text = tkinter.simpledialog.askstring(title="INPUT", prompt="Paste your own link to the file")
            return is_link(text)
        else:
            # coding=utf-8
            print("!!!!!!!!", link)
            return link
    else:
        mb.showerror(title="ERROR", message="File does`t exist")
        text = tkinter.simpledialog.askstring(title="INPUT", prompt="Paste your own link to the file")
        return is_link(text)


# command
def opening(text):
    file = open(os.path.dirname(os.path.basename(__file__))+"autostartFile.txt", "r+")
    file.readlines()
    file.write(text+"\n")
    file.close()


def openfile():
    file_name = filedialog.askopenfile()
    is_link(file_name.name)

    # label/text
    Label(text=file_name.name, fg="#51e33d", bg=window["bg"], font=Font().font).grid(sticky=W)

    # opening
    opening(file_name.name)


def pastefile():
    link = tkinter.simpledialog.askstring(title="Link", prompt="Paste your own link to the file")
    v_text = is_link(link)
    print(v_text)
    # opening
    opening(v_text)

    # label/text
    Label(text=v_text, fg="#51e33d", bg=window["bg"], font=Font().font).grid(sticky=W)


# Menu_buttons
mainmenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Add...", command=openfile)
filemenu.add_command(label="Paste...", command=pastefile)


# output
window_text = Label(text="To add new apps for autostart u need click on ,,File,, --> ,,Add...,,", bg=window["bg"],
                    fg="#51e33d", font=tkinter.font.Font(family="Times", size=14))
window_text.grid(sticky=W)
Label(text="-"*100, bg=window["bg"], fg="#51e33d").grid(sticky=W)
window.mainloop()
