""" Author: Cole Howard
Build additional training vectors, which are rotations, skews, and pans, 
of the orginal MNIST dataset
"""

import csv


import numpy as np

from random import randrange

from skimage.transform import rotate

# from matplotlib import pyplot as plt
# from matplotlib import cm

def spin_o_rama(vector, ang):
    vector = rotate(vector, ang, mode='constant')
    return vector

# def visualization(vector):
#     plt.imshow(vector, cmap=cm.Greys_r)
#     plt.axis('off')
#     plt.pause(0.0001)
#     plt.show()


if __name__ == '__main__':
    with open('train.csv', 'r') as f:
        reader = csv.reader(f)
        t = list(reader)
        train = [[int(x) for x in y] for y in t[1:]]

    ans_train = [x[0] for x in train]
    train_set = [x[1:] for x in train]
    ans_train.pop(0)
    train_set.pop(0)

    temp_train = [np.array(elem, dtype=float) for elem in train_set]
    train_set = temp_train

    with open('train_ext.csv', 'w') as g:
        filewriter = csv.writer(g)
        for idx, elem in enumerate(train_set):
            filewriter.writerow([ans_train[idx]] + elem.flatten().tolist())

        for _ in range(5):
            for idx, elem in enumerate(train_set):
                x = elem.reshape((28, 28))
                rand_ang = randrange(-89, 89)
                y = spin_o_rama(x, rand_ang).flatten()
                filewriter.writerow([ans_train[idx]] + y.flatten().tolist())





    # visualization(x)
    # visualization(spin_o_rama(x, 25))