import pickle

def create_net():
    fr = open('finnegan/my_net_2.pickle', 'rb')
    network = pickle.load(fr)
    fr.close()
    return

