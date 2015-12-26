import csv
import numpy as np
import psycopg2

from matplotlib import cm
from matplotlib import pyplot as plt


def visualization(vector, vector2, vector_name=0):
    y = np.reshape(vector, (28, 28))
    fig = plt.figure()
    a = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(y, cmap=cm.Greys_r)
    # plt.suptitle(vector_name)
    a = fig.add_subplot(1, 2, 2)
    z = np.reshape(vector2, (28, 28))  
    imgplot = plt.imshow(z, cmap=cm.Greys_r)

    plt.show()


def db_connect():
    conn_string = "host='localhost' dbname='netdb' user='postgres' password='postgres'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT tiny_array FROM guess_drawing where id=669")
    return cursor.fetchall()

def mnist():
    ans_train = []
    train_set = []

    with open('train.csv', 'r') as f:
        reader = csv.reader(f)
        t = list(reader)
        train = [[int(x) for x in y] for y in t[1:]]

    ans_train = [x[0] for x in train]
    train_set = [x[1:] for x in train]
    ans_train.pop(0)
    train_set.pop(0)
    idx = ans_train.index(6)
    return train_set[idx]


if __name__ == '__main__':
    vector = db_connect()[0][0]
    vector2 = mnist()
    visualization(vector, vector2)