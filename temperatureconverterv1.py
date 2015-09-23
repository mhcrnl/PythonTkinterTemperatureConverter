from Tkinter import *
"""
http://www.unco.edu/nhs/mathsci/ClassSites/hoppercourse/CS102/S04/week7.html
"""

def convert():
    temperature=float(temp.get())
    whichcvt=tkind.get()
    if whichcvt==1:
        mytemp = (temperature-32)*5/9
    else:
        mytemp= temperature*1.8+32
    result.config(text=str(mytemp))

win=Tk()
win.title("Convertor Temperatura")
explain = Label(win, text="Number Conversion Program")
explain.pack()
instruct = Label(win, text="Type in a temperature in the box below")
instruct.pack()
mytemp = str()
temp = Entry(win, textvariable=mytemp)
temp.pack()
tkind = IntVar()
FtoC = Radiobutton(win, text="Fahrenheit to Celsius", variable=tkind, value=1,
                   indicatoron=0, bg="yellow", fg="blue")
CtoF = Radiobutton(win, text="Celsius to Fahrenheit", variable=tkind, value=2,
                   indicatoron=0, bg="yellow", fg="blue")
FtoC.pack()
CtoF.pack()
FtoC.select()
result = Label(win, text=" ")
result.pack()
choosecvt= Button(win, text='Convert temperature', command=convert, bg='green')
choosecvt.pack()
win.mainloop()
            
    
