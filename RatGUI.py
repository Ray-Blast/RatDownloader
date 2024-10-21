""" File that actually handles the cringe ahh handling of the UX """
from tkinter import filedialog
import tkinter as tk
import downloader as dl



class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.title_label = tk.Label(self.frame, text="Download\n\n")
        self.title_label.pack()

        with open('savedPath.txt', 'r') as file:
            spath = file.read().rstrip()
        file.close()

        self.url = tk.StringVar()
        self.path = tk.StringVar()
        self.path.set(spath)

        self.url_label = tk.Label(self.frame, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.frame, textvariable=self.url, width=50)
        self.url_entry.pack()

        self.path_label = tk.Label(self.frame, text="Path:")
        self.path_label.pack(pady=(5,0))
        self.directory_button = tk.Button(self.frame, text="Set Directory", command=lambda: self.getDirectory())
        self.directory_button.pack()

        self.Download_Button = tk.Button(self.frame, text="Download", command=lambda: self.download_vid_button())
        self.Download_Button.pack(padx=(0,0), pady=(50,0))
        

        self.frame.pack()

    def download_vid_button(self):
        vid_url = self.url.get()
        vid_path = self.path.get()

        dl.downloadVideo(vid_url, vid_path)
        self.url.set("")

    def getDirectory(self):
        print(self.path.get())
        path_location = filedialog.askdirectory()
        self.path.set(path_location)
        
        if path_location != '':
            with open('savedPath.txt', 'w') as file:
                file.write(path_location)
            file.close()


def run_app():
    root = tk.Tk()
    root.title("Rat Downloader")
    root.geometry("500x500")
    app = App(root)
    root.mainloop()
