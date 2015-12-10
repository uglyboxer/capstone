from django.http import HttpResponse
from django.shortcuts import render, redirect

import numpy as np

from guess.models import Drawing

from finnegan.img_handler import downsize, visualization
from mini_net import run_mnist

import logging


logging.basicConfig(filename='badness.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def home_page(request):
    return render(request, 'home.html')


def parse_data(request):
    """ As a request comes from the home page via POST, parse the canvas
    image, downsize it to match the dims of the training data, and then
    pass it to the pre-trained neural network for it make a prediction.

    The results of the prediction (value and confidence), as well as the
    array representations of the images themselves are stored in the
    model, and hence the PostgresQL database.

    Attribues
    ---------
    orig_size : int
        The length of a side of the square html input canvas.
    train_data_size : int
        The length of a side of the square 2d array representing the training
        data.
    """

    orig_size = 194
    train_data_size =28

    try:
        if request.method == "POST":
            info = request.POST.get('payload', 'no info')
            if info != "no info":
                temp_array = info.split(',')
                img_array = [float(x) for x in temp_array[3::4]]
                small_image = downsize(img_array, orig_size, train_data_size)
                small_image_list = small_image.flatten().tolist()
                try:
                    net_guess = run_mnist(small_image)[0]
                    val_guess = net_guess[0]
                    net_confidence = round(float(net_guess[1])*100, 2)

                except:
                    return render(request, 'home.html')

            else:
                img_array = None

            Drawing.objects.create(values_array=img_array,                               
                                   guess=val_guess,
                                   confidence=net_confidence,
                                   tiny_array=small_image_list,
                                   correct=False)
            return HttpResponse()
    except:
        logger.exception('New way')
        logger.info(net_confidence)
    return render(request, 'holder.html', {'info': net_confidence})


def show_data(request):
    """ Sends a render of image as drawn and the network's guess and
    confidence via the report template.

    Attribues
    ---------
    drawing_obj : Drawing model instance
      The last line from the database (specifically the most recent entry).

    """
    drawing_obj = Drawing.objects.all().order_by('id').reverse()[0]
    return render(request, 'report.html', {'drawing_obj': drawing_obj})


def valid_info(request):
    """ Stores the users validation (or dis-validation) of the network's
    guess in the database along with what the user intended it to be, in the
    case of an incorrect guess.

    """
    obj = Drawing.objects.all().order_by('-id')[0]
    if request.method == "POST":
        if request.POST["valid"] == "correct":
            obj.correct = True
            obj.save()
        else:
            obj.correct = False
            obj.actual = request.POST["actual"]
            obj.save()

    return redirect('/')


def about(request):
    return redirect("https://github.com/uglyboxer")


def contact(request):
    return redirect("https://github.com/uglyboxer")
