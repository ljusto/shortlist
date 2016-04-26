__author__ = 'Lambert Justo'

from src.ShortlistUI import ShortlistUI
from tkinter import Tk

def main():
    top = Tk()
    app = ShortlistUI(top)
    top.mainloop()

if __name__ == "__main__":
    main()
