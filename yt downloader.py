import tkinter
import tkinter as tk
import yt_dlp
import threading

def display_text():
    url = entry.get().strip()
    button.config(state="disabled")
    label.config(text="Downloading")
    def vid_download():
        ydl_opts = {'outtmpl': 'C:/Users/varni/Desktop/%(title)s.%(ext)s',
                    'format': 'bestvideo+bestaudio/best'}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            label.config(text="Download complete!", fg="green")
        except Exception as e:
            label.config(text="Download failed!")
    threading.Thread(target=vid_download, daemon=True).start()


huh = tk.Tk()
huh.title("Youtube downloader")
huh.geometry("500x300")

Title = tk.Label(huh, text="Enter Youtube Video Link Here")
Title.pack(pady=(50,5))

entry = tk.Entry(huh)
entry.pack(pady=(5,50), expand=True)

button = tk.Button(huh, text="Submit", command=display_text)
button.pack()

label = tk.Label(huh, text="")
label.pack(pady=(5,10))

huh.mainloop()