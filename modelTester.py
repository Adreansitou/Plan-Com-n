import os
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps 
import numpy as np
import time

np.set_printoptions(suppress=True) # Disable scientific notation for clarity
model = load_model('model/keras_model.h5', compile=False)
class_names = open("labels.txt", "r").readlines()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

carpeta = "C:\\Users\\ftorr\\Downloads\\converted_keras\\imagenes"
archivos = os.listdir(carpeta)

score = 0
count = 1

start_time = time.time()

for archivo in archivos:
    image = Image.open("imagenes/" + archivo).convert("RGB") 

    #normalization
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    #prediction
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    predicted = str(class_name[2:-1])
    predicted = "Aluminium Cans" if predicted == "Aluminiuns cans" else predicted
    label = str(archivo[:-5])
    print("\n\n           Image:", count, archivo)
    print("       Predicted:", predicted)
    print("           Label:", label)
    print("Confidence Score:", confidence_score)
    if predicted == label:
        score += 1
    print("     Total Score:", score)
    count +=1

end_time = time.time()
inference_time = end_time - start_time

print(f"\n\nTiempo total de inferencia: {inference_time} segundos")

print("\n\n\nThe Model Score is:", str(score) + f"/{count - 1}!")
print("\nThe Success Probability is:", int(score) / (count