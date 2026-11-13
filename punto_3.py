"""
Programación Orientada a Objetos 2026-2 - Actividad 4
Ejercicio 6.6 (p. 412): Catchs múltiples - clase CalculosNumericos.

Calcula el logaritmo neperiano y la raíz cuadrada de un valor con métodos
estáticos. Si el valor no es válido se lanza una excepción aritmética.
La interfaz gráfica (tkinter) recibe el valor y gestiona las excepciones con
varios bloques except (equivalente a los catch múltiples de Java).
"""
import math
import tkinter as tk


class CalculosNumericos:
    """Operaciones numéricas que lanzan ArithmeticError con valores inválidos."""

    @staticmethod
    def logaritmo_neperiano(valor):
        # El logaritmo solo está definido para valores positivos
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        # La raíz cuadrada no está definida para valores negativos
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo")
        return math.sqrt(valor)


class VentanaCalculos(tk.Tk):
    """Ventana para ingresar un valor y calcular el logaritmo o la raíz."""

    def __init__(self):
        super().__init__()
        self.title("Cálculos numéricos")
        self.geometry("400x230")
        self.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Ingrese un valor:", anchor="w").place(x=20, y=20, width=120, height=23)
        self.valor = tk.Entry(self)
        self.valor.place(x=150, y=20, width=220, height=23)
        tk.Button(self, text="Logaritmo neperiano",
                  command=lambda: self.calcular(CalculosNumericos.logaritmo_neperiano, "ln")
                  ).place(x=20, y=55, width=170, height=25)
        tk.Button(self, text="Raíz cuadrada",
                  command=lambda: self.calcular(CalculosNumericos.raiz_cuadrada, "raíz")
                  ).place(x=200, y=55, width=170, height=25)
        self.out = tk.Text(self, font=("Courier", 10), state="disabled", wrap="word")
        self.out.tag_config("error", foreground="#B00020")
        self.out.place(x=20, y=95, width=350, height=110)

    def escribir(self, texto, etiqueta=None):
        self.out.config(state="normal")
        self.out.insert(tk.END, texto + "\n", etiqueta)
        self.out.config(state="disabled")

    def calcular(self, funcion, nombre):
        """Calcula con la función indicada y gestiona las excepciones."""
        texto = self.valor.get().strip().replace(",", ".")
        self.out.config(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.config(state="disabled")
        etiqueta = "logaritmo" if nombre == "ln" else "raíz cuadrada"
        try:
            valor = float(texto)
            if not math.isfinite(valor):
                raise ValueError("valor no finito")
            resultado = funcion(valor)
            simbolo = f"ln({valor})" if nombre == "ln" else f"√({valor})"
            self.escribir(f"{simbolo} = {resultado}")
        except ValueError:
            self.escribir(f"El valor debe ser numérico para calcular el {etiqueta}", "error")
        except ArithmeticError as e:
            self.escribir(f"{e} para calcular el {etiqueta}", "error")
        except Exception as e:
            self.escribir(f"Error inesperado: {e}", "error")
        finally:
            self.valor.focus_set()
            self.valor.select_range(0, tk.END)


if __name__ == "__main__":
    app = VentanaCalculos()
    app.mainloop()
