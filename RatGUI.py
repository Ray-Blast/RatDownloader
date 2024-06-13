""" File that actually handles the cringe ahh handling of the UX """
import tkinter as tk
import downloader as dl


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.title_label = tk.Label(self.frame, text="Download Video\n\n")
        self.title_label.pack()

        self.url = tk.StringVar()
        self.path = tk.StringVar()

        self.url_label = tk.Label(self.frame, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.frame, textvariable=self.url, width=50)
        self.url_entry.pack()

        self.path_label = tk.Label(self.frame, text="Path:")
        self.path_label.pack()
        self.path_entry = tk.Entry(self.frame, textvariable=self.path, width=50)
        self.path_entry.pack()

        self.Download_Button = tk.Button(self.frame, text="Download", command=lambda: self.download_vid_button())
        self.Download_Button.pack()
        self.frame.pack()

    def download_vid_button(self):
        vid_url = self.url.get()
        vid_path = self.path.get()

        dl.downloadVideo(vid_url, vid_path)
        self.url.set("")


def run_app():
    root = tk.Tk()
    root.title("Rat Downloader")
    root.geometry("500x500")
    app = App(root)
    root.mainloop()
