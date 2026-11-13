"""
Programación Orientada a Objetos 2026-2 - Actividad 4
Ejercicio 6.8 (p. 427): Lectura de archivos - clase LeerArchivo.

Lee un archivo de texto (prueba.txt) línea a línea y muestra su contenido.
En Java se usan FileInputStream + InputStreamReader + BufferedReader; en
Python 'open' con codificación UTF-8 cumple el mismo papel (flujo de bytes
convertido a caracteres y leído línea a línea).
"""
import tkinter as tk
from tkinter import filedialog


class LeerArchivo:
    """Lee el contenido de un archivo de texto."""

    @staticmethod
    def leer(ruta):
        """Devuelve el contenido del archivo. Lanza OSError si no se puede leer."""
        contenido = []
        with open(ruta, "r", encoding="utf-8") as archivo:
            linea = archivo.readline()
            while linea != "":          # readline devuelve "" al final del archivo
                contenido.append(linea)
                linea = archivo.readline()
        return "".join(contenido)


class VentanaLeerArchivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lectura de archivos")
        self.geometry("500x330")
        self.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self, text="Archivo:", anchor="w").place(x=20, y=20, width=60, height=23)
        self.ruta = tk.Entry(self)
        self.ruta.insert(0, "prueba.txt")
        self.ruta.place(x=85, y=20, width=290, height=23)
        tk.Button(self, text="Examinar...", command=self.examinar).place(x=385, y=18, width=95, height=26)
        tk.Button(self, text="Leer archivo", command=self.abrir).place(x=20, y=55, width=120, height=25)
        self.out = tk.Text(self, font=("Courier", 10), state="disabled", wrap="word")
        self.out.tag_config("error", foreground="#B00020")
        self.out.place(x=20, y=95, width=460, height=215)

    def escribir(self, texto, etiqueta=None):
        self.out.config(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.insert(tk.END, texto, etiqueta)
        self.out.config(state="disabled")

    def examinar(self):
        ruta = filedialog.askopenfilename(title="Elegir archivo .txt",
                                          filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            self.ruta.delete(0, tk.END)
            self.ruta.insert(0, ruta)
            self.abrir()

    def abrir(self):
        ruta = self.ruta.get().strip()
        try:
            self.escribir(LeerArchivo.leer(ruta))
        except FileNotFoundError:
            self.escribir(f"Excepción: no se encontró el archivo '{ruta}'.", "error")
        except UnicodeDecodeError:
            self.escribir("Excepción: el archivo no es un texto válido (UTF-8).", "error")
        except OSError as e:
            self.escribir(f"Excepción: no se pudo leer el archivo ({e.strerror}).", "error")


if __name__ == "__main__":
    app = VentanaLeerArchivo()
    app.mainloop()
