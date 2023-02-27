#####################################
# Module Books
#####################################

from tkinter import *
import tkinter as tk
from tkinter import ttk

ventana = Tk()
ventana.title("Module1")
ventana.geometry("600x600")
# ventana['bg']= 'COLORCODE'

# Agregar el título centrado en la parte superior
module_name1 = Label(ventana, text="Books", font=("Arial", 20))
module_name1.pack(side="top", fill="both", pady=10)


# Crea boton Assign
boton1 = Label(ventana, text="Assign Book: ").place(x=30, y=70)
ingreso1 = Entry(ventana).place(x=120, y=70)


def box1():
    caja1 = ingreso1.get()
    print("Book Assigned: " + caja1)


boton_enter1 = Button(ventana, text="Enter", command=box1).place(x=250, y=65)

# Crea boton Return
boton2 = Label(ventana, text="Return Book: ").place(x=30, y=100)
ingreso2 = Entry(ventana, textvariable=input).place(x=120, y=100)


def box2():
    caja2 = ingreso2.get()
    print("Book Returned: " + caja2)


boton_enter2 = Button(ventana, text="Enter", command=box2).place(x=250, y=95)

# Crea boton Add
boton3 = Label(ventana, text="Add Book: ").place(x=30, y=130)
ingreso3 = Entry(ventana, textvariable=input).place(x=120, y=130)


def box3():
    caja3 = ingreso3.get()
    print("Book Added: " + caja3)


boton_enter3 = Button(ventana, text="Enter", command=box3).place(x=250, y=125)

# Crea boton Delete
boton4 = Label(ventana, text="Delete Book: ").place(x=30, y=160)
ingreso4 = Entry(ventana, textvariable=input).place(x=120, y=160)


def box4():
    caja4 = ingreso4.get()
    print("Book Added: " + caja4)


boton_enter4 = Button(ventana, text="Enter", command=box4).place(x=250, y=155)

""" Falta la funcion que el dato se agregue a la tabla y la conexion con sql """

# Agregar el título centrado en la parte superior
table_title = tk.Label(ventana, text="Book List", font=("Arial", 20)).place(
    x=240, y=240
)

#####################################
# TABLA 
#####################################

tabla = ttk.Treeview(ventana, columns=("Id", "Title", "Author", "id_cliente"))
tabla.place(x=100, y=300)

# Agregar encabezados a las columnas
tabla.heading("#0", text="")
tabla.heading("Id", text="ID")
tabla.heading("Title", text="Title")
tabla.heading("Author", text="Author")
tabla.heading("id_cliente", text="id_cliente")

"""
dato= [Agregar Diccionario a dato]    
metodo para ingresar libros
ejemplo dato:
"""
# Definir los datos
datos = [
    ("1", "El Quijote", "Miguel de Cervantes", "464654"),
    ("2", "Cien años de soledad", "Gabriel García Márquez", "57634"),
    ("3", "Head First Python", "Paul Barry", "575686"),
    ("4", "Cronica de una muerte", "Gabriel García Márquez", "54284"),
    ("5", "El Principito", "Antoine de Saint-Exupéry", "4326485"),
]

"""centrar datos en tabla"""

# Agregar los datos a la tabla
for dato in datos:
    tabla.insert("", tk.END, text="", values=dato)

# Ajustar el ancho de las columnas
tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Id", width=30, stretch=tk.NO)
tabla.column("Title", width=150, stretch=tk.NO)
tabla.column("Author", width=120, stretch=tk.NO)
tabla.column("id_cliente", width=80, stretch=tk.NO)

# Alinear el texto de las columnas
tabla.heading("#0", anchor=tk.CENTER)
tabla.heading("Id", anchor=tk.CENTER)
tabla.heading("Title", anchor=tk.CENTER)
tabla.heading("Author", anchor=tk.CENTER)
tabla.heading("id_cliente", anchor=tk.CENTER)


mainloop()
