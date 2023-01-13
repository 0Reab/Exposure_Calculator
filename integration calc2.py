from tkinter import *

root = Tk()

sec = Entry(root, width=10, borderwidth=5)
sec.pack()

sub_count = Entry(root, width=10, borderwidth=5)
sub_count.pack()


def calc():
    total_secs = int(sec.get()) * int(sub_count.get())
    int_time = total_secs / 60

    if int_time <= 1:
        result = Label(root, text=str(int(int_time)) + " minute")
        result.pack()

    elif int_time < 60:
        result = Label(root, text=str(int(int_time)) + " minutes")
        result.pack()

    if int_time > 60:
        result2 = int_time / 60
        resultpr = Label(root, text="0" + str(int(result2)) + ":" + str(int((result2 - int(result2)) * 60)) + " h")
        resultpr.pack()


myButton = Button(root, text="calculate", command=calc)
myButton.pack()

root.mainloop()

# total_secs = sub_len * sub_coun
# int_time = total_secs / 60
# print(int_time, "minutes")
# print(int_time / 60, "hours")
