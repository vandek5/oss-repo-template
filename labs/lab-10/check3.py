from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100 * np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def load_image(image_file):
    im = Image.open(image_file)
    np_im = np.array(im)
    return np_im



print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

(_, _), (_, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

test_images = np.array([
    load_image('proc-img/bag.jpg'),
    load_image('proc-img/shirt.jpg'),
    load_image('proc-img/trousers.jpg')
])
test_labels = [8, 6, 1]
test_images = test_images / 255.0

model = tf.keras.models.load_model('my_model')

# test_loss, test_acc = model.evaluate(test_images, np.array([8,6,1]), verbose=2)
#
# print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)


num_rows = 1
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
img_start = 0
for i in range(img_start, img_start + num_images):

    plt.subplot(num_rows, 2 * num_cols, 2 * (i-img_start) + 1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(num_rows, 2 * num_cols, 2 * (i-img_start) + 2)
    plot_value_array(i, predictions[i], test_labels)
plt.show()
