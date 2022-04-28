import matplotlib.pyplot as plt
import numpy as np
from unidecode import unidecode as p2e

class PlotPrice:
    def __init__(self):
        self.plot_price = plt.gcf()
        self.draw_plot()

    def draw_price_list_plot(self, price_list, item_list):
        # print(price_list)
        # print(item_list)
        ind = np.arange(len(price_list[:5]))
        width = 0.4
        prices_list = list()
        for price in price_list:
            split_with_camma = p2e(price.split(" ")[0]).split(",")
            number = str()
            for split_part in split_with_camma:
                number += split_part
            prices_list.append(int(number))

        print(prices_list)
        p1 = plt.bar(ind, prices_list[:5], width)

        plt.xticks(ind, item_list[:5])
        ax = plt.gca()
        ax.tick_params(axis='x', labelrotation=45)
        ##plt.yticks(1, 2)
        plt.show()

        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot
        pass

    def draw_plot(self):
        values_to_plot = (0, 0 , 0, 0, 0)
        ind = np.arange(len(values_to_plot))
        width = 0.4

        p1 = plt.bar(ind, values_to_plot, width)

        plt.ylabel('Prices')
        plt.title('Price comparison')
        plt.legend((p1[0],), ('Price comparison',))
        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot

    def get_plot(self):
        return self.plot_price