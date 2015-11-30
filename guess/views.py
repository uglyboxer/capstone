from django.shortcuts import render, redirect
from django.http import HttpResponse
from guess.models import Drawing

from finnegan.img_handler import downsize
from mini_net import run_scikit_digits

import logging


logging.basicConfig(filename='badness.log',level=logging.DEBUG)
logger = logging.getLogger(__name__)

def home_page(request):
    return render(request, 'home.html', {'info': 'dummy'})


def parse_data(request):
    if request.method == "POST":
        info = request.POST.get('payload', 'no info')
        if info != "no info":
            temp_array = info.split(',')
            img_array = [float(x) for x in temp_array[3::4]]
            small_image = downsize(img_array, 128, 8)
            try:
                net_guess = run_scikit_digits(small_image)
            except:
                logger.exception('Why oh why?')
                return render(request, 'holder.html', {'info': 88})


        else:
            img_array = None

        Drawing.objects.create(values_array=img_array, guess=net_guess[0])
        return render(request, 'holder.html', {'info': net_guess[0]})
    return render(request, 'holder.html', {'info': 'x'})

def show_data(request):

    return redirect('home')