from multiprocessing import freeze_support
from my_window import MyTkWindow


if __name__ == '__main__':
    freeze_support()
    myWindow = MyTkWindow()
    myWindow.start()

