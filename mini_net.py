import csv, pickle
import numpy as np
from sklearn import datasets, utils

from finnegan.network import Network

# from img_handler import downsize


def run_scikit_digits(vector, epochs=0, layers=0, neuron_count=[]):
    # temp_digits = datasets.load_digits()
    # digits = utils.resample(temp_digits.data, random_state=3)
    # temp_answers = utils.resample(temp_digits.target, random_state=3)
    # num_of_training_vectors = 1250 
    # answers, answers_to_test, validation_answers = temp_answers[:], temp_answers[num_of_training_vectors:num_of_training_vectors+260], temp_answers[num_of_training_vectors+260:]
    # training_set, testing_set, validation_set = digits[:], digits[num_of_training_vectors:num_of_training_vectors+260], digits[num_of_training_vectors+260:]

    # network = Network(layers, neuron_count, training_set[0])
    # network.train(training_set, answers, epochs)
    # f = open('finnegan/my_net.pickle', 'wb')
    # pickle.dump(network, f)
    # f.close()
    fr = open('finnegan/my_net.pickle', 'rb')
    network = pickle.load(fr)
    fr.close()
    return network.run_unseen([vector])

def run_mnist(vector, epochs=0, layers=0, neuron_count=0):
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
    target_values : list
        The possible values for each training vector

    """

    # with open('train.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     t = list(reader)
    #     train = [[int(x) for x in y] for y in t[1:]]


    # ans_train = [x[0] for x in train]
    # train_set = [x[1:] for x in train]
    # ans_train.pop(0)
    # train_set.pop(0)

    # train_set = utils.resample(train_set, random_state=2)
    # ans_train = utils.resample(ans_train, random_state=2)

    # network = Network(layers, neuron_count, train_set[0])
    # network.train(train_set, ans_train, epochs)
    # f = open('finnegan/my_net.pickle', 'wb')
    # pickle.dump(network, f)
    # f.close()
    fr = open('finnegan/my_net_2.pickle', 'rb')
    network = pickle.load(fr)
    fr.close()
    return network.run_unseen([vector])

if __name__ == '__main__':
    epochs = 250
    layers = 3
    layer_list = [75, 73, 10]
    # run_scikit_digits([], epochs, layers, layer_list)
    run_mnist(epochs, layers, layer_list)