import tkinter as tk
import random

# Inicialización de la ventana principal
root = tk.Tk()
root.title("Triki - Tres en Línea")

# Tamaño del tablero y los botones
board_size = 3  # Inicialmente 3x3
board = []
buttons = []

# Pantalla principal
def show_start_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    title_label = tk.Label(root, text="¡Bienvenido a Triki!", font=("Arial", 24))
    title_label.pack(pady=20)

    # Botones para elegir tamaño del tablero
    size_label = tk.Label(root, text="Seleccione el tamaño del tablero:", font=("Arial", 16))
    size_label.pack(pady=10)
    
    btn_3x3 = tk.Button(root, text="3x3", font=("Arial", 16), command=lambda: set_board_size(3))
    btn_3x3.pack(pady=5)
    btn_4x4 = tk.Button(root, text="4x4", font=("Arial", 16), command=lambda: set_board_size(4))
    btn_4x4.pack(pady=5)
    btn_5x5 = tk.Button(root, text="5x5", font=("Arial", 16), command=lambda: set_board_size(5))
    btn_5x5.pack(pady=5)

# Función para configurar el tamaño del tablero y comenzar el juego
def set_board_size(size):
    global board_size, board
    board_size = size
    board = [" " for _ in range(board_size * board_size)]
    start_game()

# Configuración para iniciar el juego
def start_game():
    for widget in root.winfo_children():
        widget.destroy()

    global buttons
    buttons = []

    for i in range(board_size * board_size):
        button = tk.Button(root, text=" ", font=("Arial", 20), width=4, height=2,
                           command=lambda i=i: player_move(i))
        button.grid(row=i // board_size, column=i % board_size)
        buttons.append(button)

    global result_label
    result_label = tk.Label(root, text="", font=("Arial", 16))
    result_label.grid(row=board_size, column=0, columnspan=board_size)

# Función para verificar ganador con tamaños dinámicos
def check_winner(player):
    # Generar condiciones de victoria según el tamaño del tablero
    win_conditions = []

    # Filas
    for row in range(board_size):
        win_conditions.append([row * board_size + col for col in range(board_size)])
    # Columnas
    for col in range(board_size):
        win_conditions.append([col + row * board_size for row in range(board_size)])
    # Diagonal principal
    win_conditions.append([i * (board_size + 1) for i in range(board_size)])
    # Diagonal secundaria
    win_conditions.append([i * (board_size - 1) for i in range(1, board_size + 1)])

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
    for i in range(board_size * board_size):
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
        move = random.randint(0, board_size * board_size - 1)
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
