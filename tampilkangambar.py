import cv2

img = cv2.imread("meraw.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar meraw Original", img)
cv2.imshow("Gambar Hasil GrayScale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
