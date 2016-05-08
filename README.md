# finnegan
## by Cole Howard

A custom neural net for recoginzing handwritten digits, with a serious nod to [I Am Trask](http://iamtrask.github.io/2015/07/12/basic-python-network/).  The neural net is pre-trained on the MNIST dataset (run on an AWS instance).  And the user input is rescaled and tested.

[![Build Status](https://travis-ci.org/uglyboxer/capstone.svg?branch=master)](https://travis-ci.org/uglyboxer/capstone) [![Documentation Status](https://readthedocs.org/projects/capstone/badge/?version=latest)](http://capstone.readthedocs.org/en/latest/?badge=latest)


sketch.js is a library created by [Michael Bleigh](http://intridea.github.io/sketch.js/) to allow the user to draw the image of a digit.  It has been modified to pull a drawn image from the page before being resized and sent to the neural network for classifaciton.


## To Get Started

Requires running PostgreSQL server.  Create a new database named 'netdb'
```
createdb netdb
```
Clone the repo locally, then install the requirements:
```
pip install -r requirements.txt
python3 manage.py loaddata guess/fixtures/initial_data.json
python3 manage.py runserver
```

Then navigate to localhost:8000 on your browser and draw away1

The baseline architecture for the net is on Github, [here](http://uglyboxer.github.io/finnegan/), and the code for the webapp (including Finnegan) be found [here](https://github.com/uglyboxer/capstone).

Full documentation hosted [here](http://capstone.rtfd.org)

To adjust hyper-parameters or choose dataset:
Open net_launch.py and adjust as needed at the bottom of the file.  The dataset can be switched by commenting out the appropriate line at the bottom and uncommneting the other.  Or simply:

```
from Network import network
```

And feed it the appropriate parameters.
