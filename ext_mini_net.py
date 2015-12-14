import csv, pickle
import numpy as np

from sklearn import utils

from finnegan.network import Network

def run_mnist(run_num, epochs=0, layers=0, neuron_count=0):
    """ Run Mnist dataset and output a guess list on the Kaggle test_set

    Parameters
    ----------
    epochs : int
        Number of iterations of the the traininng loop for the whole dataset
    layers : int
        Number of layers (not counting the input layer, but does count output
        layer)
    neuron_count : list
        The number of neurons in each of the layers (in order), does not count
        the bias term

    Attributes
    ----------

    """
    ans_train = []
    train_set = []

    with open('../home/train.csv', 'r') as f:
        reader = csv.reader(f)
        t = list(reader)
        train = [[int(x) for x in y] for y in t[1:]]


    ans_train = [x[0] for x in train]
    train_set = [x[1:] for x in train]
    ans_train.pop(0)
    train_set.pop(0)

    train_set = utils.resample(train_set, random_state=2)
    ans_train = utils.resample(ans_train, random_state=2)

    network = Network(layers, neuron_count, train_set[1])
    network.train(train_set, ans_train, epochs)

    for i in range(1, 3):
        filename = '../home/train_' + str(i) + '.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            t = list(reader)
            train = [[int(x) for x in y] for y in t[1:]]


        ans_train = [x[0] for x in train]
        train_set = [x[1:] for x in train]
        ans_train.pop(0)
        train_set.pop(0)

        train_set = utils.resample(train_set, random_state=2)
        ans_train = utils.resample(ans_train, random_state=2)

        network.train(train_set, ans_train, epochs)

    with open('../home/train_3.csv', 'r') as f:
        reader = csv.reader(f)
        t = list(reader)
        train = [[int(x) for x in y] for y in t[1:]]

    ans_train = [x[0] for x in train]
    train_set = [x[1:] for x in train]
    ans_train.pop(0)
    train_set.pop(0)
    guess_list = network.run_unseen(train_set)
    print('Test Set')
    network.report_results(guess_list, ans_train)
    

    file_name = 'finnegan/my_net_' + str(run_num) + '.pickle'
    g = open(file_name, 'wb')
    pickle.dump(network, g, protocol=4)
    g.close()
    return None


if __name__ == '__main__':
    epochs = 1
    layer_list_list = [[25, 28, 10]]
    # layer_list_list = [[85, 82, 81, 10], [52, 81, 10], [110, 108, 10],
    #                    [90, 60, 42, 10], [125, 123, 10], [42, 41, 40, 39, 10]]
    for run_num, layer_list in enumerate(layer_list_list):
        run_mnist(run_num, epochs, len(layer_list), layer_list)
