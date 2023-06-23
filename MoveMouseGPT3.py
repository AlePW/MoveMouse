import pyautogui
import time

# coordenadas iniciales
x, y = pyautogui.position()

# variable para alternar el movimiento horizontal
move_right = True

while True:
    # mover el mouse 1 cm a la derecha o a la izquierda, dependiendo del valor de la variable
    if move_right:
        pyautogui.moveRel(10, 0)
    else:
        pyautogui.moveRel(-10, 0)
    
    # alternar el valor de la variable
    move_right = not move_right
    
    # esperar 5 minutos
    time.sleep(300)
