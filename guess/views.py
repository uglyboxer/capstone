from django.shortcuts import render
from django.http import HttpResponse
from guess.models import Drawing

from finnegan.img_handler import downsize
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
                try:
                    net_guess = run_mnist(small_image)[0]

                except:
                    logger.exception('Why oh why?')
                    return render(request, 'holder.html', {'info': 88})

            else:
                img_array = None

            Drawing.objects.create(values_array=img_array, guess=net_guess)
            return HttpResponse()
    except:
        logger.exception('New way')
        logger.info(request.POST.get('payload'))
    return render(request, 'holder.html', {'info': 'x'})


def show_data(request):

    net_guess = Drawing.objects.all().order_by('id').reverse()[0].guess
    return render(request, 'report.html', {'guess': net_guess})
