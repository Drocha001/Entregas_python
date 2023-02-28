#####################################
# Module Books
#####################################

from tkinter import *
import tkinter as tk
from tkinter import ttk

mi_id=0
var_titulo=StringVar()
var_autor=StringVar()
var_id_cliente=IntVar()
var_num_cliente=IntVar()


ventana = Tk()
ventana.title("Module1")
ventana.geometry("900x600")
# ventana['bg']= 'COLORCODE'

# Agregar el título centrado en la parte superior
module_name1 = Label(ventana, text="Despacho de Libros", font=("Arial", 20))
module_name1.pack(side="top", fill="both", pady=10)

boton1 = Label(ventana, text="Titulo: ").place(x=30, y=70)
ingreso1 = Entry(ventana, textvariable=var_titulo).place(x=120, y=70)

boton2 = Label(ventana, text="Autor: ").place(x=30, y=100)
ingreso2 = Entry(ventana, textvariable=var_autor).place(x=120, y=100)

boton3 = Label(ventana, text="ID Cliente: ").place(x=30, y=130)
ingreso3 = Entry(ventana, textvariable=var_id_cliente).place(x=120, y=130)

boton4 = Label(ventana, text="TEL Cliente: ").place(x=30, y=160)
ingreso3 = Entry(ventana, textvariable=var_num_cliente).place(x=120, y=160)

def funcion_g():
    global mi_id
    mi_id+=1
    tabla.insert("", "end", text=str(mi_id), values=(var_titulo.get(), var_autor.get(), var_id_cliente.get(), var_num_cliente.get()))

def funcion_d():
    global mi_id
    item= tabla.focus()
    print(item)
    tabla.delete(item)
    mi_id-=1  

def funcion_e():
    print("edit") 

tabla = ttk.Treeview(ventana)
tabla["columns"]=("Id", "Titulo", "Autor", "ID Cliente", "TEL Cliente")
tabla.place(x=100, y=300)

# Ajustar el ancho de las columnas
tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Id", width=30, stretch=tk.NO)
tabla.column("Titulo", width=150, stretch=tk.NO)
tabla.column("Autor", width=150, stretch=tk.NO)
tabla.column("ID Cliente", width=100, stretch=tk.NO)
tabla.column("TEL Cliente", width=100, stretch=tk.NO)

boton_enter1 = Button(ventana, text="ELIMINAR", command=funcion_d).place(x=270, y=205)
boton_enter2 = Button(ventana, text="GUARDAR", command=funcion_g).place(x=200, y=205)
boton_enter3 = Button(ventana, text="EDITAR", command=funcion_e).place(x=150, y=205)


""" Falta la funcion que el dato se agregue a la tabla y la conexion con sql """

# Agregar el título centrado en la parte superior
table_title = tk.Label(ventana, text="Libros Entregados", font=("Arial", 20)).place(
    x=140, y=240
)



# Agregar encabezados a las columnas
tabla.heading("#0", text="")
tabla.heading("Id", text="ID")
tabla.heading("Titulo", text="Titulo")
tabla.heading("Autor", text="Autor")
tabla.heading("ID Cliente", text="ID Cliente")
tabla.heading("TEL Cliente", text="TEL Cliente")

# Alinear el texto de las columnas
tabla.heading("#0", anchor=tk.CENTER)
tabla.heading("Id", anchor=tk.CENTER)
tabla.heading("Titulo", anchor=tk.CENTER)
tabla.heading("Autor", anchor=tk.CENTER)
tabla.heading("ID Cliente", anchor=tk.CENTER)
tabla.heading("TEL Cliente", anchor=tk.CENTER)

mainloop()
