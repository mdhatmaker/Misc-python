
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

# import input data module from TF
#from tensorflow.examples.tutorials.mnist import input_data
# !pip install -q git+https://github.com/tensorflow/examples.git
import tensorflow_datasets
mnist_dict = tensorflow_datasets.load('mnist')

### https://medium.com/@lhessani.sa/tensorflow-from-zero-to-hero-solving-a-real-business-case-bebe86a2d132
### http://yann.lecun.com/exdb/mnist/


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)



print(f"TENSOR FLOW VERSION: {tf.__version__}")       # TensorFlow version name
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

mnist = Struct(**mnist_dict)
print(f"\nTRAIN:\n{mnist.train}")    #.train.labels[1044])
print(f"TEST:\n{mnist.test}\n")

#print(len(mnist.train), len(mnist.test))

