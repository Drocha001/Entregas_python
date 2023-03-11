from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename

"""
prueba
"""


# #########
# enconding: utf-8
def apago_campos():
    entrada1 = ttk.Entry(state=tk.DISABLED)
    entrada2 = ttk.Entry(state=tk.DISABLED)
    entrada3 = ttk.Entry(state=tk.DISABLED)
    entrada4 = ttk.Entry(state=tk.DISABLED)
    entrada5 = ttk.Entry(state=tk.DISABLED)


def prendo_aceptar():
    boton_salir = Button(
        root,
        text="Cancelar",
        command=lambda: salir(),
        borderwidth=5,
        cursor="hand1",
        state=tk.DISABLED,
    )


def vaciar():
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    entrada4.delete(0, END)
    entrada5.delete(0, END)


def conectar():
    con = sqlite3.connect("nueva_alejandria.db")
    return con


def crear_tb():
    conex = conectar()

    cursor = conex.cursor()
    tabla = """CREATE TABLE IF NOT EXISTS libros
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
    cadena = titulo
    patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
    if re.match(patron, cadena):
        con = conectar()
        cursor = con.cursor()
        data = (titulo, autor, fecha_retiro, cliente, fecha_dev)
        sql = "INSERT INTO libros(titulo, autor, fecharetiro, cliente,fechadev) VALUES(?, ?, ?,?,?)"
        cursor.execute(sql, data)
        con.commit()
        showinfo("Perfecto!!", "Sus datos han sido guardados con exito!")
        vaciar()
        actualizar_treeview(tree)
    else:
        showinfo("Error", "Emplee solo caracteres alfabeticos")


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


def consultar(titulo, autor, retiro, cliente, dev, tree):
    selection = combo.get()
    tabla = ""
    sql = ""
    # sql = "SELECT * FROM libros WHERE "+tabla+"=?"
    ######################################################################################
    if selection.lower() == "titulo":
        tabla = "titulo"
        # voy a concatenar la variable para crear la instruccion a ejecutar segun la elecion del usuario

    else:
        if selection.lower() == "autor":
            sql = ""
            tabla = "autor"
            # sql = "SELECT * FROM libros WHERE "+tabla+"=?"
            # voy a concatenar la variable para crear la instruccion a ejecutar segun la elecion del usuario

            if selection.lower() == "retiro":
                sql = ""
                tabla = "fecharetiro"

            else:
                if selection.lower() == "çliente":
                    sql = ""
                    tabla = "cliente"

                else:
                    if selection.lower() == "devolucion":
                        tabla = "fechadev"

                    else:
                        showerror(
                            "Error",
                            "Debe elegir un elmento de la lista antes de modificar",
                        )
                        vaciar()
                        return
    ######################################################################################
    sql = "SELECT * FROM libros WHERE " + tabla + "=?"
    # sql = "SELECT * FROM libros WHERE titulo =?  "
    dato = (tabla,)
    con = conectar()
    cursor = con.cursor()
    cursor.execute(sql, dato)
    con.commit()
    resultado = cursor.fetchall()
    # print(resultado)
    # actualizar_treeview(tree)
    vaciar()
    entrada1.insert(0, titulo)
    entrada2.insert(0, autor)
    entrada3.insert(0, retiro)
    entrada4.insert(0, cliente)
    entrada5.insert(0, dev)


def borrar(br, tree):
    # agregar confirmacion
    if askyesno("Eliminar datos", "Desea eliminar esta entrada??"):
        showinfo("Borrar: ", "Eliminando...")
        ######### BORRADO ####################
        # obtengo el id para buscar en la base de datos
        borrar = tree.item(br).get("text")
        con = conectar()
        cursor = con.cursor()
        sql = "DELETE FROM libros WHERE id = (?) "
        dato = (borrar,)  # tupla de datos
        cursor.execute(sql, dato)
        con.commit()
        vaciar()

    else:
        showinfo("No", "Continuamos... :)")
    actualizar_treeview(tree)


def modificar(br, titulo, autor, fecharetiro, cliente, fechadev, tree):
    con = conectar()
    cursor = con.cursor()
    id_modif = tree.item(br).get("text")  # obtiene el Id para modificar
    selection = combo.get()
    tabla = ""
    sql = ""
    # 1) VOY A AVERIGUAR QUE OPCION ELIGIO EL USUARIO

    if selection.lower() == "titulo":
        tabla = "titulo"
        # voy a concatenar la variable para crear la instruccion a ejecutar segun la elecion del usuario
        sql = ""
        sql = (
            "UPDATE libros SET "
            + tabla
            + "=?"
            + ",autor=?, fecharetiro=?, cliente=?,fechadev=?  WHERE id=? "
        )
        dato = (
            titulo,
            autor,
            fecharetiro,
            cliente,
            fechadev,
            id_modif,
        )  # tupla de datos
    else:
        if selection.lower() == "autor":
            sql = ""
            tabla = "autor"
            # voy a concatenar la variable para crear la instruccion a ejecutar segun la elecion del usuario
            sql = (
                "UPDATE libros SET "
                + tabla
                + "=?"
                + ",titulo=?, fecharetiro=?, cliente=?,fechadev=?  WHERE id=? "
            )
            dato = (
                autor,
                titulo,
                fecharetiro,
                cliente,
                fechadev,
                id_modif,
            )  # tupla de datos
        else:
            if selection.lower() == "retiro":
                sql = ""
                tabla = "fecharetiro"
                sql = (
                    "UPDATE libros SET "
                    + tabla
                    + "=?"
                    + ",titulo=?,autor=?,cliente=?,fechadev=?  WHERE id=? "
                )
                dato = (
                    fecharetiro,
                    titulo,
                    autor,
                    cliente,
                    fechadev,
                    id_modif,
                )  # tupla de datos
            else:
                if selection.lower() == "çliente":
                    sql = ""
                    tabla = "cliente"
                    sql = (
                        "UPDATE libros SET "
                        + tabla
                        + "=?"
                        + ",titulo=?,autor=?,fecharetiro=?,fechadev=?  WHERE id=? "
                    )
                    dato = (
                        cliente,
                        titulo,
                        autor,
                        fecharetiro,
                        fechadev,
                        id_modif,
                    )  # tupla de datos
                else:
                    if selection.lower() == "devolucion":
                        tabla = "fechadev"
                        sql = ""
                        sql = (
                            "UPDATE libros SET "
                            + tabla
                            + "=?"
                            + ",titulo=?,autor=?,fecharetiro=?,cliente=?  WHERE id=? "
                        )
                        dato = (
                            fechadev,
                            titulo,
                            autor,
                            fecharetiro,
                            cliente,
                            id_modif,
                        )  # tupla de datos
                    else:
                        showerror(
                            "Error",
                            "Debe elegir un elmento de la lista antes de modificar",
                        )
                        vaciar()
                        return
                        # salir()

    cursor.execute(sql, dato)
    con.commit()

    showinfo("Perfecto!!", "Sus datos han sido modificados con exito!")
    actualizar_treeview(tree)
    vaciar()


try:
    conectar()
    crear_tb()
except:
    print("Hay un error")
# enconding: utf-8

################## MAIN #########################################

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
# libro = Label(root, text="Creiterio: ")
# libro.grid(
#    row=1,
#    column=2,
#    sticky=E,
# )
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

# entrada1 = ttk.Entry(state=tk.DISABLED)
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


apago_campos()
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
    # row=8,
    row=19,
    column=0,
    sticky=W + E,
)

boton_consulta = Button(
    root,
    text="Buscar",
    command=lambda: consultar(
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
boton_consulta.grid(
    row=19,
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
    ),
    borderwidth=5,
    cursor="hand1",
)
boton_modif.grid(
    row=19,
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
    row=19,
    column=3,
    sticky=W + E,
)
boton_salir = Button(
    root, text="Salir", command=lambda: salir(), borderwidth=5, cursor="hand1"
)
boton_salir.grid(
    row=19,
    column=13,
    sticky=E + W,
)
boton_salir = Button(
    root,
    text="Aceptar",
    command=lambda: salir(),
    borderwidth=5,
    cursor="hand1",
    state=tk.DISABLED,
)
boton_salir.grid(
    row=19,
    column=8,
    sticky=E + W,
)
boton_salir = Button(
    root,
    text="Cancelar",
    command=lambda: salir(),
    borderwidth=5,
    cursor="hand1",
    state=tk.DISABLED,
)
boton_salir.grid(
    row=19,
    column=9,
    sticky=E + W,
)
# combo = ttk.Combobox(
#  state="readonly",
#  values=["Titulo", "Autor", "Retiro", "Cliente", "Devolucion"],
# )
# combo.place(x=550, y=40)b


root.mainloop()
