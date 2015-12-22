import csv, pickle
# import numpy as np

# from sklearn import utils

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

    with open('train.csv', 'r') as f:
        reader = csv.reader(f)
        t = list(reader)
        train = [[int(x) for x in y] for y in t[1:]]

    ans_train = [x[0] for x in train]
    train_set = [x[1:] for x in train]
    ans_train.pop(0)
    train_set.pop(0)

    network = Network(layers, neuron_count, train_set[1])
    network.train(train_set[:37800], ans_train[:37800], epochs)

    guess_list = network.run_unseen(train_set[37800:])
    print('Test Set')
    test_report = network.report_results(guess_list, ans_train[37800:])    

    file_name = 'finnegan/my_net_' + str(run_num) + '.pickle'
    g = open(file_name, 'wb')
    pickle.dump(network, g, protocol=4)
    g.close()

    file_name_2 = 'finnegan/my_net_report_' + str(run_num) + '.txt'
    h = open(file_name_2, 'w')
    details = 'Neuron Counts: ' + str(neuron_count) + '\n'
    details_2 = 'Test Report: ' + test_report + '\n'
    h.write(details)
    h.write(details_2)
    h.close()

    return None


if __name__ == '__main__':
    epochs = 20
    layer_list_list = [[250, 10], [225, 10]]
    # layer_list_list = [[300, 10]91, [85, 82, 81, 10]bunk, [52, 81, 10]91, [80, 79, 10]87, 
    #                    [40, 38, 36, 34, 10], [600, 10]]
    for run_num, layer_list in enumerate(layer_list_list):
        run_mnist(run_num, epochs, len(layer_list), layer_list)
