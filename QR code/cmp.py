
import face_recognition
import os

known_image = face_recognition.load_image_file("img1.jpg")
lf = os.listdir("C:\Users\Rajat\Desktop\Project\module 1")

for img in lf:
	unknown_image = face_recognition.load_image_file(img)

	biden_encoding = face_recognition.face_encodings(known_image)[0]
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

	results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
	print(results)




