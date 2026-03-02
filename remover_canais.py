import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('entrada.jpg')

# Cópias para cada filtro 
azul_zerado = imagem.copy()
verde_zerado = imagem.copy()
vermelho_zerado = imagem.copy()

# Manipulação da Matriz 
# Canal 0 = Azul; Canal 1 = Verde; Canal 2 = Vermelho

# Remover Azul 
azul_zerado[:, :, 0] = 0

# Remover Verde 
verde_zerado[:, :, 1] = 0

# Remover Vermelho 
vermelho_zerado[:, :, 2] = 0

# Resultados salvos
cv2.imwrite('monalisa_sem_azul.jpg', azul_zerado)
cv2.imwrite('monalisa_sem_verde.jpg', verde_zerado)
cv2.imwrite('monalisa_sem_vermelho.jpg', vermelho_zerado)

print("Imagens processadas e salvas com sucesso!")