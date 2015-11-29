from django.shortcuts import render, redirect
from django.http import HttpResponse
from guess.models import Drawing


def home_page(request):
    return render(request, 'home.html', {'info': 'dummy'})


def parse_data(request):
    if request.method == "POST":
        info = request.POST.get('payload', 'no info')
        if info != "no info":
            temp_array = info.split(',')
            img_array = [float(x) for x in temp_array[3::4]]
        else:
            img_array = None
        # Run data thru network here
        Drawing.objects.create(values_array=img_array, guess='12')
        return render(request, 'holder.html', {'info': img_array})
    return render(request, 'holder.html', {'info': 'x'})

def show_data(request):

    return render(request, 'home.html', {'info': 'still a dummy'})