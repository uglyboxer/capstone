from django.shortcuts import render, redirect
from django.http import HttpResponse
from guess.models import Drawing
import numpy as np

from finnegan.img_handler import downsize, visualization
from mini_net import run_mnist

import logging


logging.basicConfig(filename='badness.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def home_page(request):
    return render(request, 'home.html')


def parse_data(request):
    try: 
        if request.method == "POST":
            info = request.POST.get('payload', 'no info')
            if info != "no info":
                temp_array = info.split(',')
                img_array = [float(x) for x in temp_array[3::4]]
                small_image = downsize(img_array, 194, 28)
                small_image_list = small_image.flatten().tolist()
                try:
                    net_guess = run_mnist(small_image)[0]
                    val_guess = net_guess[0]
                    net_confidence = round(float(net_guess[1])*100, 2)

                except:
                    return render(request, 'holder.html', {'info': 88})

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

    drawing_obj = Drawing.objects.all().order_by('id').reverse()[0]
    return render(request, 'report.html', {'drawing_obj': drawing_obj})


def valid_info(request):
    obj = Drawing.objects.all().order_by('-id')[0]
    if request.method == "POST":
        if request.POST["valid"] == "correct":
            obj.correct = True
            obj.save()
        else:
            obj.correct = False
            obj.save()

    return redirect('/')

def about(request):
    return redirect("https://github.com/uglyboxer")

def contact(request):
    return redirect("https://github.com/uglyboxer")
