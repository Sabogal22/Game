import tkinter as tk
import random

# Inicialización de la ventana principal
root = tk.Tk()
root.title("Triki - Tres en Línea")

# Crear el tablero vacío y los botones
board = [" " for _ in range(9)]
buttons = []

# Pantalla principal
def show_start_screen():
  for widget in root.winfo_children():
    widget.destroy()
    
  title_label = tk.Label(root, text="¡Bienvenido a Triki!", font=("Arial", 24))
  title_label.pack(pady=20)

  start_button = tk.Button(root, text="Jugar partida", font=("Arial", 16), command=start_game)
  start_button.pack(pady=10)

# Configuración para iniciar el juego
def start_game():
  for widget in root.winfo_children():
    widget.destroy()

  global board, buttons
  board = [" " for _ in range(9)]
  buttons = []

  for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
      command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

  global result_label
  result_label = tk.Label(root, text="", font=("Arial", 16))
  result_label.grid(row=3, column=0, columnspan=3)

# Función para verificar ganador
def check_winner(player):
  win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
    [0, 4, 8], [2, 4, 6]              # Diagonales
  ]
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

# Función para verificar si hay empate
def check_tie():
  return " " not in board

# Movimiento del jugador
def player_move(index):
  if board[index] == " ":
    board[index] = "X"
    buttons[index].config(text="X", state="disabled")
    if check_winner("X"):
      end_game("¡Felicidades! Has ganado.")
    elif check_tie():
      end_game("Es un empate.")
    else:
      computer_move()

# Movimiento de la máquina para evitar perder
def computer_move():
  for i in range(9):
    if board[i] == " ":
      board[i] = "O"
    if check_winner("O"):
      buttons[i].config(text="O", state="disabled")
      end_game("La máquina ha ganado. ¡Intenta de nuevo!")
      return
    board[i] = "X"
    if check_winner("X"):
      board[i] = "O"
      buttons[i].config(text="O", state="disabled")
      return
    board[i] = " "

  while True:
    move = random.randint(0, 8)
    if board[move] == " ":
      board[move] = "O"
      buttons[move].config(text="O", state="disabled")
      break

  if check_winner("O"):
    end_game("La máquina ha ganado. ¡Intenta de nuevo!")
  elif check_tie():
    end_game("Es un empate.")

# Finalización del juego y regreso a la pantalla principal
def end_game(message):
  for button in buttons:
    button.config(state="disabled")
  result_label.config(text=message)

  # Regresar a la pantalla de inicio después de un breve tiempo
  root.after(2000, show_start_screen)

# Muestra la pantalla de inicio al iniciar la aplicación
show_start_screen()

# Ejecuta la aplicación
root.mainloop()
