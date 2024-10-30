from tkinter import *

text_at_start = ""


def check_end():
    text_at_end = text_area.get(1.0, "end-1c")
    if text_at_start == text_at_end:
        text_area.delete(1.0, "END")
        text_area.insert("END", "Start typing")


def check_start():
    global text_at_start
    text_at_start = text_area.get(1.0, "end-1c")
    window.after(5000, check_end)


window = Tk()
window.title("Most dangerous writing app")
window.config(width=600, height=600)

text_area = Text()
text_area.insert('0.0', chars="Start to type")
text_area.config(font=("Arial", 12, "normal"))
text_area.pack()

on = True
while on:
    check_start()
