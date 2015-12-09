# finnegan
## by Cole Howard

A custom neural net with a serious nod to [I Am Trask](http://iamtrask.github.io/2015/07/12/basic-python-network/) for recoginzing handwritten digits.  The neural net is pre-trained on the MNIST dataset (run on an AWS instance).  And the user input is rescaled and tested.


## TODO

- Correct button layout
- Add option to enter correct value (on an incorrect guess), to collect specific data on accuracy
- Visualizations of each layer of the net (in d3 or bokeh)
- Provide a selection of neural net architectures to allow a user to swap out and see the different vizualations and results.  (Results data will be stored by specific architecture.)



## To Get Started

Navigate to: [Finnegan](https:uglyboxer.pythonanywhere.com)


The baseline architecture for the net is at [Github](http://uglyboxer.github.io/finnegan/)

To adjust hyper-parameters or choose dataset:
Open net_launch.py and adjust as needed at the bottom of the file.  The dataset can be switched by commenting out the appropriate line at the bottom and uncommneting the other.  Or simply:

```
from Network import network
```

And feed it the appropriate parameters.