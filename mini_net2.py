
# from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D


from skimage.util import pad

import theano

import numpy as np


import os
os.environ['THEANO_FLAGS'] = 'mode=FAST_RUN,device=gpu,floatX=float32'
print(theano.config.device)
np.random.seed(1337)  # for reproducibility

batch_size = 128
nb_classes = 10
nb_epoch = 3

# input image dimensions
img_rows, img_cols = 40, 40
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3


def padwithtens(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 0
    vector[-pad_width[1]:] = 0
    return vector


def initialize_model():
    print("loading model")
    model = Sequential()

    model.add(Convolution2D(nb_filters, nb_conv, nb_conv,
                            border_mode='valid',
                            input_shape=(1, img_rows, img_cols)))
    model.add(Activation('relu'))
    model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adadelta')

    print("loading weights")
    model.load_weights('results1/my_model_weights.h5')
    return model


def run_test(vector):
    model = initialize_model()
    testX = np.array(vector).reshape(40, 40)
    testX = pad(testX, 6, padwithtens).flatten()
    testX = testX.reshape(1, 1, img_rows, img_cols)
    testY = model.predict_classes(testX, verbose=2)
    return testY
