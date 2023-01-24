import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class_names = ['bee', 'butterfly', 'eye', 'mushroom', 'diamond', 'snowman', 'cat', 'popsicle', 'octopus', 'bowtie']

image_size = (28, 28)

tf.keras.preprocessing.image.load_img()

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    'images',
    labels='inferred',
    label_mode='int',
    class_names=class_names,
    color_mode='grayscale',
    batch_size=32,
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
    batch_size=32,
    image_size=image_size,
    seed=123,
    validation_split=0.2,
    subset='validation',
)

img_height = 28
img_width = 28

plt.figure(figsize=(8, 8))
for images, labels in ds_train.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        data = images[i].numpy().astype("uint8")
        plt.imshow(data, cmap='gray', vmin=0, vmax=255)
        plt.title(ds_train.class_names[labels[i]])
        plt.axis("off")
        plt.show()

"""model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), padding="same", activation="relu", input_shape=(img_height, img_width, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(128, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(ds_train, validation_data=ds_validation, epochs=25, verbose=1)
model.evaluate(ds_validation)
model.save('models/model.h5')"""