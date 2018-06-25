from tkinter import Frame, Label, Button

from DataAnalysis import DataAnalysis
from DrawCenter import DrawCenter
from WriteDataToJson import WriteDataToJson


class GuiClass(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.click_show())
        self.quitButton.pack()

    def click_show(self):
        analy = DataAnalysis()
        data = analy.analysis_data('1482849',0)
        drawer = DrawCenter()
        drawer.drawSimple(data)