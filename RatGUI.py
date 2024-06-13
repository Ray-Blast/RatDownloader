""" File that actually handles the cringe ahh handling of the UX """
import tkinter as tk
import downloader as dl
from tkinter import ttk

user_url = "https://www.youtube.com/watch?v=_m9LHQjsGYM"
user_path = "downloads"

def download_vid_button(vid_url, path):
    dl.downloadVideo(vid_url, path)


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(self.frame, text="Download Video")
        self.label.pack()
        self.Download_Button = tk.Button(self.frame, text="Download", command=lambda: download_vid_button(user_url, user_path))
        self.Download_Button.pack()
        self.frame.pack()


def run_app():
    root = tk.Tk()
    root.title("Rat Downloader")
    root.geometry("500x500")
    app = App(root)
    root.mainloop()
