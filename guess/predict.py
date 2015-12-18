""" Accept an array representing a test sample, parse it and pass through
a pre-trained neural net then store results in a pre-existing database
"""
from guess.models import Drawing

from finnegan.img_handler import downsize
from mini_net import run_mnist


def parse_to_test_sample(info):
    """
    Attribues
    ---------
    orig_size : int
        The length of a side of the square html input canvas.
    train_data_size : int
        The length of a side of the square 2d array representing the training
        data.
    """

    orig_size = 194
    train_data_size = 28
    if info != "no info":

        # Split payload into a list of floats and discard the rgb values
        # Alpha channel is used a greyscale value (Every 4th entry from
        # the sketch.js output)

        temp_array = info.split(',')
        img_array = [float(x) for x in temp_array[3::4]]

        # Resize the image to match the size of the network's training
        # data

        small_image = downsize(img_array, orig_size, train_data_size)
        small_image_list = small_image.flatten().tolist()

        # Pass it through the pre-trainedd network and retrieve a guess
        # and confidence

        net_guess = run_mnist(small_image)[0]
        val_guess = net_guess[0]
        net_confidence = round(float(net_guess[1])*100, 2)

    else:
        img_array = None

    Drawing.objects.create(values_array=img_array,
                           guess=val_guess,
                           confidence=net_confidence,
                           tiny_array=small_image_list,
                           correct=False)
