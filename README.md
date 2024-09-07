# APLICACIÓN DE CONJUNTOS CON PYTHON
![Imagen tomada de https://help.vizzlo.com/hc/en-us/articles/360013545200-How-to-create-a-Venn-Diagram-with-Vizzlo](./venn.gif)

Cordial saludo maestra. Aqui le mostramos nuestra aplicación sobre conjuntos en Python.
### LOS MÉTODOS HECHOS EN PYTHON SIRVEN PARA UN NÚMERO VARIABLE DE CONJUNTOS DE SER POSIBLE. 
Es decir, las funciones aceptan un número variable de argumentos (podrian ser cero argumentos o decenas)

### Por ejemplo:

``` python
def interseccion(*args: list) -> list:
    """ Método que calcula la interesección entre un número variable de conjuntos"""
    for e in args: clean(e)
    if (len(args) == 0): return []
    res: list = args[0]

    for i in range(1, len(args)):
        res = intersec(res, args[i]) ##Utilizamos la función auxiliar para nuestro metodo maestro.
    return res       
```

# ¿Cómo correr nuestro codigo?

Hemos creado entorno virtual de python con el cual no tendrá que instalar nada.
Los pasos para correr nuestro proyecto mediante Windows PowerShell (y ubicandose en la carpeta ``taller1`` son:
```
venv\Scripts\Activate.ps1
python .\main.py
````