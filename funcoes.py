import cv2
import numpy as np

def redimensionar_img_func (img, largura_px, altura_px):
    img_redimensionada = cv2.resize(img, (int(largura_px), int(altura_px)))
    return img_redimensionada

def escala_cinza(img):
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_cinza

def invert_cores(img):
    img_invertida = cv2.bitwise_not(img)
    return img_invertida


def aumenta_contraste(img):
    img_contraste = cv2.convertScaleAbs(img, alpha=2.0, beta=0) 
    return img_contraste

def blur(img):
    img_blur = cv2.GaussianBlur(img, (7, 7), 0)
    return img_blur

def nitidez(img):
    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])

    img_nitidez = cv2.filter2D(img, -1, kernel)
    return img_nitidez

def detecta_bordar(img):
    img_bordas = cv2.Canny(img, 100, 200)
    return img_bordas