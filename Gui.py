from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Text, END, TclError, filedialog, messagebox
from Functions import *
import time

class VideoDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Video Downloader")
        master.geometry("600x400")
        
        # URL input
        self.url_label = Label(master, text="Video URL:")
        self.url_label.pack(pady=5)
        self.url_entry = Entry(master)
        self.url_entry.pack(fill='x', padx=20, pady=5)  # Растягивается по ширине
        
        # Paste button
        self.paste_button = Button(master, text="Вставить", 
                                  command=self.paste_url)
        self.paste_button.pack(pady=5)
        
        # Height selection
        self.height_label = Label(master, text="Resolution:")
        self.height_label.pack(pady=5)
        self.height_options = ["144", "240", "360", "480", "720", "1080", "1440"]
        self.selected_height = StringVar(master)
        self.selected_height.set(self.height_options[4])
        self.height_menu = OptionMenu(master, self.selected_height, *self.height_options)
        self.height_menu.pack(pady=5)  # Растягивается по ширине
        
        # Download button
        self.download_button = Button(master, text="Download", 
                                     command=self.start_download)
        self.download_button.pack(pady=10)
        
        # Message display
        self.message_area = Text(master, height=7, wrap='word', state='disabled')
        self.message_area.pack(fill='both', expand=True, padx=20, pady=20)  # Растягивается по всем осям

    def paste_url(self):
        try:
            clipboard_text = self.master.clipboard_get()
            self.url_entry.insert(0, clipboard_text)
        except TclError:
            self.show_message("Ошибка: Буфер обмена пустой")

    def show_message(self, message):
        self.message_area.config(state='normal')
        self.message_area.delete('1.0', END)
        self.message_area.insert('1.0', message)
        self.message_area.tag_configure("center", justify='center')
        self.message_area.tag_add("center", "1.0", "end")
        self.message_area.config(state='disabled')

    def start_download(self):
        url = self.url_entry.get()
        if not url:
            self.show_message("Ошибка: Введите URL видео")
            return

        height = int(self.selected_height.get())
        
        download_path = filedialog.askdirectory(title="Выберите папку для сохранения")
        if not download_path:
            self.show_message("Ошибка: Не выбрана папка для сохранения")
            return
        infoOfVideo = checkVideo(url)

        try:
            downloadVideo(url, download_path, height)
            self.show_message(f"{infoOfVideo}Видео сохранено в:\n{download_path}")
        except Exception as e:
            self.show_message(f"Ошибка: {str(e)}\n\nСкопируйте это сообщение для отладки.")

if __name__ == "__main__":
    root = Tk()
    gui = VideoDownloaderGUI(root)
    root.mainloop()
