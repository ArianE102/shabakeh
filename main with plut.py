import PySimpleGUI as psg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests



#image data
##################################################################


     #user interface
submitlogo = b'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'
helplogo = b'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'
exitlogo = b'iVBORw0KGgoAAAANSUhEUgAAAK4AAAAqCAYAAAAqLWAgAAADvElEQVR4nO2dP0xTURTGb6EiIC3iKm6aaNk0UdkcVFx0MMFFE01g0UQTWRw0ERMdXDDRRBdINNEFooMuog5uqIluBRNHcFSkRf7ZWvM1rdHH63s9591XXnvObyTvvFse3zvc+51zb2PfuncWjKLUGU36B1PqkXiYn3lT7wGTGH+84Y/l+45dZtvsF3JcIZs186m95LgtI7fN5v6T5Lj89Gez0Hec9dzwO4K2oUum7fJF8thhs3znnlkeuWttFDEZd3HwAjkmlkiYlr4j5DiOaAFEq1SHGOGuTb4uZjQqHaP3SRGczA5+9B5ixUlF1ByXm9E6J19UdR03065OPDO/576yYqUibnE237OPHNOc2m2ae/b4Xoe5LYefQ1dYcZIRJ9xCJlNcKFDpfPncM6LarOykvKhSaIi0w7C6hWNApWPsgWtEU/f2YlamwlkwKqVnLvU5cGyulqOHTSyZXPfzrVNvyffCnBYLRoVHqD4uh1r+61w4dsJ3CuCkK/3xv8/YPnyNNba6CMGInHBrST49Y9ZevSlmUgow+ctmeuvAWfInDlO0q+NPTW7qPSmGUyTKnjpDuj4/O0cewwvRwgWLA+fJ3isqUxBu1/Qn8nh4UcK0vnDvWlhrv4gvh220V4E5PYFoUVmjghdFCY4KtwTVS+WIVq0ve6hwS4RdvdIig10iN8fl1vrdoHYkYdFkc/wyeCHwYij20IzrgFMS9kOtL/uocB2gJLwy9sja/eAVK/ZR4bqwNHyTVRJ2AusLXrFiHxWuCyjrclwDJ/GUf0eZwkOF6wLKujZA8w23R1fxRoXrgNueWAluj67iTeTsMGoN3AtqfRybFDntiX7AYtPig10iJ9yNrIGHuSM5OfHEZPpPh3Z/aehUoUQYhYd/iR/cX8zoih1UuB47G2wThTMmGgXxwsUmSGo/rglQWOC0QirrES9c6g4IgMoaCgu5dx/IsfCH1WkIjmjhcrMfKmuAu9iCtwuPV+ETOVcBq2/b5NIzf8VWBnvFbPTUoimHU7DABku1yPhETrhYfYcNSrqcvWJu5zGgKYezb82UMj5nt7EidKrAyZBouqnU28vdjoOM3zp4jhUrHXHC5ZyBYKo4h4Hbx9t+/arrWQ2KN6KEi+zGWRQt3bjle02QPl5bTT2SECNcZDVkNyqYIqyMPqwqyrkApGC7uafRESNcblajLp64UwY093AOkZaKCOFynQrOoXTc0yAN4xBpyYivnFUiyKF0Qb7rIOxmn0ZBvy5KqUs04yp1iQpXqT+MMX8AV786OQwr/qsAAAAASUVORK5CYII='

#plut data
##################################################################

values_to_plot = (100000, 15000000 , 100, 100, 100)
ind = np.arange(len(values_to_plot))
width = 0.4

p1 = plt.bar(ind, values_to_plot, width)

plt.ylabel('Prices')
plt.title('Price comparison')
plt.xticks(ind, ('apple', 'samsung', 'xiaomi', 'huawi', 'LG'))
plt.yticks(np.arange(2000000, 40000000, 2000000))
plt.legend((p1[0],), ('Price comparison',))

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds


#layout1:scarpper
##############################################################

layout1 =  [
            [psg.Input(key="url", readonly=True),
             psg.Text('لینک خود را وارد کنید', font=('Lucida', 12))],
            [psg.Input(key="page_number",size=(10,5)),
             psg.Text('صفحه مورد نظر خود را انتخاب کنید',font=('Lucida', 12)),
             psg.Combo(['apple', 'samsung', 'xiaomi'], enable_events=True,key="company"),
             psg.Text('برند خود را انتخاب کنید', size=(20, 1), font='Lucida')],
            [psg.Multiline(key="output", disabled=True, size=(45, 20), expand_x=True, expand_y=True, k='-MLINE-', justification='right')],
            [psg.Button('', key="test", image_data=submitlogo),
             psg.Button('', key="Help", image_data=helplogo),
             psg.Button('', key="Exit", image_data=exitlogo )]
            ]



#layout2:plut
##############################################################

layout2 =[[psg.Text('مقايسه قيمت', font='Any 18')],
          [psg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')]]



#layout3:theme menu
##############################################################
layout3 =[[psg.Text("See how elements look under different themes by choosing a different theme here!")],
          [psg.Listbox(values=psg.theme_list(),size=(20, 12), key="THEME LISTBOX", select_mode=True)],
          [psg.Button('Set Theme', key="changetheme")]]


#tabs maker
#############################################################
tabgrp = [
            [psg.TabGroup([
            [psg.Tab('دريافت قيمت', layout1,tooltip='دريافت قيمت', element_justification='center'),
             psg.Tab('نمودار قيمت', layout2),
             psg.Tab('تعويض تم', layout3,tooltip='nothing')]], tab_location='centertop',key="tab",title_color='Red', tab_background_color='Orange', selected_title_color='black', selected_background_color='White', border_width=5)]]


#window information
#############################################################
window = psg.Window('parin_group', tabgrp, resizable=True, force_toplevel=True, finalize=True)
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

#events
#############################################################
while True  :
    event, values = window.read()
    if event == "Help":
        psg.Popup('اين برنامه براي پيدا كردن سريع قيمت محصولات از سايت هاي فروش اينترنتي استفاده ميشود')
    if event == "Exit":
        break

   # if event == "changetheme":

    print("event: ",event)
    # values -> dictionary type { key -> value }
    print("mydivs: ", values)
    model_to_brand_number = dict()
    model_to_brand_number["samsung"] = "Samsung"
    model_to_brand_number["apple"] = "Apple"
    model_to_brand_number["xiaomi"] = "Xiaomi"

    brand_number = model_to_brand_number[values["company"]]
    page_number = values["page_number"]

    url = f"https://emalls.ir/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA~Category~39~b~{brand_number}~page~{page_number}"
    values["url"] = url
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    myprice = soup.find_all("span", {"class": "item-price"})
    price_list = list()
    for span in myprice:
        try:
            price_list.append(span.contents[0])
        except:
            True
    myitem = soup.find_all("div", {"class": "item-title"})
    item_list = list()
    for div in myitem:
        try:
            item_list.append(div.contents[0])
        except:
            True

      # ba break window mitoni on dade haro tamiz tar dar biyari

    for price in price_list:
        window["output"].print([str(price)])
        apple = price

    for item in item_list:
        window["output"].print([str(item)])


    window["url"].update(value=url)
    print([str(values)])
event, values = window.read()

window.read()
window.close()