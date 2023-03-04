from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename


# #########
# enconding: utf-8


def conectar():
    con = sqlite3.connect("nueva_alejandria.db")
    return con


def crear_tb():
    conex = conectar()

    cursor = conex.cursor()
    tabla = """CREATE TABLE libros
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             titulo varchar(80) NOT NULL, 
             autor varchar(80) NOT NULL,             
             fecharetiro varchar(8) NOT NULL,
             cliente varchar(80) NOT NULL,
             fechadev varchar(8) NOT NULL,

             copias int,
             precio real)
    """
    cursor.execute(tabla)
    conex.commit()


def salir():
    sys.exit()


def cargar(titulo, autor, fecha_retiro, cliente, fecha_dev, tree):
    con = conectar()
    cursor = con.cursor()
    data = (titulo, autor, fecha_retiro, cliente, fecha_dev)
    sql = "INSERT INTO libros(titulo, autor, fecharetiro, cliente,fechadev) VALUES(?, ?, ?,?,?)"
    cursor.execute(sql, data)
    con.commit()
    showinfo("Perfecto!!", "Sus datos han sido guardados con exito!")
    actualizar_treeview(tree)


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM libros ORDER BY id ASC"
    con = conectar()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        # print(fila)
        mitreview.insert(
            "",
            0,
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5]),
        )


def consultar(titulo, tree):
    sql = "SELECT * FROM libros WHERE titulo =?  "
    dato = (titulo,)
    con = conectar()
    cursor = con.cursor()
    cursor.execute(sql, dato)
    con.commit()
    resultado = cursor.fetchall()
    print(resultado)
    actualizar_treeview(tree)


def borrar(br, tree):
    # agregar confirmacion
    if askyesno("Eliminar datos", "Desea eliminar esta entrada??"):
        showinfo("Borrar: ", "Eliminando...")
        ######### BORRADO ####################
        borrar = tree.item(br).get(
            "text"
        )  # obtengo el id para buscar en l abase de datos
        con = conectar()
        cursor = con.cursor()
        sql = "DELETE FROM libros WHERE id = (?) "
        dato = (borrar,)  # tupla de datos
        cursor.execute(sql, dato)
        con.commit()

    else:
        showinfo("No", "Continuamos... :)")
    actualizar_treeview(tree)


def modificar(br, titulo, autor, fecha_retiro, cliente, fecha_dev, tree, campo):
    con = conectar()
    cursor = con.cursor()
    accion = "titulo"
    selection = combo.get()

    modif = tree.item(br).get("text")  # obtiene el Id para modificar
    con = conectar()
    cursor = con.cursor()
    modif = tree.item(br).get("text")  # obtiene el Id para modificar
    sql = "UPDATE libros SET titulo=?, autor=?, fecharetiro=?, cliente=?,fechadev=?  WHERE id=? "
    dato = (
        titulo,
        autor,
        fecha_retiro,
        cliente,
        fecha_dev,
        modif,
    )  # tupla de datos
    cursor.execute(sql, dato)
    con.commit()

    showinfo("Perfecto!!", "Sus datos han sido modificados con exito!")
    actualizar_treeview(tree)


try:
    conectar()
    crear_tb()
except:
    print("Hay un error")
# enconding: utf-8

################## interface de prueba

root = Tk()


root.title("X Library")
root.geometry("835x410")
titulo = Label(
    root,
    text=" Despacho de Libros",
    font=("Arial", 20),
    bg="grey",
    fg="white",
    height=1,
    width=50,
)

titulo.grid(row=0, column=0, columnspan=15, padx=1, pady=1, sticky=W + E)

libro = Label(root, text="Titulo")
libro.grid(
    row=1,
    column=0,
    sticky=W,
)
libro = Label(root, text="Creiterio: ")
libro.grid(
    row=1,
    column=2,
    sticky=E,
)

autor = Label(root, text="Autor")
autor.grid(row=2, column=0, sticky=W)

retiro = Label(root, text="Fecha de retiro")
retiro.grid(row=3, column=0, sticky=W)

cliente = Label(root, text="Cliente que retiro")
cliente.grid(
    row=4,
    column=0,
    sticky=W,
)
dev = Label(root, text="Fecha devolucion")
dev.grid(
    row=5,
    column=0,
    sticky=W,
)
dev.grid


# Defino variables para tomar valores de campos de entrada
intro1, intro2, intro3, intro4, intro5 = (
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
)


entrada1 = Entry(
    root,
    textvariable=intro1,
    width=50,
)

entrada1.grid(row=1, column=1, sticky=W + E)
entrada2 = Entry(
    root,
    textvariable=intro2,
    width=50,
)
entrada2.grid(row=2, column=1, sticky=W + E)
entrada3 = Entry(
    root,
    textvariable=intro3,
    width=8,
)
entrada3.grid(row=3, column=1, sticky=W + E)
entrada4 = Entry(
    root,
    textvariable=intro4,
    width=8,
)
entrada4.grid(row=4, column=1, sticky=W + E)
entrada5 = Entry(
    root,
    textvariable=intro5,
    width=8,
)
entrada5.grid(row=5, column=1, sticky=W + E)


# TREEVIEW


tree = ttk.Treeview(root)
actualizar_treeview(tree)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")

tree.column(
    "#0",
    width=30,
    minwidth=50,
    anchor=W,
)
tree.column(
    "col1",
    width=200,
    minwidth=50,
    anchor=W,
)
tree.column(
    "col2",
    width=200,
    minwidth=50,
    anchor=W,
)
tree.column(
    "col3",
    width=100,
    minwidth=50,
    anchor=W,
)
tree.column(
    "col4",
    width=200,
    minwidth=50,
    anchor=W,
)
tree.column(
    "col5",
    width=100,
    minwidth=50,
    anchor=W,
)

tree.grid(
    row=10,
    column=0,
    columnspan=14,
    sticky=W,
)
tree.heading("#0", text="ID")
tree.heading("col1", text="Titulo")
tree.heading("col2", text="Autor")
tree.heading("col3", text="Retiro")
tree.heading("col4", text="Cliente")
tree.heading("col5", text="Devolucion")


boton_alta = Button(
    root,
    text="Alta",
    command=lambda: cargar(
        intro1.get(),
        intro2.get(),
        intro3.get(),
        intro4.get(),
        intro5.get(),
        tree,
    ),
    borderwidth=5,
    cursor="hand1",
)
boton_alta.grid(
    row=8,
    column=0,
    sticky=W + E,
)

boton_consulta = Button(
    root,
    text="Buscar",
    command=lambda: consultar(intro1.get(), tree),
    borderwidth=5,
    cursor="hand1",
)
boton_consulta.grid(
    row=8,
    column=1,
    sticky=W + E,
)

boton_modif = Button(
    root,
    text="Modificar",
    command=lambda: modificar(
        tree.focus(),
        intro1.get(),
        intro2.get(),
        intro3.get(),
        intro4.get(),
        intro5.get(),
        tree,
        " titulo ",
    ),
    borderwidth=5,
    cursor="hand1",
)
boton_modif.grid(
    row=8,
    column=2,
    sticky=W + E,
)
boton_borrar = Button(
    root,
    text="Borrar",
    command=lambda: borrar(
        tree.focus(),
        tree,
    ),
    borderwidth=5,
    cursor="hand1",
)
boton_borrar.grid(
    row=8,
    column=3,
    sticky=W + E,
)
boton_salir = Button(
    root, text="Salir", command=lambda: salir(), borderwidth=5, cursor="hand1"
)
boton_salir.grid(
    row=8,
    column=9,
    sticky=E + W,
)

combo = ttk.Combobox(
    state="readonly",
    values=["Titulo", "Autor", "Retiro", "Cliente", "Devolucion"],
)
combo.place(x=550, y=40)


root.mainloop()
