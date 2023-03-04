#####################################
# Module Books
#####################################

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename

mi_id=0

ventana = Tk()
ventana.title("X Library")
ventana.geometry("900x600")
# ventana['bg']= 'COLORCODE'


var_titulo=StringVar()
var_autor=StringVar()
var_nombre_cliente=StringVar()
var_fecha_dev=StringVar()

# Agregar el título centrado en la parte superior
module_name1 = Label(ventana, text="Despacho de Libros", font=("Arial", 20))
module_name1.pack(side="top", fill="both", pady=10)

boton1 = Label(ventana, text="Titulo: ").place(x=30, y=70)
ingreso1 = Entry(ventana, textvariable=var_titulo).place(x=140, y=70)

boton2 = Label(ventana, text="Autor: ").place(x=30, y=100)
ingreso2 = Entry(ventana, textvariable=var_autor).place(x=140, y=100)

boton3 = Label(ventana, text="Cliente: ").place(x=30, y=130)
ingreso3 = Entry(ventana, textvariable=var_nombre_cliente).place(x=140, y=130)

boton4 = Label(ventana, text="Fecha Devolucion: ").place(x=30, y=160)
ingreso3 = Entry(ventana, textvariable=var_fecha_dev).place(x=140, y=160)

def funcion_g():
    global mi_id
    mi_id+=1
    tabla.insert("", "end", text=str(mi_id), values=(var_titulo.get(), var_autor.get(), var_nombre_cliente.get(), var_fecha_dev.get()))
    showinfo("Perfecto!!", "Sus datos han sido guardados con exito!")

def funcion_d():
    if askyesno("Eliminar datos","Desea eliminar esta entrada??"):
        showinfo("Si", "Eliminando...")
        global mi_id
        item= tabla.focus()
        print(item)
        tabla.delete(item)
        mi_id-=1 
    else:
        showinfo("No", "Continuamos... :)") 

def funcion_e():
    print("edit")
    
tabla = ttk.Treeview(ventana)
tabla["columns"]=("Titulo", "Autor", "Cliente", "Fecha Devolucion")
tabla.place(x=100, y=300)

tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Titulo", width=150, stretch=tk.NO)
tabla.column("Autor", width=150, stretch=tk.NO)
tabla.column("Cliente", width=100, stretch=tk.NO)
tabla.column("Fecha Devolucion", width=120, stretch=tk.NO)

boton_enter1 = Button(ventana, text="ELIMINAR", command=funcion_d).place(x=270, y=205)
boton_enter2 = Button(ventana, text="GUARDAR", command=funcion_g).place(x=200, y=205)
boton_enter3 = Button(ventana, text="EDITAR", command=funcion_e).place(x=150, y=205)

""" Falta la funcion que el dato se agregue a la tabla y la conexion con sql """

# Agregar el título centrado en la parte superior
table_title = tk.Label(ventana, text="Libros Entregados", font=("Arial", 20)).place(x=140, y=240)

# Agregar encabezados a las columnas
tabla.heading("#0", text="ID")
tabla.heading("Titulo", text="Titulo")
tabla.heading("Autor", text="Autor")
tabla.heading("Cliente", text="Cliente")
tabla.heading("Fecha Devolucion", text="Fecha Devolucion")

# Alinear el texto de las columnas
tabla.heading("#0", anchor=tk.CENTER)
tabla.heading("Titulo", anchor=tk.CENTER)
tabla.heading("Autor", anchor=tk.CENTER)
tabla.heading("Cliente", anchor=tk.CENTER)
tabla.heading("Fecha Devolucion", anchor=tk.CENTER)

def menu():
    print("Menu")

menubar=Menu(ventana)
menu_archivo=Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Info", command=menu)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo",menu=menu_archivo)

ventana.config(menu=menubar)

mainloop()
