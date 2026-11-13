"""
Programación Orientada a Objetos 2026-2 - Actividad 4
Ejercicio 6.4 (p. 400): Excepciones - bloques try / catch / finally.

El programa original imprime mensajes en consola. Aquí cada mensaje se envía
a una interfaz gráfica (tkinter): al pulsar el botón se ejecuta el código del
ejercicio y el resultado aparece en el área de texto.
"""
import tkinter as tk


class PruebaExcepciones:
    """Lanza diferentes excepciones en situaciones específicas del programa.
    Los mensajes ayudan a identificar la porción de código que se ejecutó."""

    def ejecutar(self, salida):
        """Equivalente al método main del libro. 'salida' es una función que
        recibe cada mensaje (en el libro era System.out.println)."""
        # Primer bloque try
        try:
            salida("Ingresando al primer try")
            cociente = 10000 / 0              # Se lanza una excepción
            salida("Después de la división")  # Nunca se ejecuta
        except ArithmeticError:               # Se captura la excepción
            salida("División por cero")
        finally:
            # finally siempre se ejecuta, ocurra o no una excepción
            salida("Ingresando al primer finally")

        # Segundo bloque try
        try:
            salida("Ingresando al segundo try")
            objeto = None
            objeto.upper()                    # Se lanza una excepción (equivale a NullPointerException)
            salida("Imprimiendo objeto")      # Nunca se ejecuta
        except ArithmeticError:               # La excepción lanzada no es de este tipo
            salida("División por cero")
        except Exception:                     # Se captura la excepción
            salida("Ocurrió una excepción")
        finally:
            salida("Ingresando al segundo finally")


class VentanaExcepciones(tk.Tk):
    """Ventana con un botón que ejecuta la prueba y muestra el resultado."""

    def __init__(self):
        super().__init__()
        self.title("Excepciones")
        self.geometry("420x290")
        self.resizable(False, False)
        self.prueba = PruebaExcepciones()
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Resultado de la ejecución del método main:",
                 anchor="w").place(x=20, y=15, width=380, height=23)
        self.btn_ejecutar = tk.Button(self, text="Ejecutar PruebaExcepciones",
                                      command=self.ejecutar)
        self.btn_ejecutar.place(x=20, y=45, width=200, height=25)
        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=230, y=45, width=100, height=25)
        self.out = tk.Text(self, font=("Courier", 10), state="disabled", wrap="word")
        self.out.place(x=20, y=85, width=380, height=185)

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.insert(tk.END, texto + "\n")
        self.out.config(state="disabled")

    def ejecutar(self):
        self.limpiar()
        self.prueba.ejecutar(self.escribir)

    def limpiar(self):
        self.out.config(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.config(state="disabled")


if __name__ == "__main__":
    app = VentanaExcepciones()
    app.mainloop()
