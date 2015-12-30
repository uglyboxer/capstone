import csv, pickle
import numpy as np

from sklearn import utils

from affnist_read import loadmat
from finnegan.network import Network

def run_mnist(run_num, epochs=0, layers=0, neuron_count=0):
    """ Run affNIST dataset and output a guess list on test and validation
    sets.  Dumps a pickle of the trained network state and a results file
    for choosing the best parameters.

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

    dataset = loadmat('1.mat')
    ans_train = dataset['affNISTdata']['label_int']
    train_set = dataset['affNISTdata']['image'].transpose()

    dataset2 = loadmat('2.mat')
    ans_train2 = dataset2['affNISTdata']['label_int']
    train_set2 = dataset2['affNISTdata']['image'].transpose()

    ans_train = np.hstack((ans_train, ans_train2))
    train_set = np.vstack((train_set, train_set2))

    network = Network(layers, neuron_count, train_set[1])
    network.train(train_set, ans_train, epochs)


    dataset = loadmat('3.mat')
    ans_train = dataset['affNISTdata']['label_int']
    train_set = dataset['affNISTdata']['image'].transpose()

    guess_list = network.run_unseen(train_set)
    print('Test Set')
    test_report = network.report_results(guess_list, ans_train)

    dataset = loadmat('4.mat')
    ans_train = dataset['affNISTdata']['label_int']
    train_set = dataset['affNISTdata']['image'].transpose()

    guess_list = network.run_unseen(train_set)
    print('Validation Set')
    val_report = network.report_results(guess_list, ans_train)

    file_name = 'finnegan/my_net_' + str(run_num) + '.pickle'
    g = open(file_name, 'wb')
    pickle.dump(network, g, protocol=4)
    g.close()

    file_name_2 = 'finnegan/my_net_report_' + str(run_num) + '.txt'
    h = open(file_name_2, 'w')
    details = 'Neuron Counts: ' + str(neuron_count) + '\n'
    details_2 = 'Test Report: ' + test_report + '\n'
    details_3 = 'Validation Report: ' + val_report + '\n'
    h.write(details)
    h.write(details_2)
    h.write(details_3)
    h.close()

    return None


if __name__ == '__main__':
    epochs = 30
    layer_list_list = [[800, 100, 10]]
    for run_num, layer_list in enumerate(layer_list_list):
        run_mnist(run_num, epochs, len(layer_list), layer_list)
