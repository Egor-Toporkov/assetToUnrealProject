from tkinter import *
from tkinter import filedialog
import zipfile
import os
import sys
import glob
import py7zr
import time
import pandas as pd
from unzipUtils import UnzipUtils
from unzipUtils7z import UnzipUtils7z

THEME_COLOR = "#434443"
FONT_COLOR = "#FFFFFF"
CANVAS_COLOR = "#000000"


class FolderInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("UnzipUtils")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.opened_dir = None
        self.zip_files = None

        self.folder_name_lable = Label(
            text="Select Folder: ", bg=THEME_COLOR, fg=FONT_COLOR)
        self.folder_name_lable.grid(row=0, column=0)

        # Open button
        self.open_button_image = PhotoImage(file="image/button.png")
        self.openDir_btn = Button(bg=THEME_COLOR, image=self.open_button_image, bd=0,
                                  highlightbackground=THEME_COLOR, highlightthickness=0, command=self.openDirectory)
        self.openDir_btn.grid(row=1, column=0)

        # Central canvas
        self.central_canvas = Canvas(
            width=600, height=200, highlightthickness=0, bg=CANVAS_COLOR,)
        self.central_text = self.central_canvas.create_text(
            200, 75, width=300, text="", fill="white", font=("Arial", 14, "italic"))
        self.central_canvas.grid(row=2, column=0, columnspan=3, pady=0)

        # unzip button
        self.unzip_btn_image = PhotoImage(file="image/button_unzip.png")
        self.unzip_btn = Button(
            image=self.unzip_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.unzipAllBtn)
        self.unzip_btn.grid(row=3, column=0)

        # TODO add command
        # csv exporter
        self.csv_btn_image = PhotoImage(file="image/button_csv.png")
        self.csv_btn = Button(image=self.csv_btn_image,
                              bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.exportCsv)
        self.csv_btn.grid(row=3, column=1)

        # delete button
        self.delete_btn_image = PhotoImage(file="image/button_delete.png")
        self.delete_btn = Button(image=self.delete_btn_image,
                                 bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.deleteZipFiles)
        self.delete_btn.grid(row=3, column=2)

        self.window.mainloop()

    # open dir function
    def openDirectory(self):
        print("Button working")
        self.opened_dir = filedialog.askdirectory()
        self.zip_files = [file for file in os.listdir(
            self.opened_dir) if file .endswith(".zip")]
        self.central_canvas.itemconfig(self.central_text, text=f"{len(
            self.zip_files)} zip files found in: {self.opened_dir}")

    def count_non_archive_files(self, dirpath):
        total = 0
        archives = 0
        for item in os.listdir(dirpath):
            if item.endswith(('.zip', '.7z')):
                archives += 1
            else:
                total += 1
        return total, archives

    def unzipAllBtn(self):
        if not self.opened_dir:
            print("No directory selected")
            return

        before_non_arch, before_arch = self.count_non_archive_files(
            self.opened_dir)
        print(
            f"Before: {before_non_arch} non-archive files, {before_arch} archives")

        # Try standard zip utils first
        try:
            zip1 = UnzipUtils(self.opened_dir)
            zip1.unzipAll()
            print("Standard unzip completed")
        except Exception as e:
            print(f"Standard unzip failed: {e}")

        after_non_arch, after_arch = self.count_non_archive_files(
            self.opened_dir)
        print(f"After standard: {
              after_non_arch} non-archive files, {after_arch} archives")

        if after_non_arch == before_non_arch:  # No change = standard didn't unzip anything
            print("Fallback to 7z")
            try:
                zip2 = UnzipUtils7z(self.opened_dir)
                zip2.unzipAll()
                print("7z unzip completed")
            except Exception as e2:
                print(f"7z unzip failed: {e2}")
        else:
            print("Standard unzip worked - no 7z needed")

    def deleteZipFiles(self):
        for zfile in self.zip_files:
            os.remove(self.opened_dir + "/" + zfile)

        zipfiles = [file for file in os.listdir(
            self.opened_dir) if file.endswith(".7z")]
        time.sleep(.5)
        print("time_slip over")
        for zipf in zipfiles:
            os.remove(self.opened_dir + "/" + zipf)

    def exportCsv(self):
        dirpath = self.opened_dir
        fbx_files = []

        for x in os.walk(dirpath):
            for y in glob.glob(os.path.join(x[0], "*.fbx")):
                fbx_files.append(y)

        h = {"fbx_files": fbx_files}

        df = pd.DataFrame(h)
        df.to_csv("file_list.csv")

        data = pd.read_csv("file_list.csv")
        print(data)


if __name__ == "__main__":
    ui = FolderInterface()
