import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


window = Tk()

label = Label()

def openPlot(choice):
    
    if choice == 1:
        RawTempPlot()
    elif choice == 2:
        RawRainPlot()
    elif choice == 3:
        RawIMPlot()
    elif choice == 4:
        messagebox.showinfo(title="Sorry", message = "Coming Soon!")
    elif choice == 5:
        DiffHapPlot()
    elif choice == 6:
        DiffTempPlot()
    elif choice == 7:
        DiffRainPlot()
    elif choice == 8:
        DiffIMPlot()
    elif choice == 9:
        messagebox.showinfo(title="Sorry", message = "Coming Soon!")
    elif choice == 10:
        DiffHapPlot()
    elif choice == 11:
        TEMP_HAP()
    elif choice == 12:
        RAIN_HAP()
    elif choice == 13:
        TEMP_IM()
    elif choice == 14:
        RAIN_IM()
    elif choice == 15:
        TEMP_RAIN()
    else:
        messagebox.showerror(title="Error", message = "No Plot Selected!")
    return

#def onClose():
#    global img
#    img.pack_forget()

def RawTempPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Raw_Temperature/Temp_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack(side=RIGHT)
    
    #Slider
    global Slider_TempPlot
    Slider_TempPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Temp,
                            length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return 

def switch_Temp(year):

    path2 = "/Users/sally/Desktop/Raw_Temperature/Temp_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack(side=RIGHT)
    
def RawRainPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Raw_Rain/Rain_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack(side=RIGHT)

    #Slider
    global Slider_RainPlot
    Slider_RainPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Rain,
                            length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Rain(year):
    
    path2 = "/Users/sally/Desktop/Raw_Rain/Rain_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack(side=RIGHT)


def RawIMPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Raw_IM/IM_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_IMPlot
    Slider_IMPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_IM,
                        length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_IM(year):

    path2 = "/Users/sally/Desktop/Raw_IM/IM_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def RawHapPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Raw_IM/IM_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_HapPlot
    Slider_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Hap,
                        length=200, from_=2006, to=2017, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Hap(year):

    path2 = "/Users/sally/Desktop/Raw_Happy/Happy_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def DiffTempPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Norm_Temp/Norm_Temp_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_Diff_TempPlot
    Slider_Diff_TempPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Temp,
                            length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Diff_Temp(year):

    path2 = "/Users/sally/Desktop/Norm_Temp/Norm_Temp_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()
    
def DiffRainPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Norm_Rain/Norm_Rain_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()

    #Slider
    global Slider_Diff_RainPlot
    Slider_Diff_RainPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Rain,
                            length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Diff_Rain(year):
    path2 = "/Users/sally/Desktop/Norm_Rain/Norm_Rain_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def DiffIMPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Norm_IM/Norm_IM_plot_2000.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_Diff_IMPlot
    Slider_Diff_IMPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_IM,
                        length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Diff_IM(year):

    path2 = "/Users/sally/Desktop/Norm_IM/Norm_IM_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def DiffHapPlot():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Norm_Happy/Norm_Happy_plot_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_Diff_HapPlot
    Slider_Diff_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Hap,
                        length=200, from_=2006, to=2017, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_Diff_Hap(year):

    path2 = "/Users/sally/Desktop/Norm_Happy/Norm_Happy_plot_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack(side=RIGHT)

def TEMP_HAP():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Temp_Hap/Temp_Hap_norm_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_TEMP_HAP_HapPlot
    Slider_TEMP_HAP_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Hap,
                        length=200, from_=2006, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_TEMP_HAP(year):

    path2 = "/Users/sally/Desktop/Temp_Hap/Temp_Hap_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def TEMP_IM():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Temp_IM/Temp_IM_norm_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_TEMP_IM_HapPlot
    Slider_TEMP_IM_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Hap,
                        length=200, from_=2006, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_TEMP_IM(year):

    path2 = "/Users/sally/Desktop/Temp_IM/Temp_IM_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def RAIN_HAP():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Rain_Hap/Rain_Hap_norm_2007.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_Rain_Hap_HapPlot
    Slider_Rain_Hap_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_Diff_Hap,
                        length=200, from_=2007, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_RAIN_HAP(year):

    path2 = "/Users/sally/Desktop/Rain_Hap/Rain_Hap_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def Temp_IM():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Temp_IM/Temp_IM_norm_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_Temp_IM_HapPlot
    Slider_TEMP_IM_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_TEMP_IM,
                        length=200, from_=2006, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_TEMP_IM(year):

    path2 = "/Users/sally/Desktop/Temp_IM/Temp_IM_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def RAIN_IM():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Temp_IM/Temp_IM_norm_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_RAIN_IM_HapPlot
    Slider_RAIN_IM_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_RAIN_IM,
                        length=200, from_=2006, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_RAIN_IM(year):

    path2 = "/Users/sally/Desktop/Temp_IM/Temp_IM_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()

def TEMP_RAIN():
    global label
    plot_window = Tk()
    plot_window.geometry('500x100')
    plot_window.title("Slider")

    year= ''
    path = '/Users/sally/Desktop/Temp_Rain/Temp_Rain_norm_2006.png'
    img = PhotoImage(file = path)
    label= Label(image=img)
    label.configure(image=img)
    label.image = img
    label.pack()
    
    #Slider
    global Slider_TEMP_RAIN_HapPlot
    Slider_TEMP_RAIN_HapPlot = Scale(plot_window, orient=HORIZONTAL, variable=year, command=switch_TEMP_RAIN,
                        length=200, from_=2000, to=2015, tickinterval = 5).grid(row = 2, column = 1)
    return

def switch_TEMP_RAIN(year):

    path2 = "/Users/sally/Desktop/Temp_Rain/Temp_Rain_norm_" + str(year) + ".png"
    img_New = PhotoImage(file=path2)
    label.configure(image=img_New)
    label.image = img_New
    label.pack()


def mNew():
    mLabel_New = Label(window, text = "New").pack()
    return

def mQuit():
    mExit = messagebox.askyesno(title = "Quit", message = "Are You Sure You Want Quit?")
    if mExit > 0:
        window.distroy()
        return

def mAbout():
    messagebox.showinfo(title="About", message = "This is my About Box")
    return

def main():
    window.geometry('550x600')
    window.title("Hophacks 2019S")

    # Menu Construction
    menubar = Menu(window)

    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label="New", command = mNew)
    filemenu.add_command(label="Quit", command = mQuit)
    menubar.add_cascade(label="Menu", menu=filemenu)

    aboutmenu = Menu(menubar, tearoff = 0)
    aboutmenu.add_command(label="About", command = mAbout)
    menubar.add_cascade(label="About", menu=aboutmenu)

    window.config(menu=menubar)

    #Welcome Statement
    Label_1 = Label(window, text="Welcome to Correpleth").pack()


    #Initialize int Varible Choice
    choice = IntVar()
    
    #Raw data Visualization
    Choice_1 = Radiobutton(window, text="Temperature", value=1, variable=choice, anchor='w', justify=LEFT).pack()
    Choice_2 = Radiobutton(window, text="Rainfall", value=2, variable=choice, anchor='w', justify=LEFT).pack()
    Choice_3 = Radiobutton(window, text="Infant Mortality Rate", value=3, variable =choice, anchor='w', justify=LEFT).pack()
    Choice_4 = Radiobutton(window, text="Gini Index", value=4, variable=choice, anchor='w', justify=LEFT).pack()
    Choice_5 = Radiobutton(window, text="Happiness Index", value=6, variable =choice, anchor='w', justify=LEFT).pack()
    #Choice_6 = Radiobutton(window, text="Proverty Head Count", value=5, variable=choice, anchor='w', justify=LEFT).pack()

    checkRaw = IntVar()
    checkRaw.set(0)

    Label_blank = Label(window, text=" ").pack()

    checkbox_Raw = Checkbutton(window, text="Check for the normalized plot", variable = checkRaw).pack()

    Label_blank = Label(window, text=" ").pack()
        
    if checkRaw.get() == 1:
        value = value + 5

    #Correlation Visualization
    #Choice 1 List Box
    Choice_1 = Radiobutton(window, text="Temperature vs. Happiness Index", value=11, variable=choice,anchor='w',justify=LEFT).pack()
    Choice_2 = Radiobutton(window, text="Rainfall vs. Happiness Index", value=12, variable=choice,anchor='w',justify=LEFT).pack()
    Choice_3 = Radiobutton(window, text="Temperature vs. Infant Mortality Rate", value=13, variable =choice,anchor='w',justify=LEFT).pack()
    Choice_4 = Radiobutton(window, text="Rainfall vs. Infant Mortality Rate", value=14, variable=choice,anchor='w',justify=LEFT).pack()
    Choice_5 = Radiobutton(window, text="Rainfall vs. Temperature", value=15, variable =choice,anchor='w',justify=LEFT).pack()
        
    #Ok Button
    Button_OK = Button(window, text = 'OK', command = lambda: openPlot(choice.get())).pack()



    window.mainloop()

if __name__ == "__main__":
    main()

