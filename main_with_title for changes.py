import PySimpleGUI as psg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import itertools

# Image data
##################################################################
submitlogo = b'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'
helplogo = b'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'
exitlogo = b'iVBORw0KGgoAAAANSUhEUgAAAK4AAAAqCAYAAAAqLWAgAAADvElEQVR4nO2dP0xTURTGb6EiIC3iKm6aaNk0UdkcVFx0MMFFE01g0UQTWRw0ERMdXDDRRBdINNEFooMuog5uqIluBRNHcFSkRf7ZWvM1rdHH63s9591XXnvObyTvvFse3zvc+51zb2PfuncWjKLUGU36B1PqkXiYn3lT7wGTGH+84Y/l+45dZtvsF3JcIZs186m95LgtI7fN5v6T5Lj89Gez0Hec9dzwO4K2oUum7fJF8thhs3znnlkeuWttFDEZd3HwAjkmlkiYlr4j5DiOaAFEq1SHGOGuTb4uZjQqHaP3SRGczA5+9B5ixUlF1ByXm9E6J19UdR03065OPDO/576yYqUibnE237OPHNOc2m2ae/b4Xoe5LYefQ1dYcZIRJ9xCJlNcKFDpfPncM6LarOykvKhSaIi0w7C6hWNApWPsgWtEU/f2YlamwlkwKqVnLvU5cGyulqOHTSyZXPfzrVNvyffCnBYLRoVHqD4uh1r+61w4dsJ3CuCkK/3xv8/YPnyNNba6CMGInHBrST49Y9ZevSlmUgow+ctmeuvAWfInDlO0q+NPTW7qPSmGUyTKnjpDuj4/O0cewwvRwgWLA+fJ3isqUxBu1/Qn8nh4UcK0vnDvWlhrv4gvh220V4E5PYFoUVmjghdFCY4KtwTVS+WIVq0ve6hwS4RdvdIig10iN8fl1vrdoHYkYdFkc/wyeCHwYij20IzrgFMS9kOtL/uocB2gJLwy9sja/eAVK/ZR4bqwNHyTVRJ2AusLXrFiHxWuCyjrclwDJ/GUf0eZwkOF6wLKujZA8w23R1fxRoXrgNueWAluj67iTeTsMGoN3AtqfRybFDntiX7AYtPig10iJ9yNrIGHuSM5OfHEZPpPh3Z/aehUoUQYhYd/iR/cX8zoih1UuB47G2wThTMmGgXxwsUmSGo/rglQWOC0QirrES9c6g4IgMoaCgu5dx/IsfCH1WkIjmjhcrMfKmuAu9iCtwuPV+ETOVcBq2/b5NIzf8VWBnvFbPTUoimHU7DABku1yPhETrhYfYcNSrqcvWJu5zGgKYezb82UMj5nt7EidKrAyZBouqnU28vdjoOM3zp4jhUrHXHC5ZyBYKo4h4Hbx9t+/arrWQ2KN6KEi+zGWRQt3bjle02QPl5bTT2SECNcZDVkNyqYIqyMPqwqyrkApGC7uafRESNcblajLp64UwY093AOkZaKCOFynQrOoXTc0yAN4xBpyYivnFUiyKF0Qb7rIOxmn0ZBvy5KqUs04yp1iQpXqT+MMX8AV786OQwr/qsAAAAASUVORK5CYII='

# TODO: Seperate function draw and get.
def draw_and_get_plot():
    values_to_plot = (100000, 15000000 , 100, 100, 100)
    ind = np.arange(len(values_to_plot))
    width = 0.4

    p1 = plt.bar(ind, values_to_plot, width)

    plt.ylabel('Prices')
    plt.title('Price comparison')
    plt.xticks(ind, ('apple', 'samsung', 'xiaomi', 'huawi', 'LG'))
    plt.yticks(np.arange(2000000, 40000000, 2000000))
    plt.legend((p1[0],), ('Price comparison',))
    fig = plt.gcf()  # if using Pyplot then get the figure from the plot
    return fig

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def make_window(color):
    psg.theme(color)
    window = psg.Window('parin_group', make_and_get_layout(), resizable=True, force_toplevel=True, finalize=True)
    fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, draw_and_get_plot())
    return window

def make_and_get_layout():
    main_layout = [
        [psg.Input(key="url", readonly=True),
         psg.Text('???????? ?????? ???? ???????? ????????', font=('Lucida', 12))],
        [psg.Input(key="page_number", size=(10, 5)),
         psg.Text('???????? ???????? ?????? ?????? ???? ???????????? ????????', font=('Lucida', 12)),
         psg.Combo(['apple', 'samsung', 'xiaomi'], enable_events=True, key="company"),
         psg.Text('???????? ?????? ???? ???????????? ????????', size=(20, 1), font='Lucida')],
        [psg.Multiline(key="output", disabled=True, size=(45, 20), expand_x=True, expand_y=True, k='-MLINE-',
                       justification='right')],
        [psg.Button('', key="submit", image_data=submitlogo),
         psg.Button('', key="Help", image_data=helplogo),
         psg.Button('', key="Exit", image_data=exitlogo)]
    ]

    # TODO:
    _, _, figure_w, figure_h = draw_and_get_plot().bbox.bounds

    plot_layout = [[psg.Text('???????????? ????????', font='Any 18')],
               [psg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')]]

    theme_layout = [[psg.Text("See how elements look under different themes by choosing a different theme here!")],
               [psg.Listbox(values=psg.theme_list(), size=(20, 12), key="THEME LISTBOX", select_mode=True)],
               [psg.Button('Set Theme', key="changetheme")]]

    tabgrp_layout = [
        [psg.TabGroup([
            [psg.Tab('???????????? ????????', main_layout, tooltip='???????????? ????????', element_justification='center'),
             psg.Tab('???????????? ????????', plot_layout),
             psg.Tab('?????????? ????', theme_layout, tooltip='nothing')]], tab_location='centertop', key="tab", title_color='Red',
            tab_background_color='Orange', selected_title_color='black', selected_background_color='White',
            border_width=5)]]
    return tabgrp_layout

def get_price_list(soup):
    span_list = soup.find_all("span", {"class": "item-price"})
    price_list = list()
    for span in span_list:
        try:
            price_list.append(span.contents[0])
        except:
            True
    return price_list

def get_item_list(soup):
    div_list = soup.find_all("div", {"class": "item-title"})
    # print("div_list: ", div_list)
    item_list = list()
    for div in div_list:
        try:
            item_list.append(div.contents[1]["href"].split("_")[1].split("-Mobile")[0])
        except:
            True
    print(div_list)
    return item_list

def scrap_from_emalls_page(values):
    brand_name = values["company"]
    page_number = values["page_number"]
    url = f"https://emalls.ir/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA~Category~39~b~{brand_name}~page~{page_number}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for (item, price) in zip(get_item_list(soup), get_price_list(soup)):
        window["output"].print([str(item), str(price)])

    window["url"].update(value=url)
    print([str(values)])

#window information
#############################################################
window = psg.Window('parin_group', make_and_get_layout(), resizable=True, force_toplevel=True, finalize=True)
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, draw_and_get_plot())

while True:
    event, values = window.read()

    if event == "Help":
        psg.Popup('?????? ???????????? ???????? ???????? ???????? ???????? ???????? ?????????????? ???? ???????? ?????? ???????? ???????????????? ?????????????? ??????????')

    if event == "Exit":
        break

    if event == "submit":
        scrap_from_emalls_page(values)

    print(values)
    if event == "changetheme":
        window = make_window(values["THEME LISTBOX"][0])

window.close()