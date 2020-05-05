from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *

fileSize=0
def strtDown():
    global fileSize
    try:
        url=uriField.get()
        print(url)
        dbtn.config(text='Download In progress....')
        dbtn.config(state=DISABLED)
        savepath=askdirectory()
        print(savepath)
        if savepath is None:
            return

        obj=YouTube(url)
        stream=obj.streams.first()
        stream.downlaod(savepath)
        print("Download Finished :)")
        dbtn.config(text='Download Finished')
        dbtn.config(text='Download')
        dbtn.config(state=NORMAL)
        showinfo("Download is Completed","Video downloaded successfuly")

    except Exception as e:
        print(e)
        print("There was an error !!!!")




gui=Tk()
gui.title("Youtube Videos in HD Downloader")

gui.geometry("800x900")
file=PhotoImage(file='icon1.png')
headingIcon=Label(gui,image=file)
headingIcon.pack(side=TOP)


uriField=Entry(gui,font=("veranda",20),justify=CENTER)

uriField.pack(side=TOP,fill=X,padx=10)
dbtn=Button(gui,text="Download",font=("veranda",18),command=lambda: strtDown())
dbtn.pack(side=TOP,pady=14)

gui.mainloop()


