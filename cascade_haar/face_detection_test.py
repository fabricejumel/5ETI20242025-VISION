import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]


# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),

)

print("Found {0} faces!".format(len(faces)))
i=0
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    i=i+1
    cv2.rectangle(image, (x, y), (x+w, y+h), (27*i%256, 255-27*i%256, 27*i%256), 2)


cv2.imshow("Faces found" ,image)
cv2.waitKey(0)


