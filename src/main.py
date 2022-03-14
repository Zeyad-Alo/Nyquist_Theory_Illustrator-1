# please for the love of god https://namingconvention.org/python/ use the pythonic naming convention here

from PyQt5 import QtGui, QtCore, QtWidgets, uic
from pyqtgraph import PlotWidget
import sys
import numpy as np

from classes import *
import interface
import utility as util
import openfile
import viewer


DebugMode = True


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./data/MainWindow.ui', self)

        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./data/icons/icon.png'))
        self.setWindowTitle("Nyquist Theory Illustrator")

       # initialize arrays and variables
        self.sinusoid_creator_array = [Sinusoid()]
        self.sinusoid_index = 0
        self.sinusoid_number = 1
        self.interpolated_signal = SampledSignal()

        interface.init_connectors(self)
        util.printDebug(
            "this should be our print function (DONT USE THE STANDARD print() )")


        # initialize graph objects array/dict
        self.plotter_window_dict = {"Primary": PlotterWindow(self.primaryPlot.plot()),
                                    "Sinusoid": PlotterWindow(self.sinusoidalSignal.plot()),
                                    "Secondary": PlotterWindow(self.reconstructedPlot.plot()),
                                    "Summed": PlotterWindow(self.summedSignal.plot())
                                    }

        # testing graph objects THIS IS AN EXAMPLE :)
        #xAxis = np.linspace(0, np.pi * 2, 200)
        #yAxis = np.sin(xAxis)
        #self.plotter_window_dict["Sinusoid"].plot_reference.setData(
        #    xAxis, yAxis)


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
