# finnegan
## by Cole Howard

A custom neural net for recoginzing handwritten digits, with a serious nod to [I Am Trask](http://iamtrask.github.io/2015/07/12/basic-python-network/).  The neural net is pre-trained on the MNIST dataset (run on an AWS instance).  And the user input is rescaled and tested.

[![Build Status](https://travis-ci.org/uglyboxer/capstone.svg?branch=master)](https://travis-ci.org/uglyboxer/capstone) [![Documentation Status](https://readthedocs.org/projects/capstone/badge/?version=latest)](http://capstone.readthedocs.org/en/latest/?badge=latest)


sketch.js is a library created by [Michael Bleigh](http://intridea.github.io/sketch.js/) to allow the user to draw the image of a digit.  It has been modified to pull a drawn image from the page before being resized and sent to the neural network for classifaciton.

## TODO

- Analize Results
- Analize correlation of misclassification and actual numbers (7's tend to be classified as 2, etc.)
- Train net on rotated images for more robust recognition
- Visualizations of each layer of the net (in d3 or bokeh)
- Provide a selection of neural net architectures to allow a user to swap out and see the different vizualations and results.  (Results data will be stored by specific architecture.)



## To Get Started

Navigate to: [Finnegan](https:uglyboxer.pythonanywhere.com)


The baseline architecture for the net is on Github, [here](http://uglyboxer.github.io/finnegan/), and the code for the webapp (including Finnegan) be found [here](https://github.com/uglyboxer/capstone).

Full documentation hosted [here](http://capstone.rtfd.org)

To adjust hyper-parameters or choose dataset:
Open net_launch.py and adjust as needed at the bottom of the file.  The dataset can be switched by commenting out the appropriate line at the bottom and uncommneting the other.  Or simply:

```
from Network import network
```

And feed it the appropriate parameters.