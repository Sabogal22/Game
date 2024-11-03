import tkinter as tk
from tkinter import messagebox
import random

class GuessTheCodeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Código")
        
        self.difficulty = None  # Variable para almacenar la dificultad
        self.attempts = 0
        self.max_attempts = 10  # Límite de intentos
        self.score = 0  # Inicializar la puntuación
        self.start_game()

    def start_game(self):
        self.select_difficulty()

    def select_difficulty(self):
        self.clear_window()
        self.label = tk.Label(self.master, text="Selecciona la dificultad:\nFácil, Intermedio o Difícil", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.easy_button = tk.Button(self.master, text="Fácil", command=lambda: self.start_new_game(4, 5), font=("Helvetica", 14))
        self.easy_button.pack(pady=10)
        
        self.medium_button = tk.Button(self.master, text="Intermedio", command=lambda: self.start_new_game(4, 9), font=("Helvetica", 14))
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self.master, text="Difícil", command=lambda: self.start_new_game(6, 9), font=("Helvetica", 14))
        self.hard_button.pack(pady=10)

    def start_new_game(self, code_length, max_number):
        self.code_length = code_length
        self.max_number = max_number
        self.code = self.generate_code()
        self.attempts = 0
        self.max_attempts = 10 if code_length == 4 else 5  # Cambiar límite de intentos según la dificultad
        self.clear_window()
        self.setup_game_interface()

    def generate_code(self):
        return [random.randint(0, self.max_number) for _ in range(self.code_length)]
    
    def setup_game_interface(self):
        self.label = tk.Label(self.master, text=f"Adivina el código de {self.code_length} números (0 a {self.max_number}):", font=("Helvetica", 14))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.master, text="Adivinar", command=self.check_guess, font=("Helvetica", 14))
        self.submit_button.pack(pady=20)

    def check_guess(self):
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Fin del Juego", f"No adivinaste el código: {''.join(map(str, self.code))}.")
            self.select_difficulty()
            return

        guess = self.entry.get()
        if len(guess) != self.code_length or not guess.isdigit():
            messagebox.showerror("Error", f"Por favor, ingresa exactamente {self.code_length} números.")
            return

        self.attempts += 1
        guess_list = [int(num) for num in guess]
        
        correct_position = sum(1 for i in range(self.code_length) if guess_list[i] == self.code[i])
        correct_numbers = sum(min(guess_list.count(x), self.code.count(x)) for x in set(guess_list))
        incorrect_position = correct_numbers - correct_position
        
        result_message = f"Intento {self.attempts}/{self.max_attempts}: {correct_position} en la posición correcta, {incorrect_position} en la posición incorrecta."
        
        if correct_position == self.code_length:
            # Calcular puntuación (ejemplo simple)
            self.score += (self.max_attempts - self.attempts + 1) * 10  # 10 puntos por intento no usado
            messagebox.showinfo("¡Felicidades!", f"¡Adivinaste el código: {''.join(map(str, self.code))}!\nTu puntuación es: {self.score}.")
            self.select_difficulty()
        else:
            messagebox.showinfo("Resultado", result_message)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheCodeGame(root)
    root.mainloop()
