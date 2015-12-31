****************************************
Finnegan - An Exploration in Neural Nets
****************************************

========
Overview
========

Finnegan is a basic multi-class neural net classifier.  It is designed to be trained with any labled dataset, and then make predictions (classifications) on unseen, similar examples.

A front end user experience, in the form of a web app is provided around the task of classifying handwritten digits (0-9).  To try: navigate `here <http://uglyboxer.pythonanywhere.com>`_ in a browser.

The webapp uses django and boostrap to serve a javascript page to collect the handwriting sample.  On the backend the server parses the drawing to a greyscale image and then uses the pixel values as the input vector to the neural net.

The neural net in the webapp is pre-trained (as real time training would be impractical from the perspective of a user's time).

The pre-training was done on the MNIST dataset, a set of 60,000 handwritten digit examples.  Each a 28px by 28px greyscale image.  The architecture of the net was chosen by running the helper function "ext_mini_net.py" to iterate over many possible combinations of layer sizes (number of neurons) and number of layers.  The most successful of those runs against a validation set were chosen and the state of that trained network was "pickled" using Python Pickle.  

The webapp reinstantiates that trained network and runs the user's sample resized (see this `post <http://uglyboxer.github.io/machine%20learning/neural%20net/python/mnist/scikit-image/2015/12/26/smaller.html>` on my blog for deatails on that).  It then makes a guess as to which digit it is.  It also provides a confidence and requests feedback from the user on the validity of the guess.  The data surrounding each submission is stored in a PostgreSQL database: image, resized image, guess, confidence, correct/incorrect, actual digit (if guess was incorrect).

Lastly, a statistic page is provided for the overall performance of the classifier.

============
Requirements
============

Basic Neural Network Needs

- Scipy
- Numpy
- Scikit-learn (for randomize dataset, or using their handwritten, smaller digits)

Webapp Needs (in addition to above)

- Django
- Bootstrap
- PosgreSQL

=====
Usage
=====

To run the webapp locally, clone the `repo <https://github.com/uglyboxer/capstone>`_.

You will need to setup a PostgreSQL database and point the app to it in:
capstone/net/settings.py

Then from the capstone directory::

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

This will serve the page on localhost:8000.  Navigate your browser there and enjoy.

To use the Finnegan network separately, from capstone/finnegan::

    from network import Network

Create an instance from the class::

    net = Network(layers, neuron_count, vector)

Where:
- layers is number of layers including the output layer
- neuron_count is a list of integers representing the number of neurons per layer, with the output layer being the last in the list (and therefor should be the total number of possible classifications).
- vector is a sample input vector (for determining size and shape)

Then::

    net.train(dataset, answers, epcohs)
    guesses = net.run_unseen(test_dataset)
    net.report_results(guesses, test_answers)

Will train the net, and provide a report on the success of guessing against the test set.

================
Acknowledgements
================

sketch.js is a javascript/jquery tool for capturing user input on an html canvas.  Borrowed and modified from `here <http://intridea.github.io/sketch.js/>`_.

The blog `I Am Trask <http://iamtrask.github.io/2015/07/12/basic-python-network/>`_ provided me with the key insight to vectorize each layer as a single unit and thereby get rid of the for loops as that took FOREVER to run.
