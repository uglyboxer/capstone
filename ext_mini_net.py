import pickle
import numpy as np

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

    with open('train_ext.txt', 'r') as f:
        for line in f:
            ans_train.append(line[0])
            train_set.append(line[1])

    train_set = utils.resample(train_set, random_state=2)
    ans_train = utils.resample(ans_train, random_state=2)

    network = Network(layers, neuron_count, train_set[0])
    network.train(train_set[:91000], ans_train[:91000], epochs)

    guess_list = network.run_unseen(train_set[91000:])
    network.report_results(guess_list, ans_train[91000:])
    
    file_name = 'finnegan/my_net_' + str(run_num) + '.pickle'
    g = open(file_name, 'wb')
    pickle.dump(network, g)
    g.close()
    return None


if __name__ == '__main__':
    epochs = 250
    layer_list_list = [[75, 73, 10], [85, 82, 81, 10], [65, 63, 62, 61, 10],
                       [64, 63, 10], [35, 34, 34, 32, 28, 10], [52, 81, 10]]
    for run_num, layer_list in enumerate(layer_list_list):
        run_mnist(run_num, epochs, len(layer_list), layer_list)
