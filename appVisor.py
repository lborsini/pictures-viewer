from tkinter import *
from PIL import Image, ImageTk

root = Tk() 
root.title('Visor de Imagenes')

i1 = ImageTk.PhotoImage(Image.open('Img/pexels-alexander-grey-1148998.jpg'))
i2 = ImageTk.PhotoImage(Image.open('Img/pexels-benjamin-suter-3617500.jpg'))
i3 = ImageTk.PhotoImage(Image.open('Img/pexels-eberhard-grossgasteiger-1366919.jpg'))
i4 = ImageTk.PhotoImage(Image.open('Img/pexels-eberhard-grossgasteiger-443446.jpg'))
i5 = ImageTk.PhotoImage(Image.open('Img/pexels-kehn-hermano-3849167.jpg'))
i6 = ImageTk.PhotoImage(Image.open('Img/pexels-mo-eid-9454915.jpg'))
i7 = ImageTk.PhotoImage(Image.open('Img/pexels-pixabay-268533.jpg'))
i8 = ImageTk.PhotoImage(Image.open('Img/pexels-tiff-ng-3700245.jpg'))

lst=[i1, i2, i3, i4, i5, i6, i7, i8]

l = Label(root, image = i1)
l.grid(row = 0, column = 0, columnspan = 3 )

def adelante(imgNum):
    global l
    global btnAtras
    global btnAdelante

    l.grid_forget()
    l = Label(root, image=lst[imgNum])
    btnAtras = Button(root, text= ' <- ', command= lambda: atras(imgNum - 1 ))
    btnAdelante = Button(root, text = ' -> ', command= lambda: adelante(imgNum + 1))
    
    if imgNum == (len(lst) - 1):
        btnAdelante = Button(root, text= 'N/A', state=DISABLED)

    l.grid(row = 0, column = 0, columnspan = 3 )
    btnAtras.grid(row = 1, column = 0)
    btnAdelante.grid(row = 1, column = 2)

def atras(imgNum):
    global l
    global btnAtras
    global btnAdelante

    l.grid_forget()
    l = Label(root, image=lst[imgNum])
    btnAtras = Button(root, text= ' <- ', command= lambda: atras(imgNum - 1 ))
    btnAdelante = Button(root, text = ' -> ', command= lambda: adelante(imgNum + 1))
    
    if imgNum == 0:
        btnAtras = Button(root, text= 'N/A', state=DISABLED)

    l.grid(row = 0, column = 0, columnspan = 3 )
    btnAtras.grid(row = 1, column = 0)
    btnAdelante.grid(row = 1, column = 2)

btnAtras = Button(root, text= 'N/A', state=DISABLED)
btnAdelante = Button(root, text = ' -> ', command= lambda: adelante(1))

btnAtras.grid(row = 1, column = 0)
btnAdelante.grid(row = 1, column = 2)


root.mainloop()