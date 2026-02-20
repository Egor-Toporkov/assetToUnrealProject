from tkinter import *
import os
import sys
import glob
import pandas as pd

THEME_COLOR = "#434443"
FONT_COLOR = "#000000"


class FolderInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.opened_dir = None
        self.zip_files = None

        self.folder_name_lable = Lable(
            text="Select Folder: ", bg=THEME_COLOR, fg=FONT_COLOR)

        self.window.mainloop()


if __name__ == "__main__":
    ui = FolderInterface()
