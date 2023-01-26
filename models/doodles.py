import tensorflow as tf
import numpy as np

class_names = ['bee', 'bowtie', 'butterfly', 'cat', 'diamond', 'eye', 'mushroom', 'octopus', 'popsicle', 'snowman']

image_size = (28, 28)

dataset_dir = 'images'

batch_size = 32

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size
)

ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    color_mode="grayscale",
    image_size=image_size,
    batch_size=batch_size
)

input_shape = (28, 28, 1)

model = tf.keras.Sequential([
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(6, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.Conv2D(8, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.Conv2D(10, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(800, activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(600, activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), metrics=['accuracy'])

model.fit(ds_train, validation_data=ds_validation, epochs=10, verbose=1)
model.evaluate(ds_validation)
model.save('models/model.h5')