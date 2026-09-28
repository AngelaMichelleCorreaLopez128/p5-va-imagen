import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('ariaNA.jfif')
# determinar el tipo de imagen
print(type(img))
# mostrar pixeles
print(img.shape)
# mostrando imagen en ventana barra de titulo ariaNA 0037
cv2.imshow('ariaNA 0037', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()