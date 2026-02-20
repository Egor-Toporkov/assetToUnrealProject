from tkinter import *
from tkinter import filedialog
import zipfile
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

        self.folder_name_lable = Label(
            text="Select Folder: ", bg=THEME_COLOR, fg=FONT_COLOR)
        self.folder_name_lable.grid(row=0, column=1)

        # Open button
        self.open_button_image = PhotoImage(file="image/button.png")
        self.openDir_btn = Button(bg=THEME_COLOR, image=self.open_button_image, bd=0,
                                  highlightbackground=THEME_COLOR, highlightthickness=0, command=self.openDirectory)
        self.openDir_btn.grid(row=1, column=1)

        # Central canvas
        self.central_canvas = Canvas(
            width=200, height=200, highlightthickness=0, bg=FONT_COLOR,)
        self.central_text = self.central_canvas.create_text(
            150, 75, width=200, text="", fill=FONT_COLOR, font=("Arrial", 20, "italic"))
        self.central_canvas.grid(row=0, column=0, columnspan=3, pady=50)

        # unzip button
        self.unzip_btn_image = PhotoImage(file="image/button_unzip.png")
        self.unzip_btn = Button(
            image=self.unzip_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOR)
        self.unzip_btn.grid(row=5, column=1)

        # TODO add command
        # csv exporter
        self.csv_btn_image = PhotoImage(file="image/button_csv.png")
        self.csv_btn = Button(image=self.csv_btn_image,
                              bd=0, highlightthickness=0, bg=THEME_COLOR)
        self.csv_btn.grid(row=6, column=1)

        # delete button
        self.delete_btn_image = PhotoImage(file="image/button_delete.png")
        self.delete_btn = Button(image=self.delete_btn_image,
                                 bd=0, highlightthickness=0, bg=THEME_COLOR)
        self.delete_btn.grid(row=6, column=1)

        self.window.mainloop()

    # open dir function
    def openDirectory(self):
        print("Button working")
        self.opened_dir = filedialog.askdirectory()
        self.zip_files = [file for file in os.listdir(
            self.opened_dir) if file .endswith(".zip")]
        self.central_canvas.itemconfig(self.central_text, text=f"{len(
            self.zip_files)} zip files found in: {self.opened_dir}")


if __name__ == "__main__":
    ui = FolderInterface()
