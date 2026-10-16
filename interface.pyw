
"""
    Add a function to save data about downloaded videos into an SQLite database
    Error: The interface does not respond while the download is in progress, when it finishes, the interface starts working again
    Organize it 
"""
from downloader import Download

import customtkinter as ctk

class Interface:
    def __init__(self):
        self.dld = Download()

        self.MP3 = False
        self.MKV = False

        # Window

        self.app = ctk.CTk()
        self.app.title('Clippy')
        self.app.resizable(False, False)
        self.app.geometry('300x250')
       
        ctk.set_appearance_mode('dark')

        # Entry box

        self.entry = ctk.CTkEntry(self.app, placeholder_text='URL')
        self.entry.pack(pady=15)
     
        # MP3 check var
     
        self.check_var1 = ctk.StringVar(value='off')
        self.checkbox1 = ctk.CTkCheckBox(self.app, text='MP3', command=self.check_box_mp3, 
                                          variable=self.check_var1, onvalue='on', offvalue='off')
        self.checkbox1.pack(pady=5)
     
        # MKV check var
     
        self.check_var2 = ctk.StringVar(value='off')
        self.checkbox2 = ctk.CTkCheckBox(self.app, text='MKV', command=self.check_box_mkv, 
                                          variable=self.check_var2, onvalue='on', offvalue='off') 
        self.checkbox2.pack()
     
        # Button
     
        self.button = ctk.CTkButton(self.app, text='Download', command=lambda: self.dld.start_download(
                                        self.entry.get(), self.MP3, self.MKV))
        self.button.pack(pady=20)

        self.app.mainloop()
  
    # MP3 check box

    def check_box_mp3(self):
        if not self.MP3:
            self.MP3 = True

        else:
            self.MP3 = False

        print('[MP3]', self.MP3)

        # MKV check box
    
    # MKV chech box

    def check_box_mkv(self):
        if not self.MKV:
            self.MKV = True

        else:
            self.MKV = False

        print('[MKV]', self.MKV)

Interface()