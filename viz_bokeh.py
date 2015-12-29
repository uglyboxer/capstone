""" Author: Cole Howard
Creates a bokeh friendly array and plots it to an html file (and opens it)

As an example, if executed as main, it pulls an example from netdb and renders
that.
"""
from collections import OrderedDict
from math import sqrt
import pickle

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
import numpy as np

from finnegan.network import Network
from viz_test import db_connect


def convert_np_to_bokeh(vector):
    """ Takes a numpy 2d array and converts it to something Bokeh can plot

    Parameters
    ----------
    vector : numpy array
        A 2d numpy array represenenting a grayscale image or some similar

    Returns
    -------
    numpy array
        Array of 32bit ints each represening (4) 8 bit values for each of RGBA
        colors

    """

    shp = vector.shape
    img = np.empty(shp, dtype=np.uint32)
    view = img.view(dtype=np.uint8).reshape((shp[0], shp[1], 4))
    for i in range(shp[0]):
        for j in range(shp[1]):
            view[i, j, 0] = 0
            view[i, j, 1] = 0
            view[i, j, 2] = 0
            view[i, j, 3] = vector[(shp[0]-1)-i, j]  # Flip image rightside up

    return img


def bokeh_img_plot(img):
    """ Plot an image from a list of grayscale values, or the equivalent

    Parameters
    ----------
    img : numpy array
        A 2d array of 32bit ints

    Returns
    -------
    None

    """

    output_file('input_vector.html', title='input example')

    p = figure(x_range=[0, 5], y_range=[0, 5])
    p.image_rgba(image=[img], x=[0], y=[0], dw=[5], dh=[5], dilate=True)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    show(p)

    return None


def bokeh_heatmap(vector):
    """ Creates a heatmap from a 2d numpy array that represent weights of a
    given neural net layer.

    Parameters
    ----------
    vector : numpy array
        A 2d array

    Returns
    -------
    None

    """

    output = [str(x) for x in range(10)]
    weights = [str(x) for x in range(vector.shape[0])]

    # this is the colormap from the plot
    colors = [
        "#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce",
        "#ddb7b1", "#cc7878", "#933b41", "#550b1d"
    ]

    weight = []
    out = []
    color = []
    val = []
    for o in output:
        for w in weights:
            out.append(o)
            weight.append(w)
            strength = vector[w, o]
            val.append(strength)
            color.append(colors[min(int(strength/10000000), 8)])

    output_file('unemployment.html')

    TOOLS = "resize,hover,save,pan,box_zoom,wheel_zoom"

    p = figure(title='Output layer weights',
               x_range=output, y_range=list(weights),
               x_axis_location="above", plot_width=600, plot_height=1200,
               toolbar_location="left", tools=TOOLS)
    source = ColumnDataSource(
        data=dict(
            y=out,
            x=weight,
            weight=val
        )
    )

    p.rect(out, weight, width=1, height=1, source=source,
           color=color, line_color=None)

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = np.pi/3

    hover = p.select(dict(type=HoverTool))
    hover.tooltips = OrderedDict([
        ('output #', '@x'),
        ('node', '@y'),
        ('weight', '@weight')
    ])

    show(p)      # show the plot

if __name__ == '__main__':
    # vector = db_connect()[0][0]
    # n = int(sqrt(len(vector)))
    # vector = convert_np_to_bokeh(np.array(vector).astype(int).reshape((n, n)))

    # bokeh_img_plot(vector)

    fr = open('finnegan/live_pickle.pickle', 'rb')
    network = pickle.load(fr)
    fr.close()
    print(network.layers[1].weights.shape)
    bokeh_heatmap(convert_np_to_bokeh(network.layers[1].weights))
