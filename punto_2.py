"""
Programación Orientada a Objetos 2026-2 - Actividad 4
Ejercicio 6.5 (p. 406): Lanzamiento de excepciones - clase Vendedor.

El vendedor tiene nombre, apellidos y edad. Al verificar la edad se lanza una
excepción (ValueError, equivalente a IllegalArgumentException de Java) si el
vendedor no es mayor de edad o si la edad está fuera del rango 0 a 120.
Los datos se ingresan en una interfaz gráfica (tkinter) en lugar del teclado.
"""
import tkinter as tk


class Vendedor:
    """Modela un vendedor con nombre, apellidos y edad."""

    EDAD_MINIMA = 18
    EDAD_MAXIMA = 120

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        """Devuelve el texto con los valores de los atributos."""
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        """Verifica la edad y la asigna; si no es válida lanza ValueError."""
        if edad < 0 or edad > Vendedor.EDAD_MAXIMA:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < Vendedor.EDAD_MINIMA:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad


class VentanaVendedor(tk.Tk):
    """Ventana con los campos del vendedor, el botón y el resultado."""

    def __init__(self):
        super().__init__()
        self.title("Vendedor")
        self.geometry("380x300")
        self.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        self.campos = {}
        for i, etiqueta in enumerate(["Nombre:", "Apellidos:", "Edad:"]):
            tk.Label(self, text=etiqueta, anchor="w").place(x=20, y=20 + 30 * i, width=90, height=23)
            campo = tk.Entry(self)
            campo.place(x=120, y=20 + 30 * i, width=230, height=23)
            self.campos[etiqueta] = campo
        self.nom = self.campos["Nombre:"]
        self.ape = self.campos["Apellidos:"]
        self.edad = self.campos["Edad:"]
        tk.Button(self, text="Crear vendedor", command=self.crear).place(x=120, y=112, width=120, height=25)
        self.out = tk.Text(self, font=("Courier", 10), state="disabled", wrap="word")
        self.out.tag_config("error", foreground="#B00020")
        self.out.place(x=20, y=150, width=330, height=130)

    def escribir(self, texto, etiqueta=None):
        self.out.config(state="normal")
        self.out.insert(tk.END, texto + "\n", etiqueta)
        self.out.config(state="disabled")

    def limpiar_salida(self):
        self.out.config(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.config(state="disabled")

    def crear(self):
        """Lee los datos, crea el vendedor y verifica la edad."""
        self.limpiar_salida()
        try:
            nombre = self.nom.get().strip()
            apellidos = self.ape.get().strip()
            if nombre == "" or apellidos == "":
                raise ValueError("El nombre y los apellidos son obligatorios.")
            try:
                edad = int(self.edad.get().strip())
            except ValueError:
                raise ValueError("La edad debe ser un número entero.")
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)   # puede lanzar ValueError
            self.escribir("Vendedor creado:")
            self.escribir(vendedor.imprimir())
        except ValueError as e:
            self.escribir(f"Excepción: {e}", "error")


if __name__ == "__main__":
    app = VentanaVendedor()
    app.mainloop()
