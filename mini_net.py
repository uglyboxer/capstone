import pickle
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

if __name__ == '__main__':
    epochs = 250
    layers = 3
    layer_list = [36, 34, 10]
    run_scikit_digits([], epochs, layers, layer_list)