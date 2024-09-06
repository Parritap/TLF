## INTERSECCIÓN
##Función solución
import string
import tkinter as tk
from tkinter import messagebox
from sympy import FiniteSet
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt


def clean(e : list) -> list:
    """Método para limpiar una lista de manera que no permita elementos repetidos."""
    return (list)(set(e))

def subconjunto(conjunto_a : list, conjunto_b : list) -> string:
    """Genera los subconjuntos de A y B"""
    subconjuntos_a = subconjuntos(conjunto_a)
    subconjuntos_b = subconjuntos(conjunto_b)
    return "Los subconjuntos de A son: " + str(subconjuntos_a) + "\n\n" + " y los subconjuntos de B son: " + str(subconjuntos_b)


def subconjuntos(conjunto: list) -> list:
    """método auxiliar para generar los subconjuntos de una lista"""
    if len(conjunto) == 0:
        return [[]]
    sub = subconjuntos(conjunto[:-1])
    return sub + [s + [conjunto[-1]] for s in sub]


def interseccion(*args: list) -> list:
    """ Método que calcula la interesección entre un número variable de conjuntos"""
    for e in args: clean(e)
    if (len(args) == 0): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = intersec(res, args[i]) ##Utilizamos la función auxiliar para nuestro metodo maestro.
    return res


##Función auxiliar
def intersec(a: list, b: list) -> list:
    """Método auxiliar que calcula la intersección entre dos conjuntos dados"""
    return list(filter(lambda x: x in b, a))

    ##DIFERENCIA SIMETRICA
    ##Función solución


def diferencia_simetrica(*args: list) -> list:
    """Método que calcula la diferencia simétrica entre un número variable de conjuntos"""
    for e in args: clean(e)
    if (len(args) == 0): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = dif_sec(res, args[i])
    return res


def dif_sec(a: list, b: list) -> list:
    """Función auxiliar que encuentra la diferencia simétrica entre dos conjuntos"""
    inter: list = intersec(a, b)
    uni: list = union(a, b)
    return list(filter(lambda x: x not in inter, uni))


##Metodos de Osma

def union(conjunto1: list, conjunto2: list) -> list:
    """Encuentra la union entre dos conjuntos"""
    for elemento1 in conjunto1:
        if elemento1 not in conjunto2:
            conjunto2.append(elemento1)
    return conjunto2


##UNION
## Función solución
def union_conjuntos_recursiva(*conjuntos: list, pos: int, conjunto_aux: list) -> None:
    if pos > conjuntos.count:
        return conjunto_aux

    return union_conjuntos_recursiva(conjuntos, pos + 1, union(conjunto_aux, conjuntos[pos]))




# Donde al primer conjunto se le sustraen los elementos de los demás conjuntos.
def diferencia(*args: list) -> list:
    """DIFERENCIA DE CONJUNTOS
        Debe tenerse en consideración que esta funcióin
        realiza la diferencia en el orden en que van indicados los parametros."""
    for e in args:
        clean(e)
    if (len(args) == 0): return []
    res = args[0]
    for i in range(1, len(args)):
        res = dif(res, args[i])
    return res


def dif(a: list, b: list) -> list:
    """Retorna A menos B y no al revez"""
    return list(filter(lambda x: x not in b, a))  ##Esto quiere decir, "todos los elementos de a que no estén en b).

def superconjunto(a : list, b : list) -> string:
    """"Metodo que verifica si el conjunto a superconjunto de b"""
    for e in b:
        if e not in a:
            return "El conjunto A NO es superconjunto de B"
    return "El conjunto A SI es un superconjunto de B"




"""
------------------------------------- ------------------------------------- ------------------------------------- ------------------------------------- 
------------------------------------- MÉTODOS DE LA INTEFAZ GRAFICA---------------------------------------------- ------------------------------------- 
------------------------------------- ------------------------------------- ------------------------------------- ------------------------------------- 
"""


def dibujar_venn(conjunto_a, conjunto_b):
    # agregar los conjuntos a un objeto de tipo FiniteSet

    A = FiniteSet(*conjunto_a)
    B = FiniteSet(*conjunto_b)

    plt.figure(figsize=(6, 8))
    v = venn2(subsets=[A, B], set_labels=('A', 'B'))
    v.get_label_by_id('10').set_text(A - B)
    v.get_label_by_id('11').set_text(A.intersection(B))
    v.get_label_by_id('01').set_text(B - A)
    c = venn2_circles(subsets=[A, B], linestyle='dashed')
    c[0].set_ls('solid')
    plt.show()


class ConjuntosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones de Conjuntos")

        # Variables para almacenar los conjuntos
        self.conjunto_a = []
        self.conjunto_b = []

        # Etiqueta y entrada para el primer conjunto
        self.label_conjunto_a = tk.Label(root, text="Conjunto A:")
        self.entry_conjunto_a = tk.Entry(root)
        self.label_conjunto_a.grid(row=0, column=0, padx=5, pady=5)
        self.entry_conjunto_a.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para el segundo conjunto
        self.label_conjunto_b = tk.Label(root, text="Conjunto B:")
        self.entry_conjunto_b = tk.Entry(root)
        self.label_conjunto_b.grid(row=1, column=0, padx=5, pady=5)
        self.entry_conjunto_b.grid(row=1, column=1, padx=5, pady=5)

        # Menú desplegable para seleccionar la operación
        opciones_operaciones = ["Unión", "Intersección", "Diferencia A-B", "Diferencia B-A", "Diferencia simetrica", "subconjunto", "superconjunto","Ver como diagrama de venn"]
        self.operacion_var = tk.StringVar(root)
        self.operacion_var.set(opciones_operaciones[0])  # Configurar la opción predeterminada
        self.menu_operacion = tk.OptionMenu(root, self.operacion_var, *opciones_operaciones)
        self.menu_operacion.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para realizar la operación
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.realizar_operacion)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

    def obtener_conjuntos_ingresados(self):
        try:
            conjunto_a = list(map(int, self.entry_conjunto_a.get().split(',')))
            conjunto_b = list(map(int, self.entry_conjunto_b.get().split(',')))
            return conjunto_a, conjunto_b
        except ValueError:
            messagebox.showerror("Error", "Ingrese conjuntos válidos (números separados por comas)")
            return None, None

    def realizar_operacion(self):
        conjunto_a, conjunto_b = self.obtener_conjuntos_ingresados()

        resultado = None
        if conjunto_a is not None and conjunto_b is not None:
            operacion = self.operacion_var.get()

            if operacion == "Unión":
                resultado = union(conjunto_a, conjunto_b)
            elif operacion == "Intersección":
                resultado = interseccion(conjunto_a, conjunto_b)
            elif operacion == "Diferencia A-B":
                resultado = diferencia(conjunto_a, conjunto_b)
            elif operacion == "Diferencia B-A":
                resultado = diferencia(conjunto_a, conjunto_b)
            elif operacion == "subconjuntos":
                resultado = subconjunto(conjunto_a, conjunto_b)
            elif operacion == "Diferencia simetrica":
                resultado = diferencia_simetrica(conjunto_a, conjunto_b)
            elif operacion == "superconjunto":
                resultado = superconjunto(conjunto_a, conjunto_b)
            elif operacion == "subconjunto":
                resultado = subconjunto(conjunto_a, conjunto_b)
            elif operacion == "Ver como diagrama de venn":
                dibujar_venn(conjunto_a, conjunto_b)

            if resultado != None:
                messagebox.showinfo("Resultado", f"Resultado de {operacion}: {resultado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()
