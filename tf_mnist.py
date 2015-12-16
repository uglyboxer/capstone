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

    dataset = loadmat('training_batches/1.mat')
    ans_train = dataset['affNISTdata']['label_int']
    train_set = dataset['affNISTdata']['image'].transpose() 

    train_set = utils.resample(train_set, random_state=2)
    ans_train = utils.resample(ans_train, random_state=2)

    network = Network(layers, neuron_count, train_set[1])
    network.train(train_set, ans_train, epochs)

    for i in range(2, 10):
        filename = 'training_batches/' + str(i) + '.mat'

        dataset = loadmat(filename)
        ans_train = dataset['affNISTdata']['label_int']
        train_set = dataset['affNISTdata']['image'].transpose() 

        train_set = utils.resample(train_set, random_state=2)
        ans_train = utils.resample(ans_train, random_state=2)

        network.train(train_set, ans_train, epochs)

    dataset = loadmat('training_batches/11.mat')
    ans_train = dataset['affNISTdata']['label_int']
    train_set = dataset['affNISTdata']['image'].transpose()

    guess_list = network.run_unseen(train_set)
    print('Test Set')
    test_report = network.report_results(guess_list, ans_train)

    dataset = loadmat('training_batches/12.mat')
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
    epochs = 1
    layer_list_list = [[24, 22, 18, 16, 14, 12, 10], [500, 250, 200, 170, 100, 80, 10]]
    for run_num, layer_list in enumerate(layer_list_list):
        run_mnist(run_num, epochs, len(layer_list), layer_list)
