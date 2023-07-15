import cv2
import pyautogui
import numpy as np
from time import sleep
import keyboard
import win32api
import win32con

pyautogui.alert('Vai começar!!!!!!!!!!!!')
sleep(4)


# ponto inicial x=462, y=48
# ponto final x=820, y=477
def clicar(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def tirar_screenshot(pos_inicial_x, pos_inicial_y, largura, altura):
    pyautogui.screenshot('images/piano_tiles.png', region=(pos_inicial_x, pos_inicial_y, largura, altura))


def funcao_analisa(altura_img):
    # abrir imagem
    imagem = cv2.imread(filename="images/piano_tiles.png")
    # Transformar em tons de cinza
    img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # binarizar ou 0 ou 255
    _, imagem_binaria = cv2.threshold(img_cinza, 132, 255, cv2.THRESH_BINARY)
    # inverter a imagem - vai ficar espelhada
    # Vai ficar de baixo para cima e direta pra esquerda
    img_invertida = np.flip(imagem_binaria, axis=0)
    # encontra o primeiro px preto de baixo para cima
    for px_alt, altura in enumerate(img_invertida):
        for px_lar, lagura in enumerate(altura):
            #  Ta passando x = 1, por que eu não sei
            if lagura == 0:
                # Corrigir a altura
                y_real = altura_img - px_alt
                tupla_coord = px_lar + 1, y_real + 1
                return tupla_coord


# CODIGO ESTRUTURADO
# Pegar as coordenadas da imagem
pos_inicial_x = 462
pos_inicial_y = 48
largura = 370
altura = 350
contador = 0
while not keyboard.is_pressed('q'):
    # Tirar prints da tela
    # Coloquei to Try e o except pq chegava um momento que ele não encontrava mais o preto, e dava erro
    # no inicio ele vai muito rápido
    try:
        tirar_screenshot(pos_inicial_x=462, pos_inicial_y=48, largura=370, altura=350)
        # analisar os prints da tela
        primeiro_px_preto = funcao_analisa(altura_img=altura)
        x_img, y_img = primeiro_px_preto
        desconto_x = 20
        desconto_y = 40
        if contador > 190:
            desconto_y = 80
        x_real = (pos_inicial_x + x_img + desconto_x)
        y_real = (pos_inicial_y + y_img + desconto_x)
        # clicar no px preto
        clicar(x_real, y_real)
        contador += 1
    except:
        pass


# Comando para mostrar a imagem na tela
# cv2.imshow('img_jogo', img_invertida)
# cv2.waitKey(0)
# cv2.destroyWindow()
