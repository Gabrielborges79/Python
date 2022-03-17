import webbrowser
from tkinter import *

raiz = Tk ( )

raiz.title ('Abrir Navegador')
raiz.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(raiz, text='Abrir o Google', command=google).pack(pady=20)

raiz.mainloop()
