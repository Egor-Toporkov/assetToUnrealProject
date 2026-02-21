import time
import os
import py7zr
import threading

DIRPATH = ""


class UnzipUtils7z:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def unzipAll(self):
        z7files = [file for file in os.listdir(
            self.dirpath) if file.endswith(".7z")]
        for zipf in z7files:
            with py7zr.SevenZipFile(self.dirpath + "/" + zipf, "r") as zip_ref:
                zip_ref.extractall(self.dirpath)
        print(f"Done extracting {zipf}")
        print("All files unzipped")

    def deleteZipFiles(self):
        zipfiles = [file for file in os.listdir(
            self.dirpath) if file.endswith(".7z")]
        time.sleep(3)
        print("time_slip over")
        for zipf in zipfiles:
            os.remove(self.dirpath + "/" + zipf)


if __name__ == "__main__":
    folder1 = UnzipUtils7z(DIRPATH)

    thread1 = threading.Thread(target=folder1.unzipAll)
    thread2 = threading.Thread(target=folder1.deleateZipFiles)

    thread1.start()
    thread1.join
    thread2.start()
    thread2.join
