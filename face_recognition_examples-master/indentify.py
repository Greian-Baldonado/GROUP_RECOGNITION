import face_recognition
from PIL import Image, ImageDraw

image_of_baldonado = face_recognition.load_image_file('./img/known/BALDONADO.jpg')
baldonado_face_encoding = face_recognition.face_encodings(image_of_baldonado)[0]

image_of_cometa = face_recognition.load_image_file('./img/known/COMETA.jpg')
cometa_face_encoding = face_recognition.face_encodings(image_of_cometa)[0]

image_of_mui = face_recognition.load_image_file('./img/known/MUI.jpg')
mui_face_encoding = face_recognition.face_encodings(image_of_mui)[0]

image_of_muro = face_recognition.load_image_file('./img/known/MURO.jpg')
muro_face_encoding = face_recognition.face_encodings(image_of_muro)[0]

image_of_santos = face_recognition.load_image_file('./img/known/santos.jpg')
santos_face_encoding = face_recognition.face_encodings(image_of_santos)[0]

#  Create arrays of encodings and names
known_face_encodings = [
  baldonado_face_encoding,
  cometa_face_encoding,
  mui_face_encoding,
  muro_face_encoding,
  santos_face_encoding,
]

known_face_names = ["Baldonado", "Cometa", "Mui", "Muro", "Santos"]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/groups/B_C_M_M_S.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=("Black"), width=2)

 #Draw label 
  text_width = 20
  text_height = 5
  #text_width, text_height == draw.textsize(name)
  #draw.text((500, 100), name) 
  draw.rectangle(((left,bottom - text_height - 5), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('ELECTIVE MATITIKAS.jpg')