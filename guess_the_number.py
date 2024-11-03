import random
import tkinter as tk
from tkinter import messagebox, font

class AdivinaElNumero:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Número")
        
        self.dificultad = tk.StringVar(value="fácil")
        self.numero_secreto = 0
        self.oportunidades = 0
        
        self.instrucciones = tk.Label(master, text="Selecciona la dificultad:", font=("Helvetica", 16))
        self.instrucciones.pack(pady=10)
        
        self.facil_rb = tk.Radiobutton(master, text="Fácil (1-10)", variable=self.dificultad, value="fácil", command=self.set_dificultad, font=("Helvetica", 14))
        self.facil_rb.pack()

        self.intermedio_rb = tk.Radiobutton(master, text="Intermedio (1-50)", variable=self.dificultad, value="intermedio", command=self.set_dificultad, font=("Helvetica", 14))
        self.intermedio_rb.pack()

        self.dificil_rb = tk.Radiobutton(master, text="Difícil (1-100)", variable=self.dificultad, value="difícil", command=self.set_dificultad, font=("Helvetica", 14))
        self.dificil_rb.pack()
        
        self.start_button = tk.Button(master, text="Iniciar Juego", command=self.iniciar_juego, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        # Widgets ocultos inicialmente
        self.suposicion_entry = tk.Entry(master, font=("Helvetica", 14))
        self.adivinar_button = tk.Button(master, text="Adivinar", command=self.adivinar, font=("Helvetica", 14))
        self.resultado = tk.Label(master, text="", font=("Helvetica", 14))
        self.intentos_label = tk.Label(master, text="", font=("Helvetica", 14))

    def set_dificultad(self):
        self.resultado.config(text="")
        self.suposicion_entry.delete(0, tk.END)

    def iniciar_juego(self):
        if self.dificultad.get() == "fácil":
            self.numero_secreto = random.randint(1, 10)
            self.oportunidades = 3
        elif self.dificultad.get() == "intermedio":
            self.numero_secreto = random.randint(1, 50)
            self.oportunidades = 5
        else:  # difícil
            self.numero_secreto = random.randint(1, 100)
            self.oportunidades = 10
            
        self.intentos_label.config(text=f"Tienes {self.oportunidades} oportunidades.")
        self.resultado.config(text="")
        self.suposicion_entry.delete(0, tk.END)

        # Mostrar widgets de juego
        self.suposicion_entry.pack(pady=10)
        self.adivinar_button.pack(pady=10)
        self.resultado.pack(pady=10)
        self.intentos_label.pack(pady=10)

        # Ocultar botones de dificultad y inicio
        self.facil_rb.pack_forget()
        self.intermedio_rb.pack_forget()
        self.dificil_rb.pack_forget()
        self.start_button.pack_forget()

    def adivinar(self):
        try:
            suposicion = int(self.suposicion_entry.get())

            if (self.dificultad.get() == "fácil" and (suposicion < 1 or suposicion > 10)) or \
               (self.dificultad.get() == "intermedio" and (suposicion < 1 or suposicion > 50)) or \
               (self.dificultad.get() == "difícil" and (suposicion < 1 or suposicion > 100)):
                messagebox.showwarning("Advertencia", "Por favor, introduce un número dentro del rango permitido.")
                return

            if suposicion == self.numero_secreto:
                messagebox.showinfo("¡Felicidades!", "¡Adivinaste el número!")
                self.resetear_juego()
            elif suposicion < self.numero_secreto:
                self.oportunidades -= 1
                self.resultado.config(text="El número es más alto.")
            else:
                self.oportunidades -= 1
                self.resultado.config(text="El número es más bajo.")

            if self.oportunidades == 0:
                messagebox.showinfo("Fin del Juego", f"Lo siento, has agotado tus oportunidades. El número era: {self.numero_secreto}")
                self.resetear_juego()
            else:
                self.intentos_label.config(text=f"Tienes {self.oportunidades} oportunidades.")

        except ValueError:
            messagebox.showwarning("Advertencia", "Por favor, introduce un número válido.")

    def resetear_juego(self):
        self.numero_secreto = 0
        self.oportunidades = 0
        
        # Ocultar widgets de juego
        self.suposicion_entry.pack_forget()
        self.adivinar_button.pack_forget()
        self.resultado.pack_forget()
        self.intentos_label.pack_forget()

        # Volver a mostrar botones de dificultad y reiniciar
        self.instrucciones.pack(pady=10)
        self.facil_rb.pack()
        self.intermedio_rb.pack()
        self.dificil_rb.pack()
        self.start_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    juego = AdivinaElNumero(root)
    root.mainloop()
