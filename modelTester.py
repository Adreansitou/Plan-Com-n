import os
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import time

np.set_printoptions(suppress=True)

model = load_model('model/keras_model.h5', compile=False)
class_names = open("labels.txt", "r").readlines()

carpeta = "C:\\Users\\ftorr\\Downloads\\converted_keras\\imagenes"
archivos = os.listdir(carpeta)

batch_size = 32  
image_size = (224, 224)  
score = 0
count = 1

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, image_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    return normalized_image_array

start_time = time.time()
for i in range(0, len(archivos), batch_size):
    batch_files = archivos[i:i+batch_size]
    batch_data = np.ndarray(shape=(len(batch_files), 224, 224, 3), dtype=np.float32)

    for j, archivo in enumerate(batch_files):
        image_path = os.path.join(carpeta, archivo)
        batch_data[j] = preprocess_image(image_path)

    predictions = model.predict(batch_data)

    for k, archivo in enumerate(batch_files):

        index = np.argmax(predictions[k])
        predicted_class = class_names[index].strip() 

        true_class = archivo[:-5]  

        confidence_score = predictions[k][index]

        print(f"\n\n           Image: {count}, {archivo}")
        print(f"       Predicted: {predicted_class}")
        print(f"           Label: {true_class}")
        print(f"Confidence Score: {confidence_score:.4f}")

        if predicted_class.lower() == true_class.lower():
            score += 1
        print(f"     Total Score: {score}")
        count += 1

end_time = time.time()
print(f"\n\nTiempo total de inferencia: {end_time - start_time:.2f} segundos")

print(f"\n\n\nThe Model Score is: {score}/{count - 1}!")
print(f"\nThe Success Probability is: {score / (count - 1):.2%}")
