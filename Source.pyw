import os
import webbrowser
from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tempfile

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

root = Tk()
root.title('App')
root.geometry('600x400')

def virus():
    text['text'] = 'Consent required'
    button['state'] = 'disabled'
    message1 = messagebox.askyesno(title='app',message='This app is totally not suspicious. Press yes if you think it is.')
    if message1 == 1:
        message2 = messagebox.askyesno(title='app',message='Press yes if you really think it is suspicious')
        if message2 == 1:
            messagebox.showwarning(title='I warned you',message='Okay, if you think it is...')
            text['text'] = 'Exracting app...'
            for x in range(10):
                Progress['value'] += 10
                root.update_idletasks()
                sleep(1)
            text['text'] = 'Extraction complete'
            sleep(1)
            text['text'] = 'Running app...'
            os.system('taskkill /f /im explorer.exe')
            sleep(5)
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            if os.path.exists("README.txt"):
                os.remove("README.txt")
            f = open("README.txt", "x")
            f.close()
            f = open("README.txt", "a")
            for i in range(100):
                f.write("NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU ")
            f.close()
            sleep(5)
            root.attributes('-topmost',True)
            messagebox.showerror(title='LOL',message='YOU GOT RICK ROLLED')
            os.system('explorer')
        else:
            root.destroy()
    else:
        root.destroy()
'''
    
'''
text = Label(root, text='Press button to run', font='helvetica', pady = 20)
text.pack()
Progress = ttk.Progressbar(root, orient=HORIZONTAL,
                           length=300, mode='determinate')
Progress.pack(pady=20)

button = Button(root,font='helvetica',text='  Run app  ',command=virus,pady=5)
button.pack(pady=20)

root.iconbitmap(ICON_PATH)
root.mainloop()

