import tensorflow as tf
import numpy as np
from PIL import Image
from quickdraw import QuickDrawDataGroup

class_names = ['bee', 'bowtie', 'butterfly', 'cat', 'diamond', 'eye', 'mushroom', 'octopus', 'popsicle', 'snowman']



test_image = Image.open('download (2).png')
test_image = test_image.resize((28,28))
test_image.save("temp.png")
test_image.show()

test_image = tf.keras.preprocessing.image.load_img('temp.png', color_mode="grayscale", target_size=(28, 28))
test_image = tf.keras.preprocessing.image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0) # add an extra dimension for batch size

model = tf.keras.models.load_model('models/model.h5')

predictions = model.predict(test_image)
predicted_classes = np.argmax(predictions, axis=1)
predictions_percentage = predictions*100
predictions_percentage = np.round(predictions_percentage, 2)

predicted_class = class_names[predicted_classes[0]]
confidence = predictions_percentage[0][predicted_classes[0]]

print("Model is predicting class " + predicted_class + " with " + str(confidence) + "% confidence.")
