import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('bTS.jpg')
# determinar el tipo de imagen
print(type(img))
# mostrar pixeles
print(img.shape)
# mostrando imagen en ventana barra de titulo bTS 0037
cv2.imshow('bTS.jpg 0037', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()

# imagen pequena
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# mostrar imagen en ventana con imshow
cv2.imshow('Img peque 0037', small)
## tiempo de espera
cv2.waitKey(0)
# destruir las ventanas
cv2.destroyAllWindows()

print(small.shape)
# <'class numpy.ndarray'>
# (554, 554, 3)
# (277, 277, 3)
small[0,0]
# en la posicion [0,0] los valores [255,255,255]
small[0,0] = (255,255,255)
print(small[0,0])

cv2.imshow('img final 0037', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

# otra forma
small[0:100,0:10] = (0,0,255)
cv2.imshow('Img F M 0037', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imagen en gris}
gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
# aqui modifica en gris
print(gray.shape)

cv2.imshow('Img Gris 0037', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

