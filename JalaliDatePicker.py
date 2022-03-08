###This code was created by Atieh Khodadadi on 3/7/2022.
####Email: ati.khodadadi@ut.ac.ir
from tkinter import *
from subpages.Jalalicalendarwidget import JCalendar

def menueSelectDate():

    global reg_screen
    reg_screen = Tk()
    reg_screen.title(" انتخاب تاریخ فارسی ")
    reg_screen.geometry("450x280")
    def validate():
        year, month, day= calendar.selection
        if year is not None:
            SelectedDate=str(day)+'/'+str(month)+'/'+str(year)

            label.configure(text='تاریخ انتخابی:   ' + SelectedDate)
            B1.place(x=140, y=290)
            B1.config(command=lambda: submit(SelectedDate,dateinf))


    calendar = JCalendar(reg_screen, selectbackground='red', selectforeground='white')
    calendar.grid(column=1, row=1)
    Button(reg_screen, text='انتخاب', command=validate).grid(column=1, row=2)
    label = Label(reg_screen)
    label.grid(column=1, row=3)


    B1 = Button(reg_screen, text='تایید و ادامه', background='purple', fg='white')
    B1.place()

    reg_screen.mainloop()

menueSelectDate()
