import tensorflow as tf
import numpy as np
from quickdraw import QuickDrawDataGroup

data = QuickDrawDataGroup('cat', recognized=True)

drawing = data.get_drawing()
image = drawing.image
image.save('cat.png')

class_names = ['bee', 'bowtie', 'butterfly', 'cat', 'diamond', 'eye', 'mushroom', 'octopus', 'popsicle', 'snowman']

test_image = 'Untitled.png'

test_image = tf.keras.preprocessing.image.load_img(test_image, color_mode="grayscale", target_size=(28, 28))
test_image = tf.keras.preprocessing.image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0) # add an extra dimension for batch size

model = tf.keras.models.load_model('models/model.h5')

predictions = model.predict(test_image)
predicted_classes = np.argmax(predictions, axis=1)
predictions_percentage = predictions*100
predictions_percentage = np.round(predictions_percentage, 2)

print(predictions_percentage)
print("Model is predicting: " + class_names[predicted_classes[0]])
