import cv2  
image = cv2.imread("C:\\Users\\lenovo\\Documents\\GitHub\\DeepFake-Detection-Face-Swap-Detection-Face-Blur-Level-Detection-\\293293_faces.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        gray,
scaleFactor=1.3,
minNeighbors=3,
minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    ...
status = cv2.imwrite('faces_detected.png', image)

print("[INFO] Image faces_detected.png written to filesystem: ")
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
roi_color = image[y:y + h, x:x + w] 
    print("[INFO] Object found. Saving locally.") 
    cv2.imwrite(str(w) + str(h) + '_faces.png', roi_color) 


value = cv2.Laplacian(gray, cv2.CV_64F).var()
print(value)  
if value < 5:
print("Image blurry")  
else: 
print("not blurry")

cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
