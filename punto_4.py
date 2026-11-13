"""
Programación Orientada a Objetos 2026-2 - Actividad 4
Ejercicio 6.7 (p. 418): Validación de campos - EquipoMaratonProgramacion.

Un equipo de maratón de programación tiene nombre, universidad, lenguaje y
tamaño (mínimo dos y máximo tres programadores). Cada programador tiene nombre
y apellidos. Los nombres y apellidos se validan: solo texto (sin dígitos) y
menos de 20 caracteres. Si el equipo está lleno se muestra la excepción.
"""
import tkinter as tk


class EquipoLlenoError(Exception):
    """Se lanza al intentar añadir un programador a un equipo completo."""


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    TAMANO_MINIMO = 2
    TAMANO_MAXIMO = 3
    LONGITUD_MAXIMA = 20   # no se permiten campos con 20 o más caracteres

    def __init__(self, nombre, universidad, lenguaje, tamano):
        for valor, etiqueta in ((nombre, "nombre del equipo"),
                                (universidad, "universidad"),
                                (lenguaje, "lenguaje")):
            if valor.strip() == "":
                raise ValueError(f"El campo {etiqueta} es obligatorio.")
        if not (self.TAMANO_MINIMO <= tamano <= self.TAMANO_MAXIMO):
            raise ValueError("El tamaño del equipo debe ser 2 o 3.")
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        """Determina si el equipo ya tiene todos sus programadores."""
        return len(self.programadores) == self.tamano

    @staticmethod
    def validar_campo(valor, etiqueta):
        """Valida que el campo sea solo texto y de menos de 20 caracteres."""
        if valor.strip() == "":
            raise ValueError(f"El {etiqueta} es obligatorio.")
        if any(c.isdigit() for c in valor):
            raise ValueError(f"El {etiqueta} no puede tener dígitos.")
        if len(valor) >= EquipoMaratonProgramacion.LONGITUD_MAXIMA:
            raise ValueError(f"La longitud del {etiqueta} debe ser menor a 20 caracteres.")

    def agregar_programador(self, nombre, apellidos):
        """Valida los datos y añade el programador; lanza excepción si el
        campo es inválido o si el equipo está completo."""
        self.validar_campo(nombre, "nombre")
        self.validar_campo(apellidos, "apellido")
        if self.esta_completo():
            raise EquipoLlenoError("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(Programador(nombre.strip(), apellidos.strip()))

    def resumen(self):
        lineas = [f"Equipo: {self.nombre} | Universidad: {self.universidad} | Lenguaje: {self.lenguaje}",
                  f"Programadores ({len(self.programadores)}/{self.tamano}):"]
        lineas += [f"  - {p.nombre} {p.apellidos}" for p in self.programadores]
        return "\n".join(lineas)


class VentanaEquipo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equipo de maratón de programación")
        self.geometry("470x490")
        self.resizable(False, False)
        self.equipo = None
        self.crear_interfaz()

    def campo(self, etiqueta, fila):
        tk.Label(self, text=etiqueta, anchor="w").place(x=20, y=15 + 30 * fila, width=170, height=23)
        entrada = tk.Entry(self)
        entrada.place(x=200, y=15 + 30 * fila, width=240, height=23)
        return entrada

    def crear_interfaz(self):
        self.nom = self.campo("Nombre del equipo:", 0)
        self.uni = self.campo("Universidad:", 1)
        self.leng = self.campo("Lenguaje:", 2)
        self.tam = self.campo("Tamaño (2 o 3):", 3)
        tk.Button(self, text="Crear equipo", command=self.crear).place(x=170, y=140, width=120, height=25)
        self.pn = self.campo("Nombre programador:", 6)
        self.pa = self.campo("Apellidos programador:", 7)
        tk.Button(self, text="Añadir programador", command=self.anadir).place(x=160, y=260, width=140, height=25)
        self.out = tk.Text(self, font=("Courier", 10), state="disabled", wrap="word")
        self.out.tag_config("error", foreground="#B00020")
        self.out.place(x=20, y=300, width=430, height=170)

    def escribir(self, texto, etiqueta=None):
        self.out.config(state="normal")
        self.out.insert(tk.END, texto + "\n", etiqueta)
        self.out.config(state="disabled")

    def limpiar_salida(self):
        self.out.config(state="normal")
        self.out.delete("1.0", tk.END)
        self.out.config(state="disabled")

    def crear(self):
        self.limpiar_salida()
        try:
            try:
                tamano = int(self.tam.get().strip())
            except ValueError:
                raise ValueError("El tamaño del equipo debe ser un número entero (2 o 3).")
            self.equipo = EquipoMaratonProgramacion(self.nom.get(), self.uni.get(),
                                                    self.leng.get(), tamano)
            self.escribir("Equipo creado.")
            self.escribir(self.equipo.resumen())
        except ValueError as e:
            self.equipo = None
            self.escribir(f"Excepción: {e}", "error")

    def anadir(self):
        self.limpiar_salida()
        if self.equipo is None:
            self.escribir("Primero debe crear el equipo.", "error")
            return
        try:
            self.equipo.agregar_programador(self.pn.get(), self.pa.get())
            self.pn.delete(0, tk.END)
            self.pa.delete(0, tk.END)
            self.escribir("Programador añadido.")
        except (ValueError, EquipoLlenoError) as e:
            self.escribir(f"Excepción: {e}", "error")
        self.escribir(self.equipo.resumen())


if __name__ == "__main__":
    app = VentanaEquipo()
    app.mainloop()
