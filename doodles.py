import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class_names = ['bee', 'butterfly', 'eye', 'mushroom', 'diamond', 'snowman', 'cat', 'popsicle', 'octopus', 'bowtie']

image_size = (28, 28)

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    'images',
    labels='inferred',
    label_mode='int',
    class_names=class_names,
    color_mode='grayscale',
    batch_size=64,
    image_size=image_size,
    seed=123,
    validation_split=0.2,
    subset='training',
)

ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    'images',
    labels='inferred',
    label_mode='int',
    class_names=class_names,
    color_mode='grayscale',
    batch_size=64,
    image_size=image_size,
    seed=123,
    validation_split=0.2,
    subset='validation',
)

img_height = 28
img_width = 28

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(img_height, img_width)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])
  
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])