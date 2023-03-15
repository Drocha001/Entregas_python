from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from tkinter.messagebox import showinfo
import sqlite3
from tkinter import ttk
import re
import sys
from datetime import date, timedelta
import tkinter as tk
from tkinter.filedialog import askopenfilename

state = ""
"""
prueba
"""


# #########
# enconding: utf-8


def validar ():
    if state=="mod":
        lambda: modificar(
        tree.focus(),
        intro1.get(),
        intro2.get(),
        intro3.get(),
        intro4.get(),
        intro5.get(),
        tree,
        off_btn(),
    ),
        
    else:
        if state=="buscar":
            lambda: modificar(
            tree.focus(),
            intro1.get(),
            intro2.get(),
            intro3.get(),
            intro4.get(),
            intro5.get(),
            tree,
            off_btn(),
        ),
        else:
            print("error en eleccion del estado")
    state=""

def seleccion():
    print("selecto")


def on_btn():
    boton_alta.config(state="normal")
    boton_consulta.config(state="normal")
    boton_modif.config(state="normal")
    boton_borrar.config(state="normal")
    boton_salir.config(state="normal")
    boton_aceptar.config(state="disabled")
    # boton_cancelar.config(state="normal")


def off_btn():
    boton_alta.config(state="disabled")
    boton_consulta.config(state="disabled")
    boton_modif.config(state="disabled")
    boton_borrar.config(state="disabled")
    boton_salir.config(state="disabled")
    boton_aceptar.config(state="normal")


def gg(br, tree):
    # datos=tree.item(br).get("text")
    datos = tree.item(br).get("values")

    intro1.set(datos[0]),
    intro2.set(datos[1]),
    intro3.set(datos[2]),
    intro4.set(datos[3]),
    intro5.set(datos[4]),


# vaciar()


def apago_campos():
    # entrada1 = tk.Entry(state=tk.DISABLED)
    entrada1.config(state="normal")
    entrada2.config(state="disabled")
    entrada3.config(state="disabled")
    entrada4.config(state="disabled")
    entrada5.config(state="disabled")


def prendo_campos():
    # entrada1 = tk.Entry(state=tk.DISABLED)
    entrada1.config(state="normal")
    entrada2.config(state="normal")
    entrada3.config(state="normal")
    entrada4.config(state="normal")
    entrada5.config(state="normal")


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

    cursor = conex.cursor()  # evitamos que ocurra un error si la tabla ya existe
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
    patron_titulo = "^[A-Za-záéíóúüÜñÑ0-9\s]+$"
    patron_autor = "^[A-Za-záéíóúüÜñÑ\s]+$"
    patron_cliente = "^[0-9]*$"

    if not all(
        re.match(patron, cadena)
        for patron, cadena in [
            (patron_titulo, titulo),
            (patron_autor, autor),
            (patron_cliente, cliente),
        ]
    ):
        print("Error en los datos")
        showinfo("¡Atención!", "Hay un error en los datos")
        return

    con = conectar()
    cursor = con.cursor()

    data = (titulo, autor, fecha_retiro, cliente, fecha_dev)

    sql = "INSERT INTO libros(titulo, autor, fecharetiro, cliente, fechadev) VALUES(?, ?, ?, ?, ?)"
    cursor.execute(sql, data)
    con.commit()

    showinfo("¡Perfecto!", "¡Sus datos han sido guardados con éxito!")
    vaciar()
    actualizar_treeview(tree)

    intro3.set(date.today().strftime("%d/%m/%Y"))
    intro5.set((date.today() + timedelta(days=14)).strftime("%d/%m/%Y"))


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
    # selection = combo.get()
    global state 
    state ="consultar"
    apago_campos()
    selection = titulo
    sql = ""
    # sql = "SELECT * FROM libros WHERE "+tabla+"=?"
    ######################################################################################
    if selection.lower() == "titulo":
        tabla = "titulo"
        # voy a concatenar la variable para crear la instruccion a ejecutar segun la elecion del usuario

    else:
        showerror(
            "Error",
            "Debe elegir un elmento de la lista antes de modificar",
        )
        return
    vaciar()

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
    # apago_capos
    
    prendo_campos()


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
    global state
    # gg(br, tree)
    #############
    # datos = tree.item(br).get("values")
    # intro1.set(datos[0]),
    # intro2.set(datos[1]),
    # intro3.set(datos[2]),
    # intro4.set(datos[3]),
    # intro5.set(datos[4]),
    #############
    state="modificar"
    con = conectar()
    cursor = con.cursor()
    id_modif = tree.item(br).get("text")  # obtiene el Id para modificar
    # selection = combo.get()
    tabla = ""
    sql = ""
    # 1) VOY A AVERIGUAR QUE OPCION ELIGIO EL USUARIO
    showinfo("Perfecto!!", "Sus datos han sido modificados con exito!")
    actualizar_treeview(tree)
    vaciar()
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

    # vaciar()

    # salir()

    cursor.execute(sql, dato)
    con.commit()


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
    StringVar(value=date.today().strftime("%d/%m/%Y")),
    StringVar(),
    StringVar(value=(date.today() + timedelta(days=14)).strftime("%d/%m/%Y")),
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
# tree.bind("<<TreeviewSelect>>", seleccion())

# apago_campos()
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
    # takefocus=False
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
    command=lambda:validar( ),
   # """
   # command=lambda: consultar(
   #     intro1.get(),
   #     intro2.get(),
   #     intro3.get(),
   #     intro4.get(),
   #     intro5.get(),
   #     tree,
   # ),"""
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
    command=lambda: gg(
        tree.focus(),
        tree,
        off_btn(),
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
    root,
    text="Salir",
    command=lambda: salir(),
    borderwidth=5,
    cursor="hand1",
)
boton_salir.grid(
    row=19,
    column=13,
    sticky=E + W,
)
boton_aceptar = Button(
    root,
    text="Guardar cambios",
    command=lambda:validar( )
    """command=lambda: modificar(
        tree.focus(),
        intro1.get(),
        intro2.get(),
        intro3.get(),
        intro4.get(),
        intro5.get(),
        tree,
        off_btn(),
    ),"""
    borderwidth=5,
    cursor="hand1",
    # state=flag,
)
boton_aceptar.grid(
    row=19,
    column=8,
    sticky=E + W,
)
"""boton_cancelar = Button(
    root,
    text="Cancelar",
    command=lambda: salir(),
    borderwidth=5,
    cursor="hand1",
)


boton_cancelar.grid(
    row=19,
    column=9,
    sticky=E + W,
)
# combo = ttk.Combobox(
#  state="readonly",
#  values=["Titulo", "Autor", "Retiro", "Cliente", "Devolucion"],
# )
# combo.place(x=550, y=40)b
"""


def seleccionar(mv, parametros):
    try:
        item = mv.selection()[0]
    except IndexError:
        messagebox.showwarning(
            message="Debe seleccionar un elemento.", title="No hay selección"
        )
    else:
        text = mv.item(item, option="text")
        messagebox.showinfo(message=text, title="Selección")

        data = mv.item(item)


"""
# tree.bind("<<TreeviewSelect>>", gg())
if flag == "on":
    boton_cancelar(state=tk.NORMAL),
    boton_aceptar(state=tk.NORMAL),
else:
    boton_cancelar(state=tk.DISABLED),
    boton_aceptar(state=tk.DISABLED),"""
on_btn()
root.mainloop()
