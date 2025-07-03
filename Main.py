from Functions import *
from Gui import *
import tkinter as tk
import nightjson
import os

haveImport = checkImport("yt_dlp")
if haveImport:
    if not os.path.exists("./data.json"):
        nightjson.add_to_json("./data.json", {"FirstOpen": 1})
    if nightjson.read_json("./data.json", "FirstOpen") == 1:
        nightjson.add_to_json("./data.json", {"FirstOpen": 0})
        tk.messagebox.showwarning("Предупреждение", "Установите FFmpeg если он у вас отсутствует.\nОн играет роль конвентатора видео в mp4.")

    root = Tk()
    gui = VideoDownloaderGUI(root)
    root.mainloop()

if not haveImport:
    error_root = tk.Tk()
    error_root.withdraw()
    tk.messagebox.showerror(
        "Ошибка",
        "Установите зависимость:\n"
        "YT-dlp https://github.com/yt-dlp/yt-dlp\n"
    )
    error_root.destroy()
