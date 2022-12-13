import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube

window = tk.Tk()
window.title("Youtube Downloader")
window.minsize(505, 200)

def Body():
    link_case = tk.Label(window, text="Video Link")
    link_case.grid(row=0, padx=20, pady=20)
    link_case.config(font=("None", 15), fg="blue")

    link_input = tk.Entry(window, width=40, textvariable=video_link)
    link_input.grid(row=0, column=1)

    locate_case = tk.Label(window, text="Location")
    locate_case.grid(row=1, padx=20, pady=20)
    locate_case.config(font=("None", 15), fg="blue")

    locate_input = tk.Entry(window, width=30, textvariable=download_add)
    locate_input.grid(row=1, column=1, sticky="W")

    locate_button = tk.Button(window, text="Browse", width=10, bg="blue", fg="white", command=Browse)
    locate_button.grid(row=1, column=2)

    download_button = tk.Button(text="Download", width=20, height=1, bg="green", fg="white", command=Download)
    download_button.grid(row=2, column=1, pady=10)

def Browse():
    address = askdirectory(initialdir="Your Address", title="Browse For Folders")
    download_add.set(address)

def Download():
    link = video_link.get()
    save_at = download_add.get()
    yt_downloader = YouTube(link)
    yt_downloader.streams.filter(file_extension="mp4").get_lowest_resolution().download(save_at)
    messagebox.showinfo(title="Youtube Downloader", message="Download video was successful")

download_add = tk.StringVar()
video_link = tk.StringVar()

Body()
window.mainloop()
