# Game 🎮
Este repositorio contiene cuatro juegos clásicos desarrollados en Python: el juego de la serpiente, el juego de triki (tres en línea), el juego de adivinar números y el juego de adivinar un código. Todos están diseñados para brindar una experiencia de juego sencilla y entretenida, permitiendo a los usuarios disfrutar de estos clásicos en su computadora.

## Juegos Incluidos

### 1. Juego de la Serpiente 🐍
En este juego, el jugador controla una serpiente que debe comer la comida que aparece aleatoriamente en la pantalla. Cada vez que come, la serpiente crece, aumentando así la dificultad del juego. La meta es obtener el puntaje más alto posible sin chocar contra el propio cuerpo de la serpiente.

- **Características**:
  - Marcador en pantalla que muestra la puntuación y el puntaje más alto.
  - Incremento en la velocidad del juego a medida que la serpiente crece.
  - Colisiones con los bordes de la pantalla con regreso automático al lado opuesto.
  
- **Controles**:
  - Usa las teclas `W`, `A`, `S`, `D` para mover la serpiente en las direcciones correspondientes.

### 2. Juego de Triki (Tres en Línea) ✖️⭕
Este es un juego de tres en línea donde puedes jugar contra la computadora. Puedes elegir el tamaño de la cuadrícula (3x3, 4x4 o 5x5) para aumentar la dificultad y la duración del juego. La computadora elige sus jugadas estratégicamente para evitar que ganes.

- **Características**:
  - Opciones de tamaño de cuadrícula: 3x3 (fácil), 4x4 (intermedio) y 5x5 (difícil).
  - La computadora toma decisiones para bloquear tus posibles victorias.
  - Interfaz visual con opción de reinicio.

- **Controles**:
  - Selecciona el tamaño de la cuadrícula y haz clic en los paneles para realizar tus jugadas.

### 3. Adivina el Número 🔢
En este juego, la máquina generará un número aleatorio dentro de un rango específico según el nivel de dificultad que elijas. El jugador tendrá que adivinar cuál es ese número en un número limitado de oportunidades. Después de cada intento, el juego indicará si el número es más alto o más bajo que la suposición.

- **Características**:
  - Tres niveles de dificultad: Fácil (1-10), Intermedio (1-50) y Difícil (1-100).
  - Indicación de si el número a adivinar es más alto o más bajo.
  - Oportunidades limitadas según el nivel de dificultad.
  - Juego reiniciable.

- **Controles**:
  - Selecciona la dificultad y utiliza el campo de entrada para hacer tu suposición.

### 4. Adivina el Código 🔐
En este juego, la máquina genera un código de números aleatorios, y el jugador debe adivinarlo. El código tiene una longitud variable según el nivel de dificultad elegido. El juego indicará cuántos números están correctos y cuántos están en la posición incorrecta.

- **Características**:
  - Tres niveles de dificultad: Fácil (4 números, rango 0-5), Intermedio (4 números, rango 0-9), Difícil (6 números, rango 0-9).
  - Indicación de números correctos en posición correcta y en posición incorrecta.
  - Oportunidades limitadas según el nivel de dificultad.
  - Sistema de puntuación basado en los intentos utilizados.

- **Controles**:
  - Selecciona la dificultad y utiliza el campo de entrada para hacer tu suposición.

## Requisitos
- Python 3.x
- Biblioteca `turtle` (incluida con Python)

## Instalación y Ejecución
1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/Sabogal22/Game.git
   cd Game

2. **Arrancar el juego de la serpiente**:
   ```bash
   python snake_game.py

2. **Arrancar el juego de triki**:
   ```bash
   python triki_game.py

2. **Arrancar el juego del numero mayor**:
   ```bash
   python guess_the_number.py
   
2. **Arrancar el juego del codigo**:
   ```bash
   python guess_the_code.py

## Contribuciones
Las contribuciones para mejorar estos juegos son bienvenidas. Si tienes ideas o mejoras, no dudes en abrir un pull request y los revisaré para mejorar los juegos.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
