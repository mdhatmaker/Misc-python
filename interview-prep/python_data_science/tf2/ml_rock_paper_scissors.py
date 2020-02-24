# machine learning: rock, paper, scissors
import tensorflow as tf
import numpy as np
import sys


### https://youtu.be/MyYPpmVPed0
### https://www.tensorflow.org/datasets/catalog/rock_paper_scissors
### http://www.laurencemoroney.com/rock-paper-scissors-dataset/
### https://rubikscode.net/2019/04/22/ultimate-guide-to-tensorflow-2-0-in-python/


def convolutions_demo():
    # Convolutions to identify image features (3 x 3 pixel area)
    pixel_values = np.array([[0, 64, 128], [48, 192, 144], [142, 226, 168]])
    print(np.shape(pixel_values))
    conv1 = np.array([[-1, 0, -2], [.5, 4.5, -1.5], [1.5, 2, -3]])
    conv2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # vertical lines
    conv3 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # horizontal lines
    mult1 = pixel_values * conv1
    print(mult1)
    print(np.sum(mult1))
    #print((-1*0)+(0*64)+(-2*128)+(.5*48)+(4.5*192)+(-1.5*144)+(1.5*42)+(2*226)+(-3*168))

def max_pooling_demo():
    # Max Pooling to compress images (2 x 2 pixel area)
    pixel_values = np.array([[0, 64, 128, 128], [48, 192, 144, 144], [142, 226, 168, 0], [255, 0, 0, 64]])
    p1 = np.max(np.array([[0, 64], [48, 192]]))
    p2 = np.max(np.array([[128, 128], [144, 144]]))
    p3 = np.max(np.array([[142, 226], [255, 0]]))
    p4 = np.max(np.array([[168, 0], [0, 64]]))
    pooled_values = np.array([[p1, p2], [p3, p4]])
    print(pooled_values)


model1 = tf.keras.models.Sequential([
    # inputs to neural network (150x150 images x3 color depth)
    tf.keras.layers.Flatten(input_shape=(150, 150, 3)),
    # consider this to be 512 functions (in middle layer?)
    tf.keras.layers.Dense(512, activation='relu'),
    # output 3 "neurons" from neural network (3 outputs i.e. rock, paper, scissors)
    tf.keras.layers.Dense(3, activation='softmax')
])

# multiple layers of convolution followed by pooling
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.summary()

# loss function determines how well/badly we did in predicting
# based on loss, optimizer function generates the next guess
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

history = model.fit_generator(train_generator, epochs=25, validation_data=validation_generator, verbose=1)

model.fit(..., epochs=100)


#sys.exit()



