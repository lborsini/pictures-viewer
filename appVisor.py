from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk() 
root.title('Photo Viewer')
root.configure(background='#212121')
root.geometry('760x750')
root.resizable(0,0)

frame = Frame(root, width=700, height=650)
frame.grid(row=0, column=0, columnspan=4, padx=30, pady=30)
frame.config(background='#212121')

# fisrt 4 img its a demostration
i1 = Image.open('Img/pexels-alexander-grey-1148998.jpg').resize((700, 600), Image.ANTIALIAS)
i2 = Image.open('Img/pexels-benjamin-suter-3617500.jpg').resize((700, 600), Image.ANTIALIAS)
i3 = Image.open('Img/pexels-eberhard-grossgasteiger-443446.jpg').resize((700, 600), Image.ANTIALIAS)
i4 = Image.open('Img/pexels-kehn-hermano-3849167.jpg').resize((700, 600), Image.ANTIALIAS)

lst=[i1, i2, i3, i4]
list = []

for i in lst:
    img = ImageTk.PhotoImage(i)
    list.append(img)

l = Label(frame, image = list[0])
l.grid(row = 0, column = 0, columnspan = 3, sticky='nswe')

def adelante(imgNum):
    global l
    global btnAtras
    global btnAdelante

    l.grid_forget()
    l = Label(frame, image=list[imgNum])
    btnAtras = Button(root, text= ' <- ', bd=5, fg='#222212', bg='#EEE', height=1, width=11, command= lambda: atras(imgNum - 1 ))
    btnAdelante = Button(root, text = ' -> ', bd=5, fg='#222212', bg='#EEE', height=1, width=11, command= lambda: adelante(imgNum + 1))
    
    if imgNum == (len(list) - 1):
        btnAdelante = Button(root, text= 'N/A', state=DISABLED)
        btnAtras.focus()

    l.grid(row = 0, column = 0, sticky='nswe')
    btnAtras.grid(row = 2, column = 0, padx=100, pady=20)  
    btnAdelante.grid(row = 2, column = 2, padx=100, pady=20)
    btnAdelante.focus()

def atras(imgNum):
    global l
    global btnAtras
    global btnAdelante

    l.grid_forget()
    l = Label(frame, image=list[imgNum])
    btnAtras = Button(root, text= ' <- ', bd=5, fg='#222212', bg='#EEE', height=1, width=11, command= lambda: atras(imgNum - 1 ))
    btnAdelante = Button(root, text = ' -> ', bd=5, fg='#222212', bg='#EEE', height=1, width=11, command= lambda: adelante(imgNum + 1))

    if imgNum == 0:
        btnAtras = Button(root, text= 'N/A', state=DISABLED)
        btnAdelante.focus()

    l.grid(row = 0, column = 0, sticky='nswe')
    btnAtras.grid(row = 2, column = 0, padx=100, pady=20)  
    btnAdelante.grid(row = 2, column = 2, padx=100, pady=20)
    btnAtras.focus()

btnAtras = Button(root, text= 'N/A', state=DISABLED, bd=5, fg='#222212', bg='#EEE', height=1, width=11)
btnAtras.grid(row = 2, column = 0, padx=100, pady=20)

btnAdelante = Button(root, text = ' -> ', command= lambda: adelante(1), bd=5, fg='#222212', bg='#EEE', height=1, width=11)
btnAdelante.grid(row = 2, column = 2, padx=100, pady=20)

btnAdelante.focus()

root.mainloop()